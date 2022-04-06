"""APIs and Requests for Travel Bucketlist App."""

import requests
import os

API_KEY = os.environ['GOOGLE_PLACES_KEY']


def get_point_location(location):
    """Gets the lat/lng of a Location."""
    
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={location}&key={API_KEY}"

    payload = {}
    headers = {}
    
    response = requests.request("GET", url, headers=headers, data=payload)
    search_results = response.json()
    results = search_results['results']
    result = results[0]
    geometry = result['geometry']
    point_location = geometry['location']
    
    lat = point_location['lat']
    lng = point_location['lng']

    location_dict = {
        "lat": lat,
        "lng": lng
    }

    return location_dict



def travel_data(location_dict, location, category):
    """Returns data from Google Places API."""

    lat = location_dict['lat']
    lng = location_dict['lng']

    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat}%2C{lng}&radius=20000&keyword=things%20to%20do%20in%20{location}&type={category}&rankby=prominence&key={API_KEY}"
    
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    search_results = response.json()
    results = search_results['results']

    category_list = []
    category_photos = []
    category_ratings = []

    for result in results:
        item = result['name']
        rating = result['rating']
        if "photos" in result:
            photos = result['photos']
            photo_ref = photos[0]['photo_reference']
            photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photo_reference={photo_ref}&key={API_KEY}"
            category_photos.append(photo_url)
        else:
            category_photos.append("")
        category_list.append(item)
        category_ratings.append(rating)

    category_items = category_list[:5]
    category_photos = category_photos[:5]
    category_ratings = category_ratings[:5]
    zipped_category = zip(category_list, category_photos, category_ratings)
    category_test = list(zipped_category)

    return category_items, category_test






    # """Category 2."""

    # url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=48.856614%2C2.3522219&radius=20000&keyword=things%20to%20do%20in%20{location}&type={category2}&rankby=prominence&key={API_KEY}"
    
    # payload = {}
    # headers = {}

    # response = requests.request("GET", url, headers=headers, data=payload)
    # search_results = response.json()
    # results = search_results['results']
    # category2_list = []
    # category2_photos = []
    # for result in results:
    #     item = result['name']
    #     if "photos" in result:
    #         photos = result['photos']
    #         photo_ref = photos[0]['photo_reference']
    #         photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photo_reference={photo_ref}&key={API_KEY}"
    #         category2_photos.append(photo_url)
    #     else:
    #         category2_photos.append("")
    #     category2_list.append(item)
    # category2_items = category2_list[:5]
    # category2_photos = category2_photos[:5]
    # category2_test = list(zip(category2_list, category2_photos))



    # """Category 3."""

    # url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=48.856614%2C2.3522219&radius=20000&keyword=things%20to%20do%20in%20{location}&type={category3}&rankby=prominence&key={API_KEY}"
    
    # payload = {}
    # headers = {}

    # response = requests.request("GET", url, headers=headers, data=payload)
    # search_results = response.json()
    # results = search_results['results']
    # category3_list = []
    # category3_photos = []
    # for result in results:
    #     item = result['name']
    #     if "photos" in result:
    #         photos = result['photos']
    #         photo_ref = photos[0]['photo_reference']
    #         photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photo_reference={photo_ref}&key={API_KEY}"
    #         category3_photos.append(photo_url)
    #     else:
    #         category3_photos.append("")
    #     category3_list.append(item)
    # category3_items = category3_list[:5]
    # category3_photos = category3_photos[:5]
    # category3_test = list(zip(category3_list, category3_photos))