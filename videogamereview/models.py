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
        return "#{0} - Game: {1} | Developer: {2} | Genre: {3} | Release Year: {4} | Description: {5}".format(
            self.id, self.game_name, self.developer, self.genre, self.release_year, self.game_description
        )


class User(db.Model):
    # schema for User model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} | User: {1}".format(
            self.id, self.username
        )
