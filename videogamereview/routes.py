from flask import (render_template, request,
    redirect, session, url_for
    )
from videogamereview import app, db, mongo
from videogamereview.models import Game, User


@app.route("/")
def home():
    return render_template("reviews.html")


@app.route("/games")
def games():
    return render_template("games.html")


@app.route("/add_game", methods=["GET", "POST"])
def add_game():
    if request.method == "POST":
        game = Game(
            game_name=request.form.get("game_name"),
            developer=request.form.get("developer"),
            genre=request.form.get("game_name"),
            release_year=Int(request.form.get("release_year")),
            game_description=request.form.get("game_description")
        )
        db.session.add(game)
        db.session.commit()
