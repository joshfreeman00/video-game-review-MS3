from flask import render_template
from videogamereview import app, db


@app.route("/")
def home():
    return render_template("base.html")