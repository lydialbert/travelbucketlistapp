"""Models for Travel Bucketlist App."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A User."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fname = db.Column(db.String, nullable=False)
    lname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    bucketlists = db.relationship("Bucketlist", back_populates="user")
    bucketlist_items = db.relationship("Item", back_populates="user")

    def __repr__(self):
        return f'<User user_id={self.user_id} first_name={self.fname} email={self.email}>'


class Bucketlist(db.Model):
    """A Bucketlist."""

    __tablename__ = "bucketlists"

    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    bucketlist_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    location = db.Column(db.String, nullable=False)
    category1 = db.Column(db.String)
    category2 = db.Column(db.String)
    category3 = db.Column(db.String)

    user = db.relationship("User", back_populates="bucketlists")
    bucketlist_items = db.relationship("Item", back_populates="bucketlist")

    def __repr__(self):
        return f"<Bucketlist bucketlist={self.bucketlist_id} location={self.location}>"


class Item(db.Model):
    """A Bucketlist Item."""

    __tablename__ = "bucketlist_items"

    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    bucketlist_id = db.Column(db.Integer, db.ForeignKey("bucketlists.bucketlist_id"), nullable=False)
    item_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item_category = db.Column(db.String, nullable=False)
    item_title = db.Column(db.String, nullable=False)
    item_bio = db.Column(db.Text)
    item_img = db.Column(db.String)

    user = db.relationship("User", back_populates="bucketlist_items")
    bucketlist = db.relationship("Bucketlist", back_populates="bucketlist_items")

    def __repr__(self):
        return f"<Item item={self.item_id} title={self.item_title}>"


def connect_to_db(flask_app, db_uri="postgresql:///bucketlists", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app
    
    connect_to_db(app)
    db.create_all()