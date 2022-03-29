"""APIs and Requests for Travel Bucketlist App."""

import requests


"""Food Requests in Sydney, AUS."""

url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=500&types=food&name=harbour&key=AIzaSyATYk66toeHx7smEeVhhWw-fI-iNTNUnXw"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
search_results = response.json()
results = search_results['results']
restaurant_list = []
for result in results:
    restaurant = result['name']
    restaurant_list.append(restaurant)
print(restaurant_list)


"""Museum Requests in Syndey, AUS."""

url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=500&types=museum&key=AIzaSyATYk66toeHx7smEeVhhWw-fI-iNTNUnXw"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
search_results = response.json()
results = search_results['results']
museum_list = []
for result in results:
    museum = result['name']
    museum_list.append(museum)
print(museum_list)


"""Shopping Requests in Syndey, AUS."""

url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=500&types=shopping_mall&name=harbour&key=AIzaSyATYk66toeHx7smEeVhhWw-fI-iNTNUnXw"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
search_results = response.json()
results = search_results['results']
print(results[0]['name'])
shopping_list = []
for result in results:
    shop = result['name']
    shopping_list.append(shop)
print(shopping_list)


"""Park Requests in Syndey, AUS."""

url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=500&types=park&name=harbour&key=AIzaSyATYk66toeHx7smEeVhhWw-fI-iNTNUnXw"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
search_results = response.json()
results = search_results['results']
print(results[0]['name'])
nature_list = []
for result in results:
    park = result['name']
    nature_list.append(park)
print(nature_list)



"""Shopping Requests in Syndey, AUS."""

url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=500&types=food&key=AIzaSyATYk66toeHx7smEeVhhWw-fI-iNTNUnXw"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
search_results = response.json()
results = search_results['results']
print(results[0]['name'])