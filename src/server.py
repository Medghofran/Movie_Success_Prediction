from aiohttp import web
import json
import numpy as np

_classifier = None


def predict(data):
    movie_frame = {
        "title": "Der Vagabund und das Kind (1921)",
        "wordsInTitle": "der vagabund und das kind",
        "imdbRating": 8.4,
        "ratingCount": 40550,
        "duration": 3240,
        "year": 1921,
        "nrOfWins": 1,
        "nrOfNominations": 0,
        "nrOfPhotos": 19,
        "nrOfNewsArticles": 96,
        "nrOfUserReviews": 85,
        "nrOfGenre": 3,
        "Action": 0,
        "Adult": 0,
        "Adventure": 0,
        "Animation": 0,
        "Biography": 0,
        "Comedy": 1,
        "Crime": 0,
        "Documentary": 0,
        "Drama": 1,
        "Family": 1,
        "Fantasy": 0,
        "FilmNoir": 0,
        "GameShow": 0,
        "History": 0,
        "Horror": 0,
        "Music": 0,
        "Musical": 0,
        "Mystery": 0,
        "News": 0,
        "RealityTV": 0,
        "Romance": 0,
        "SciFi": 0,
        "Short": 0,
        "Sport": 0,
        "TalkShow": 0,
        "Thriller": 0,
        "War": 0,
        "Western": 0,
    }

    movie_frame = [
        1,
        0,
        19,
        85,
        3,
        0,
        0,
        0,
        0,
        0,
        1,
        0,
        0,
        1,
        1,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    ]
    movie_frame = np.reshape(data, (1, -1))

    td = _classifier.predict(movie_frame)
    print("\n\n----------------------Prediction Test----------------------\n\n", td)
    return td


async def handle(request):
    request = await request.text()
    print(request)
    request_body = json.loads(request)
    movie_data = []
    movie_data.append(int(request_body['wins']))
    movie_data.append(int(request_body['reviews']))
    movie_data.append(int(request_body['photos']))
    movie_data.append(len(request_body['genres']))
    
    for i in range(0, 27):
        movie_data.append(0)
    
    for i in request_body['genres']:
        movie_data[int(i) + 4] = 1
    
    print(movie_data)
    response = predict(movie_data)
    return web.json_response(response.tolist(), status=200)


def run(classifier):
    global _classifier
    _classifier = classifier
    app = web.Application()
    app.router.add_post("/predict", handle)
    web.run_app(app, port=8000)
