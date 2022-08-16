from flask import (render_template, request,
    redirect, session, url_for
    )
from videogamereview import app, db, mongo
from videogamereview.models import Game, User


@app.route("/")
def home():
    return render_template("base.html")
