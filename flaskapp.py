from flask import Flask, render_template

from flask_pie import PieController
from flask_pie.disambiguator.autocat import Autocat
from autocat import NeedsDisambiguation, StraightAutodisambiguation, CategoryAutodisambiguation, GroupAutodisambiguation

from modules import get_iterator_and_formatter

pos = CategoryAutodisambiguation.from_file("./latin-pos.json", category_key="pos", lemma_key="lemma")
straight = StraightAutodisambiguation.from_file("./latin-straight.json", lemma_key="lemma")
impossible = NeedsDisambiguation.from_file("./latin-needs.json", lemma_key="lemma")
group = GroupAutodisambiguation(lemma_key="lemma", categorizers=(straight, pos, impossible))

app = Flask(__name__, static_folder="./statics", template_folder="./templates")


@app.route("/")
def form():
    return render_template("index.html")


# Add the lemmatizer routes
controller = PieController(
    model_file="<model.tar,lemma,Voice,Mood,Deg,Numb,Person,Tense,Case,Gend,pos>",
    headers={"X-Accel-Buffering": "no"},
    get_iterator_and_formatter=get_iterator_and_formatter,
    batch_size=16,
    force_lower=False,
    disambiguation=Autocat(autocat_categorizer=group, lemma_key="lemma")
)
controller.init_app(app)


if __name__ == "__main__":
    app.run(debug=True)
