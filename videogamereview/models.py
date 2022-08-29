from videogamereview import db


class Game(db.Model):
    # schema for the Game model
    id = db.Column(db.Integer, primary_key=True)
    game_name = db.Column(db.String(50), unique=True, nullable=False)
    developer = db.Column(db.String(50), nullable=False)
    genre = db.Column(db.String(30), nullable=False)
    release_year = db.Column(db.Integer, nullable=False)
    game_description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return (
            f"{self.id} - Game: {self.game_name} | Developer: {self.developer}"
            f" | Genre: {self.genre} | Release Year: {self.release_year} |"
            f" Description: {self.game_description}"
        )


class User(db.Model):
    # schema for User model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(260), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} | User: {1}".format(
            self.id, self.username
        )
