from flask import (render_template, request,
    redirect, session, url_for
    )
from videogamereview import app, db, mongo
from videogamereview.models import Game, User


@app.route("/")
@app.route("/get_reviews")
def get_reviews():
    reviews = list(mongo.db.tasks.find())
    return render_template("reviews.html")


@app.route("/add_review" methods=["GET", "POST"])
def add_review():
    if "user" not in session:
        flash("You must be logged in to write a review!")
        return redirect("get_reviews")
    
    if request.method == "POST":
        review = {
            "review_title": request.form.get("review_title"),
            "review_by": session["user"],
            "game_name": request.form.get("game_name"),
            "review_desc": request.form.get("review_desc")
        }
        mongo.db.reviews.insert_one(review)
        flash("You have wrote a review!")
        return redirect(urlfor("get_reviews"))
    
    games = list(Game.query.order_by(Game.game_name).all())
    return render_template("add_review.html", games=games)


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    review = mongo.db.tasks.find_one({"_id": ObjectId(review_id)})

    if "user" is not in session or session["user"] != review["review_by"]:
        flash("Only the review author can edit this!")
        return redirect(url_for("get_reviews"))
    
    if request.method == "POST":
        submit = {
            "review_title": request.form.get("review_title"),
            "review_by": session["user"],
            "game_name": request.form.get("game_name"),
            "review_desc": request.form.get("review_desc")
        }
        mongo.db.tasks.update({"_id": ObjectId(review_id)}, submit)
        flash("You have successfully updated your review!")
    
    games = list(Game.query.order_by(Game.game_name).all())
    return render_template("add_review.html", games=games)


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


# the User Authentication code below is from the Code Institute lessons by Matt

# routes for registeration
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = User.query.filter(User.user_name == \
            request.form.get("username").lower()).all()
    
        if existing_user:
            flash("Username is taken! Please try another username.")
            return redirect(url_for("register"))

        user = User(
                user_name=request.form.get("username").lower(),
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
        existing_user = User.query.filter(User.user_name == \
                                           request.form.get("username").lower()).all()

        if existing_user:
            print(request.form.get("username"))
            # check if the hashed password matches user input
            if check_password_hash(
                    existing_user[0].password, request.form.get("password")):
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
        return render_template("profile.html", username=session["user"])

    return redirect(url_for("login"))


# route for logging out of the session
@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))