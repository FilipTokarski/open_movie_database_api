import requests
from movieguru.local_settings import APIKEY


def get_movie(title):
    """Makes request to omdb api and gets data based on given title"""
    BASE_URL = 'http://omdbapi.com/?'
    payload = {'apikey': APIKEY, 't': title}
    try:
        request = requests.get(BASE_URL, payload)
        data = request.json()
    except:
        raise H
        #data = {"Title": "Sorry, there has been an error"}

    return data