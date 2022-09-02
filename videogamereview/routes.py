from flask import flash, render_template, request, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
from videogamereview import app, db, mongo
from videogamereview.models import Game, User


@app.errorhandler(404)
def client_error(error):
    return render_template("errors/404.html"), 404


@app.errorhandler(500)
def server_error(error):
    return render_template("errors/500.html"), 500


@app.route("/")
# route for reviews page
@app.route("/get_reviews")
def get_reviews():
    reviews = list(mongo.db.reviews.find())
    return render_template("reviews.html", reviews=reviews)


# route for adding reviews
@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    if "user" not in session:
        flash("You must be logged in to write a review!")
        return redirect("get_reviews")

    if request.method == "POST":
        game = Game.query.filter(
            Game.game_name == request.form.get("game_name")).first()
        review = {
            "review_title": request.form.get("review_title"),
            "review_by": session["user"],
            "game_name": request.form.get("game_name"),
            "review_desc": request.form.get("review_desc"),
            "review_score": request.form.get("review_score"),
            "game_id": game.id
        }
        mongo.db.reviews.insert_one(review)
        flash("You wrote a review!")
        return redirect(url_for("get_reviews"))

    games = list(Game.query.order_by(Game.game_name).all())
    return render_template("add_review.html", games=games)


# route for editing reviews
@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})

    # checking if the user is the same user that created the review in question
    if "user" not in session or session["user"] != review["review_by"]:
        flash("Only the review author can edit this!")
        return redirect(url_for("get_reviews"))

    if request.method == "POST":
        game = Game.query.filter(
            Game.game_name == request.form.get("game_name")).first()
        submit = {
            "review_title": request.form.get("review_title"),
            "review_by": session["user"],
            "game_name": request.form.get("game_name"),
            "review_desc": request.form.get("review_desc"),
            "review_score": request.form.get("review_score"),
            "game_id": game.id
        }
        mongo.db.reviews.update_one(
            {"_id": ObjectId(review_id)}, {"$set": submit})
        flash("You have successfully updated your review!")
        return redirect(url_for("get_reviews"))

    games = list(Game.query.order_by(Game.game_name).all())
    return render_template("edit_review.html", games=games, review=review)


# route to delete a review
@app.route("/delete_review/<review_id>", methods=["GET", "POST"])
def delete_review(review_id):

    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})

    # check if the user is the same user as the author or is the admin
    if "user" not in session or session["user"] != review["review_by"] or session["user"] != "admin":  # noqa
        flash("Only the review author or admin can delete reviews!")
        return redirect(url_for("get_reviews"))

    mongo.db.reviews.delete_one({"_id": ObjectId(review_id)})
    flash("The review has been successfully deleted.")
    return redirect(url_for("get_reviews"))


# route for games page
@app.route("/get_games")
def get_games():

    games = list(Game.query.order_by(Game.game_name).all())
    return render_template("games.html", games=games)


# route to add a game
@app.route("/add_game", methods=["GET", "POST"])
def add_game():

    # check if the user is admin
    if "user" not in session or session["user"] != "admin":
        flash("You must be admin to add Games!")
        return redirect(url_for("get_games"))

    if request.method == "POST":
        game = Game(
            game_name=request.form.get("game_name"),
            developer=request.form.get("developer"),
            genre=request.form.get("genre"),
            release_year=int(request.form.get("release_year")),
            game_description=request.form.get("game_description")
        )
        db.session.add(game)
        db.session.commit()
        flash("Succesfully added")
        return redirect(url_for("get_games"))
    return render_template("add_game.html")


# route for editing games
@app.route("/edit_game/<int:game_id>", methods=["GET", "POST"])
def edit_game(game_id):
    if "user" not in session or session["user"] != "admin":
        flash("You must be admin to edit Games!")
        return redirect(url_for("get_games"))

    game = Game.query.get_or_404(game_id)
    if request.method == "POST":
        game.game_name = request.form.get("game_name"),
        game.developer = request.form.get("developer"),
        game.genre = request.form.get("genre"),
        game.release_year = int(request.form.get("release_year")),
        game.game_description = request.form.get("game_description")
        db.session.commit()
        flash("Succesfully edited")
        return redirect(url_for("get_games"))
    return render_template("edit_game.html", game=game)


# route for deleteing a game
@app.route("/delete_game/<int:game_id>", methods=["GET", "POST"])
def delete_game(game_id):
    if "user" not in session or session["user"] != "admin":
        flash("You must be admin to delete Games!")
        return redirect(url_for("get_games"))

    game = Game.query.get_or_404(game_id)
    # deleting a game will delte every review associated to the game
    mongo.db.reviews.delete_many({"game_id": int(game.id)})
    # delete in postgres
    db.session.delete(game)
    db.session.commit()
    flash("Succesfully deleted")
    return redirect(url_for("get_games"))


# the User Authentication code below is from the Code Institute lessons by Matt

# routes for registeration
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = User.query.filter(
            User.username == request.form.get(
                "username").lower()).all()

        if existing_user:
            flash("Username is taken! Please try another username.")
            return redirect(url_for("register"))

        user = User(
                username=request.form.get("username").lower(),
                password=generate_password_hash(request.form.get("password"))
            )

        db.session.add(user)
        db.session.commit()

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


# routes for login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = User.query.filter(
            User.username == request.form.get(
                "username").lower()).all()

        if existing_user:
            print(request.form.get("username"))
            # check if the hashed password matches user input
            if check_password_hash(existing_user[0].password, request.form.get("password")):  # noqa
                session["user"] = request.form.get("username").lower()
                flash("Hello, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# route for the users profile
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    if "user" in session:
        reviews = list(mongo.db.reviews.find(
            {'review_by': session["user"].lower()}))
        return render_template(
            "profile.html", username=session["user"], reviews=reviews)

    return redirect(url_for("login"))


# route for logging out of the session
@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))
