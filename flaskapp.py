"""

This module can be run by install the app requirements (`pip install -r requirements-app.txt`)

The goal here is to be able to have, later, a distributed series of APIs that could be using different version of Pie
and run through containers, unified by a public API such as https://github.com/hipster-philology/deucalion which would
then talk to the different micro-services.

How to run for development :
    PIE_MODEL=/home/thibault/dev/pie/model-lemma-2018_10_23-14_05_19.tar FLASK_ENV=development flask run

    where PIE_MODEL is the path to your model

How to run in production :
    gunicorn --workers 2 app:app --env PIE_MODEL=/home/thibault/dev/pie/model-lemma-2018_10_23-14_05_19.tar

    Probably add to this a --bind

Example URL:
    http://localhost:5000/?data=Ci+gist+saint+Martins+el+sains+de+tours.%20Il%20fut%20bon%20rois.

Example curl :
    curl --data "data=Ci gist saint Martins el sains de tours. Il fut bon rois." http://localhost:5000

Example output :
    token	lemma	morph	pos
    ci	ci	DEGRE=-	ADVgen
    gist	jesir	MODE=ind|TEMPS=pst|PERS.=3|NOMB.=s	VERcjg
    saint	saint	NOMB.=s|GENRE=f|CAS=r	ADJqua
    martins	martin	NOMB.=s|GENRE=m|CAS=r	NOMcom
    el	en1+le	NOMB.=s|GENRE=m|CAS=r	PRE.DETdef
    sains	sain	NOMB.=p|GENRE=m|CAS=r	NOMcom
    de	de	MORPH=empty	PRE
    tours	tor2	NOMB.=p|GENRE=f|CAS=r	NOMcom
    .	.	_	PONfrt
    il	il	PERS.=3|NOMB.=s|GENRE=m|CAS=n	PROper
    fut	estre1	MODE=ind|TEMPS=psp|PERS.=3|NOMB.=s	VERcjg
    bon	bon	NOMB.=s|GENRE=m|CAS=n|DEGRE=p	ADJqua
    rois	roi2	NOMB.=s|GENRE=m|CAS=n	NOMcom
    .	.	_	PONfrt

"""
from webapp import bind, Formatter
from flask import Flask, render_template
from pie.tagger import Tagger, simple_tokenizer
import re

app = Flask(__name__, static_folder="./statics", template_folder="./templates")


@app.route("/")
def form():
    return render_template("index.html")

# Forms where the que should be kept
QVE_NOT_REMOVE = ["quicumque", "atque", "neque"]

# Uppercase regexp
uppercase = re.compile("^[A-Z]$")

class MemoryzingTokenizer(object):
    def __init__(self):
        self.tokens = [
        ]

    def replacer(self, inp: str):
        x = inp.replace("v", "u")
        if len(x) > 3 and x[-3:] == "que" and x not in QVE_NOT_REMOVE:
            x = x[:-3]
        return x

    def __call__(self, data: str, lower=True):
        for sentence in simple_tokenizer(data, lower=lower):
            new_sentence = []
            for inp in sentence:
                # Check first if this is a damn "." after an uppercase letter like L.
                if inp == "." and new_sentence and uppercase.match(new_sentence[-1]):
                    _, o_inp, o_out = self.tokens[-1]
                    self.tokens[-1] = (len(self.tokens) - 1, o_inp+".", o_out+".")
                    new_sentence[-1] = o_out+"."
                else:
                    out = self.replacer(inp)
                    self.tokens.append((len(self.tokens), inp, out))
                    new_sentence.append(out)
            yield new_sentence



class GlueFormatter(Formatter):
    HEADERS = ["token", "lemma", "POS", "morph", "treated_token"]
    MORPH_PART = ["Case", "Numb", "Deg", "Mood", "Tense", "Voice", "Person"]
    PONCTU = re.compile("\W")

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
            print(self.tokenizer_memory.tokens)
            raise Exception("The output token does not match our inputs %s : %s" % (token, out_token))

        if GlueFormatter.PONCTU.match(token):
            return [
                token,
                token,
                "PUNC",
                "MORPH=empty",
                token
            ]

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
bind(app, formatter_class=GlueFormatter(tokenizer), route_path="/api", tokenizer=tokenizer)

if __name__ == "__main__":
    app.run(debug=True)