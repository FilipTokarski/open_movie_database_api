import requests


def get_movie(title):
    try:
        request = requests.get('http://omdbapi.com/?apikey=258211c2&t={}'.format(title))
        data = request.json()
    except:
        data = {"Title": "Sorry, there has been an error"}
        
    return data