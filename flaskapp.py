import regex as re

from flask import Flask, render_template

from cltk.tokenize.sentence import TokenizeSentence
from cltk.tokenize.word import WordTokenizer

from flask_pie import PieController
from flask_pie.utils import DataIterator
from flask_pie.formatters.glue import GlueFormatter as SourceGlueFormatter


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

        # Fix regarding the current issue of apostrophe
        # https://github.com/cltk/cltk/issues/925#issuecomment-522065530
        # On the other hand, it creates empty tokens...
        data = data.replace("'", " ' ")

        for sentence in self.sentence_tokenizer.tokenize_sentences(data):
            toks = self.word_tokenizer.tokenize(sentence)
            new_sentence = []

            for tok in toks:
                out = self.replacer(tok)
                self.tokens.append((len(self.tokens), tok, out))
                new_sentence.append(out)

            yield new_sentence


class GlueFormatter(SourceGlueFormatter):
    HEADERS = ["form", "lemma", "POS", "morph", "treated_token"]
    MORPH_PART = ["Case", "Numb", "Deg", "Mood", "Tense", "Voice", "Person"]
    PONCTU = re.compile(r"^\W+$")

    def __init__(self, tokenizer_memory):
        super(GlueFormatter, self).__init__([])
        self.tokenizer_memory = tokenizer_memory

    def rule_based(cls, token):
        if cls.PONCTU.match(token):
            return [token, token, "PUNC", "MORPH=empty", token]
        elif token.startswith("-"):
            if token == "-ne":
                lemma = "ne_2"
            else:
                lemma = token[1:]
            return [token, lemma, "CONcoo", "MORPH=empty", token]

        return None


# Add the lemmatizer routes
tokenizer = MemoryzingTokenizer()
controller = PieController(model_file="<model.tar,lemma,Voice,Mood,Deg,Numb,Person,Tense,Case,Gend,pos>",
                           headers={"X-Accel-Buffering": "no"},
                           formatter_class=GlueFormatter(tokenizer),
                           iterator=DataIterator(
                               tokenizer=tokenizer,
                               remove_from_input=DataIterator.remove_punctuation
                           ),
                           batch_size=16,
                           force_lower=True
                           )
controller.init_app(app)


if __name__ == "__main__":
    app.run(debug=True)
