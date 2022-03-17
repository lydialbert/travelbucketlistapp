"""Server for Travel Bucketlist App."""

from flask import Flask, render_template, request, session
from jinja2 import StrictUndefined

import requests
import json
import secrets.sh

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def loginpage():
    """View login page."""

    return render_template('login.html')


@app.route('/login', methods=['POST'])
def userprofile():
    """View a User's Profile Page."""

    user = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")

    return render_template('profile.html', user=user)


@app.route('/destination', methods=['POST'])
def categories():
    """View the Categories Form Page."""

    location = request.form.get("location")

    return render_template('destination.html', location=location)

@app.route('/travel', methods=['POST'])
def travelcategories():
    """View the Suggested Travel Items Page."""

    category1 = request.form.get("category1")
    category2 = request.form.get("category2")
    category3 = request.form.get("category3")
    
    session['category1'] = category1
    session['category2'] = category2
    session['category3'] = category3

    return render_template('suggestions.html', category1=category1, 
    category2=category2, category3=category3)


@app.route('/bucketlist', methods=['POST'])
def bucketlist():
    """View the final Bucketlist!"""
    
    category1_items = request.form.getlist("category1_items")
    category2_items = request.form.getlist("category2_items")
    category3_items = request.form.getlist("category3_items")
    
    category1 = session.get('category1')
    category2 = session.get('category2')
    category3 = session.get('category3')

    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?key=API_KEY"
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()

    if 'short_name' in data:
        place = data['long_name']
    else:
        place = []


    return render_template('bucketlist.html', category1=category1, 
    category2=category2, category3=category3, category1_items=category1_items, 
    category2_items=category2_items, category3_items=category3_items, place=place, data=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)