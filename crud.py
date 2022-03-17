"""CRUD operations for Travel Bucketlist App."""

from model import db, User, Bucketlist, Item, connect_to_db



def create_user(email, password): #Creating a 'fake user'
    """Return a user."""

    user = User(email=email password=password)

    return user

if __name__ == '__main__':
    from server import app
    connect_to_db(app)