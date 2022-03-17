"""Models for Travel Bucketlist App."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A User."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fname = db.Column(db.String, nullable=False)
    lname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    bucketlists = db.relationship("Bucketlist", back_populates="user")

    def __repr__(self):
        return f'<User user_id={self.user_id} first_name={self.fname} email={self.email}>'



class Bucketlist(db.Model):
    """A Bucketlist."""

    __tablename__ = "bucketlists"

    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    bucketlist_id = db.Column(db.Integer, primary_key=True, autoincrement=True)   #Do I need this column? (Would like each bucketlist made to be associated with the user that made it.)
    location = db.Column(db.String, nullable=False)
    category1 = db.Column(db.String)
    category2 = db.Column(db.String)
    category3 = db.Column(db.String)

    user = db.relationship("User", back_populates="bucketlists")
    #because of backref I can use the bucketlist_items here in this class

    def __repr__(self):
        return f"<Bucketlist bucketlist={self.bucketlist_id} location={self.location}>"


class Item(db.Model):
    """A Bucketlist Item."""

    __tablename__ = "bucketlist_items"

    bucketlist_id = db.Column(db.Integer, db.ForeignKey("bucketlists.bucketlist_id"), nullable=False)
    item_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item_category = db.Column(db.String, nullable=False)
    item_title = db.Column(db.String, nullable=False)
    item_bio = db.Column(db.Text)
    item_img = db.Column(db.String)

    bucketlist = db.relationship("Bucketlist", backref="bucketlist_items")

    def __repr__(self):
        return f"<Item item={self.item_id} title={self.item_title}>"
