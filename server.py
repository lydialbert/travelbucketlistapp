"""Server for Travel Bucketlist App."""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db, db
from jinja2 import StrictUndefined

import os
import requests
import crud

app = Flask(__name__)
app.secret_key = "SECRET"
app.jinja_env.undefined = StrictUndefined

API_KEY = os.environ['GOOGLE_PLACES_KEY']


@app.route('/')
def loginpage():
    """View the Welcome page."""

    return render_template('welcome.html')


@app.route('/about')
def about_page():
    """View the About Page."""

    return render_template('about.html')

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

@app.route('/profile')
def profile_page():
    """View a User's Profile Page."""

    user_id = session['user_id']
    user = crud.get_user_by_id(user_id)

    return render_template('profile.html', user=user.fname)

@app.route('/home')
def homepage():
    """View the User's Profile."""

    return render_template('home.html')

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

    if category1 == 'Other':
        category1 = request.form.get("users_choice")
        print(category1)
    elif category2 == 'Other':
        category2 = request.form.get("users_choice")
        print(category2)
    elif category3 == 'Other':
        category3 = request.form.get("users_choice")
        print(category3)
    else:
        location = request.form.get("location")
        category1 = request.form.get("category1")
        category2 = request.form.get("category2")
        category3 = request.form.get("category3")
    
    session['location'] = location
    session['category1'] = category1
    session['category2'] = category2
    session['category3'] = category3

    user_id = session['user_id']
    user = crud.get_user_by_id(user_id)

    bucketlist = crud.create_bucketlist(user, location, category1, category2, category3)
    db.session.add(bucketlist)
    db.session.commit()
    session["bucketlist_id"] = bucketlist.bucketlist_id



    """Category 1."""

    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={category1}%20in%20{location}&key={API_KEY}"
    
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    search_results = response.json()
    results = search_results['results']
    category1_list = []
    category1_photos = []
    for result in results:
        item = result['name']
        photos = result['photos']
        photo_ref = photos[0]['photo_reference']
        photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photo_reference={photo_ref}&key={API_KEY}"
        category1_photos.append(photo_url)
        category1_list.append(item)
    category1_items = category1_list[:5]
    category1_photos = category1_photos[:5]
    category1_test = list(zip(category1_list, category1_photos))



    """Category 2."""

    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={category2}%20in%20{location}&key={API_KEY}"
    
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    search_results = response.json()
    results = search_results['results']
    category2_list = []
    category2_photos = []
    for result in results:
        item = result['name']
        photos = result['photos']
        photo_ref = photos[0]['photo_reference']
        photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photo_reference={photo_ref}&key={API_KEY}"
        category2_photos.append(photo_url)
        category2_list.append(item)
    category2_items = category2_list[:5]
    category2_photos = category2_photos[:5]
    category2_test = list(zip(category2_list, category2_photos))



    """Category 3."""

    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={category3}%20in%20{location}&key={API_KEY}"
    
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    search_results = response.json()
    results = search_results['results']
    category3_list = []
    category3_photos = []
    for result in results:
        item = result['name']
        photos = result['photos']
        photo_ref = photos[0]['photo_reference']
        photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photo_reference={photo_ref}&key={API_KEY}"
        category3_photos.append(photo_url)
        category3_list.append(item)
    category3_items = category3_list[:5]
    category3_photos = category3_photos[:5]
    category3_test = list(zip(category3_list, category3_photos))


    return render_template('travelpicks.html', 
    location=location, 
    category1=category1, 
    category2=category2, 
    category3=category3,
    category1_items=category1_items, 
    category2_items=category2_items, 
    category3_items=category3_items,
    category1_test=category1_test,
    category2_test=category2_test,
    category3_test=category3_test
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
    category1=category1, 
    category2=category2, 
    category3=category3,
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

    category1_items = crud.get_items_from_bucketlist_in_category(bucketlist_id, bucketlist.category1)
    category2_items = crud.get_items_from_bucketlist_in_category(bucketlist_id, bucketlist.category2)
    category3_items = crud.get_items_from_bucketlist_in_category(bucketlist_id, bucketlist.category3)

    return render_template("bucketlist.html",
    location=bucketlist.location,
    category1=bucketlist.category1,
    category2=bucketlist.category2,
    category3=bucketlist.category3,
    category1_items=category1_items,
    category2_items=category2_items,
    category3_items=category3_items
    )

@app.route('/delete_bucketlist', methods=["POST"])
def delete_bucketlist():
    """Delete a Bucketlist."""

    bucketlist_id = request.json.get("bucketlist_id")
    crud.delete_entire_bucketlist(bucketlist_id)
    db.session.commit()

    return "Success"


@app.route('/logout', methods=["POST"])
def user_logout():
    """Log a User out."""

    return redirect("/")


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)