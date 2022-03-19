"""Server for Travel Bucketlist App."""

from flask import Flask, render_template, request, session

import os
import requests

app = Flask(__name__)
app.secret_key = "SECRET"

API_KEY = os.environ['GOOGLE_PLACES_KEY']



@app.route('/')
def loginpage():
    """View the Welcome/Login page."""

    return render_template('login.html')


@app.route('/profile', methods=['POST'])
def userprofile():
    """View the User's Profile Page."""

    user = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")

    return render_template('profile.html', user=user)


@app.route('/travelform', methods=['POST'])
def travelcategories():
    """View the Suggested Travel Items Page."""

    location = request.form.get("location")

    category1 = request.form.get("category1")
    category2 = request.form.get("category2")
    category3 = request.form.get("category3")
    
    session['location'] = location
    session['category1'] = category1
    session['category2'] = category2
    session['category3'] = category3

    """Google Places API Request for Category 1."""

    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={category1}%20in%20{location}&key={API_KEY}"
    
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    search_results = response.json()
    results = search_results['results']

    category1_list = []
    for result in results:
        item = result['name']
        category1_list.append(item)
    category1_items = category1_list[:5]

    """Google Places API Request for Category 2."""

    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={category2}%20in%20{location}&key={API_KEY}"
    
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    search_results = response.json()
    results = search_results['results']
    category2_list = []
    for result in results:
        item = result['name']
        #photo = result['photo_reference']
        category2_list.append(item)
    category2_items = category2_list[:5]

    """Google Places API Request for Category 3."""

    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={category3}%20in%20{location}&key={API_KEY}"
    
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    search_results = response.json()
    results = search_results['results']
    category3_list = []
    for result in results:
        item = result['name']
        category3_list.append(item)
    category3_items = category3_list[:5]

    return render_template('travelpicks.html', location=location, category1=category1, category2=category2, category3=category3,
    category1_items=category1_items, category2_items=category2_items, category3_items=category3_items)


@app.route('/bucketlist', methods=['POST'])
def bucketlist():
    """View the final Bucketlist!"""
    
    category1_items = request.form.getlist("category1")
    category2_items = request.form.getlist("category2")
    category3_items = request.form.getlist("category3")

    location = session.get('location')
    category1 = session.get('category1')
    category2 = session.get('category2')
    category3 = session.get('category3')

    return render_template('bucketlist.html', location=location, category1=category1, category2=category2, category3=category3,
    category1_items=category1_items, category2_items=category2_items, category3_items=category3_items)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)