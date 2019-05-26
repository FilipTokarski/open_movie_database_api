import requests


def get_movie(title):
    request = requests.get('http://omdbapi.com/?apikey=258211c2&t={}'.format(title))
    data = request.json()
    return data