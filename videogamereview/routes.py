from flask import render_template
from videogamereview import app, db
from videogamereview.models import Game, User


@app.route("/")
def home():
    return render_template("base.html")
