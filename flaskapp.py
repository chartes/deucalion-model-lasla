import re

from flask import Flask, render_template

from cltk.tokenize.sentence import TokenizeSentence
from cltk.tokenize.word import WordTokenizer

from flask_pie import PieController
from flask_pie.utils import Formatter, DataIterator


app = Flask(__name__, static_folder="./statics", template_folder="./templates")


@app.route("/")
def form():
    return render_template("index.html")


# Uppercase regexp
uppercase = re.compile("^[A-Z]$")


class MemoryzingTokenizer(object):
    def __init__(self):
        self.tokens = [
        ]

        self.sentence_tokenizer = TokenizeSentence("latin")
        self.word_tokenizer = WordTokenizer("latin")

    def replacer(self, inp: str):
        inp = inp.replace("U", "V").replace("v", "u").replace("J", "I").replace("j", "i")
        return inp

    def __call__(self, data, lower=True):
        if lower:
            data = data.lower()

        for sentence in self.sentence_tokenizer.tokenize_sentences(data):
            toks = self.word_tokenizer.tokenize(sentence)
            new_sentence = []

            for tok in toks:
                out = self.replacer(tok)
                self.tokens.append((len(self.tokens), tok, out))
                new_sentence.append(out)

            yield new_sentence


class GlueFormatter(Formatter):
    HEADERS = ["form", "lemma", "POS", "morph", "treated_token"]
    MORPH_PART = ["Case", "Numb", "Deg", "Mood", "Tense", "Voice", "Person"]
    PONCTU = re.compile(r"^\W+$")

    def __init__(self, tokenizer_memory):
        super(GlueFormatter, self).__init__([])
        self.tokenizer_memory = tokenizer_memory

    def __call__(self, tasks):
        super(GlueFormatter, self).__init__(tasks)
        self.pos_tag = "POS"
        if "POS" not in self.tasks and "pos" in self.tasks:
            self.pos_tag = "pos"
        return self

    def format_headers(self):
        return GlueFormatter.HEADERS

    def format_line(self, token, tags):
        tags = list(tags)
        lemma = tags[self.tasks.index("lemma")]
        index, input_token, out_token = self.tokenizer_memory.tokens.pop(0)
        if token != out_token:
            raise Exception("The output token does not match our inputs %s : %s" % (token, out_token))

        if GlueFormatter.PONCTU.match(token):
            return [
                token,
                token,
                "PUNC",
                "MORPH=empty",
                token
            ]
        elif token.startswith("-"):
            return [token, token[1:].upper().replace("U", "V"), "CONcoo", "MORPH=empty", token]

        return [
            input_token,
            lemma.upper().replace("U", "V"),
            tags[self.tasks.index(self.pos_tag)],
            "|".join(
                "{cat}={tag}".format(
                    cat=morph_part,
                    tag=tags[self.tasks.index(morph_part)]
                )
                for morph_part in GlueFormatter.MORPH_PART
                if morph_part in self.tasks and
                tags[self.tasks.index(morph_part)] != "_"
            ) or "MORPH=empty",
            out_token
        ]


# Add the lemmatizer routes
tokenizer = MemoryzingTokenizer()
controller = PieController(model_file="<lemma.split-morph.tar,lemma,Voice,Mood,Deg,Numb,Person,Tense,Case,Gend>"
                                      "<lemma-pos-morph.tar,pos>", headers={"X-Accel-Buffering": "no"},
                           formatter_class=GlueFormatter(tokenizer),
                           iterator=DataIterator(tokenizer=tokenizer), batch_size=16)
controller.init_app(app)


if __name__ == "__main__":
    app.run(debug=True)
