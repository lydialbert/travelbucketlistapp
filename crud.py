"""CRUD operations for Travel Bucketlist App."""

from model import db, User, Bucketlist, Item, connect_to_db


def create_user(fname, lname, email, password):
    """Create and Return a User."""

    user = User(
        fname=fname,
        lname=lname,
        email=email,
        password=password,
    )

    return user

def get_user_by_id(user_id):
    """Return a User by primary key."""

    return User.query.filter(User.user_id == user_id).first()


def get_user_by_email(email):
    """Return a User by email."""

    return User.query.filter(User.email == email).first()



def create_bucketlist(user, location, category1, category2, category3):
    """Create and Return a Bucketlist."""

    bucketlist = Bucketlist(
        user=user,
        location=location, 
        category1=category1, 
        category2=category2, 
        category3=category3,
    )

    return bucketlist

def get_a_bucketlist_by_bucketlist_id(bucketlist_id):
    """Return a Bucketlist by primary key."""

    return Bucketlist.query.get(bucketlist_id)


def get_a_bucketlist_by_user(user_id):
    """Return a Bucketlist by User."""

    return Bucketlist.query.filter(Bucketlist.user_id == user_id).first()
    

def get_all_bucketlists_by_user(user_id):
    """Return all Bucketlists by User."""

    return Bucketlist.query.filter(Bucketlist.user_id == user_id).all()


def create_bucketlist_item(user_id, bucketlist_id, category, title):
    """Create and Return a Bucketlist Item."""

    bucketlist_item = Item(
        user_id=user_id,
        bucketlist_id=bucketlist_id,
        item_category=category,
        item_title=title,
    )

    return bucketlist_item


def get_items_from_bucketlist_in_category(bucketlist_id, category):
    """Return Items by Category."""

    return Item.query.filter(Item.bucketlist_id == bucketlist_id, Item.item_category == category).all()


def delete_entire_bucketlist(bucketlist_id):
    """Delete all of the Items within a Bucketlist and the Bucketlist."""

    bucketlist_to_delete = get_a_bucketlist_by_bucketlist_id(bucketlist_id)

    Item.query.filter(Item.bucketlist_id == bucketlist_id).delete()
    
    db.session.delete(bucketlist_to_delete)


if __name__ == '__main__':
    from server import app
    connect_to_db(app)