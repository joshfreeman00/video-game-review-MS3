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