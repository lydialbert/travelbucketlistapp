"""Server for Travel Bucketlist App."""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db, db
from jinja2 import StrictUndefined

import os
import requests
import crud
import googleapi

app = Flask(__name__)
app.secret_key = "SECRET"
app.jinja_env.undefined = StrictUndefined

API_KEY = os.environ['GOOGLE_PLACES_KEY']


travel_categories = {
    'park': "Nature and Parks", 
    'art_gallery': "Art Galleries", 
    'museum': "Museums",
    'amusement_park': "Amusement Parks",
    'tourist_attraction': "Tourist Attractions",
    'point_of_interest': "Most Popular",
    'night_club': "Night Life",
    'cafe': "Cafes",
    'restaurant': "Restaurants",
    }

@app.route('/')
def loginpage():
    """View the Welcome page."""

    return render_template('welcome.html')


@app.route('/create_account', methods=["POST"])
def register_user():
    """Create a New User."""

    fname = request.form.get("fname")
    lname = request.form.get("lname")
    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.create_user(fname, lname, email, password)
    db.session.add(user)
    db.session.commit()

    return redirect("/")

@app.route('/login', methods=["POST"])
def process_login():
    """Process a User Login."""

    fname = request.form.get("fname")
    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if user.password != password:
        flash("The password you entered was incorrect.")
        return redirect("/")
    else:
        session["user_id"] = user.user_id
        return render_template('profile.html', user=user.fname)


@app.route("/forgotpassword", methods=['POST'])
def reset_password():
    """Send email to reset a password."""

    flash("Check your email for resetting password instructions.")
    return redirect("/")

@app.route('/profile')
def profile_page():
    """View a User's Profile Page."""

    user_id = session['user_id']
    user = crud.get_user_by_id(user_id)

    return render_template('profile.html', user=user.fname)


@app.route('/createbucketlist')
def bucketlist_form():
    """Create a Bucketlist."""

    return render_template('createbucketlist.html')

@app.route('/travelform', methods=['POST'])
def travelcategories():
    """Complete the Bucketlist Form."""
    
    location = request.form.get("location")
    category1 = request.form.get("category1")
    category2 = request.form.get("category2")
    category3 = request.form.get("category3")

    """'Other' Feature."""
    if category1 == 'Other':
        category1 = request.form.get("category1_choice")
        print(category1)
    if category2 == 'Other':
        category2 = request.form.get("category2_choice")
        print(category2)
    if category3 == 'Other':
        category3 = request.form.get("category3_choice")
        print(category3)
    
    """Store categories in Session for later use."""
    session['location'] = location
    session['category1'] = category1
    session['category2'] = category2
    session['category3'] = category3

    """If a User does not enter in a Location."""
    if location == "":
        flash("Make sure to enter a correct City.")
        return redirect('/createbucketlist')


    """If a User does not select a Category."""
    category_keys = [session['category1'], session['category2'], session['category3']]

    for category in category_keys:
        if category == None:
            flash("Must enter in a category.")
            return redirect('/createbucketlist')


    """Creating a Bucketlist for the User."""
    user_id = session['user_id']
    user = crud.get_user_by_id(user_id)

    bucketlist = crud.create_bucketlist(user, location, category1, category2, category3)
    db.session.add(bucketlist)
    db.session.commit()
    
    session["bucketlist_id"] = bucketlist.bucketlist_id
    
    travel_categories = {
        'park': "Nature and Parks", 
        'art_gallery': "Art Galleries", 
        'museum': "Museums",
        'amusement_park': "Amusement Parks",
        'tourist_attraction': "Tourist Attractions",
        'point_of_interest': "Most Popular",
        'night_club': "Night Life",
        'cafe': "Cafes",
        'restaurant': "Restaurants",
        'zoo': "Zoo",
        'shopping_mall': "Shopping",
        'aquarium': "Aquariums",
        }

    categories = []
    categories.append(travel_categories.get(category1, ""))
    categories.append(travel_categories.get(category2, ""))
    categories.append(travel_categories.get(category3, ""))

    item_lists = []
    test_lists = []

    """Get the lat/lng of the Location."""
    location_dict = googleapi.get_point_location(location)

    """Get each Categories Items"""
    category1_items, category1_test = googleapi.travel_data(location_dict, location, category1)
    item_lists.append(category1_items)
    test_lists.append(category1_test)
    category2_items, category2_test = googleapi.travel_data(location_dict, location, category2)
    item_lists.append(category2_items)
    test_lists.append(category2_test)
    category3_items, category3_test = googleapi.travel_data(location_dict, location, category3)
    item_lists.append(category3_items)
    test_lists.append(category3_test)


    return render_template('travelpicks.html', 
    location=location,
    categories=categories,
    item_lists=item_lists,
    test_lists=test_lists
    )


@app.route('/bucketlist', methods=['POST'])
def bucketlist():
    """View the Bucketlist!"""
    
    category1_items = request.form.getlist("category1")
    category2_items = request.form.getlist("category2")
    category3_items = request.form.getlist("category3")

    location = session.get('location')
    category1 = session.get('category1')
    category2 = session.get('category2')
    category3 = session.get('category3')

    user_id = session['user_id']
    bucketlist_id = session['bucketlist_id']

    for item in category1_items:
        bucketlist_item = crud.create_bucketlist_item(user_id, bucketlist_id, category1, item)
        db.session.add(bucketlist_item)
        db.session.commit()
    
    for item in category2_items:
        bucketlist_item = crud.create_bucketlist_item(user_id, bucketlist_id, category2, item)
        db.session.add(bucketlist_item)
        db.session.commit()

    for item in category3_items:
        bucketlist_item = crud.create_bucketlist_item(user_id, bucketlist_id, category3, item)
        db.session.add(bucketlist_item)
        db.session.commit()

    return render_template('bucketlist.html', 
    location=location, 
    category1=travel_categories[session['category1']], 
    category2=travel_categories[session['category2']], 
    category3=travel_categories[session['category3']],
    category1_items=category1_items, 
    category2_items=category2_items, 
    category3_items=category3_items
    )

@app.route("/mybucketlists")
def show_all_bucketlists():
    """Show all of the User's Bucketlists."""

    user_id = session['user_id']
    bucketlists = crud.get_all_bucketlists_by_user(user_id)

    return render_template("mybucketlists.html", bucketlists=bucketlists)


@app.route('/bucketlist/<bucketlist_id>')
def show_individual_bucketlist(bucketlist_id):
    """Show one Bucketlist."""

    bucketlist = crud.get_a_bucketlist_by_bucketlist_id(bucketlist_id)
    category1_items = crud.get_item_title(bucketlist_id, bucketlist.category1)
    category2_items = crud.get_item_title(bucketlist_id, bucketlist.category2)
    category3_items = crud.get_item_title(bucketlist_id, bucketlist.category3)

    return render_template("bucketlist.html",
    location=bucketlist.location,
    category1=bucketlist.category1,
    category2=bucketlist.category2,
    category3=bucketlist.category3,
    category1_items=category1_items,
    category2_items=category2_items,
    category3_items=category3_items
    )

@app.route("/delete_bucketlist", methods=["POST"])
def delete_bucketlist():
    """Delete a Bucketlist."""

    bucketlist_id = request.json.get("bucketlist_id")
    crud.delete_entire_bucketlist(bucketlist_id)
    db.session.commit()

    return "Success"


@app.route("/logout", methods=["POST"])
def user_logout():
    """Log a User out."""

    return redirect("/")


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)