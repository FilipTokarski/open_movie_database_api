from rest_framework import status
from rest_framework.test import APITestCase

from .models import Comment, Movie
from .utils import get_movie


class TestMovieViewSet(APITestCase):

    def test_getting_movie_from_api(self):
        response = get_movie('titanic')
        self.assertEqual(type(response), dict)

    def test_post_movies(self):
        response = self.client.post('/movies/', {"Title": "Skyfall"})
        self.assertEqual(Movie.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_movies(self):
        Movie.objects.create(**{"Title": "Test title1"})
        Movie.objects.create(**{"Title": "Test title2"})

        response = self.client.get('/movies/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Movie.objects.count(), 2)

        self.assertEqual(Movie.objects.get(id=3).Title, "Test title1")
        self.assertEqual(Movie.objects.get(id=4).Title, "Test title2")


class TestCommentViewset(APITestCase):

    def setUp(self):
        Movie.objects.create(**{"Title": "Awesome test movie"})

    def test_post_comments(self):
        response1 = self.client.post('/comments/', {"movie": 2, "content": "bdb"})
        response2 = self.client.post('/comments/', {"movie": 2, "content": "ok"})
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response1.data['content'], "bdb")
        self.assertEqual(response2.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response2.data['content'], "ok")
        self.assertEqual(Comment.objects.count(), 2)

    def test_get_comments(self):
        Movie.objects.get(id=1).comments.create(**{"content": "super"})
        Movie.objects.get(id=1).comments.create(**{"content": "extra"})
        response = self.client.get('/comments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Comment.objects.count(), 2)
        self.assertEqual(Comment.objects.get(id=1).content, "super")
        self.assertEqual(Comment.objects.get(id=2).content, "extra")


class TestTopViewset(APITestCase):

    def setUp(self):
        Movie.objects.create(**{"Title": "Awesome movie 1"})
        Movie.objects.create(**{"Title": "Awesome movie 2"})
        Movie.objects.create(**{"Title": "Awesome movie 3"})
        Movie.objects.get(id=6).comments.create(**{"content": "super"})
        Movie.objects.get(id=6).comments.create(**{"content": "extra"})
        Movie.objects.get(id=7).comments.create(**{"content": "cool"})
        Movie.objects.get(id=8).comments.create(**{"content": "ok"})

    def test_get_top(self):
        response = self.client.get('/top/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data[0]['total_comments'], 2)
        self.assertEqual(response.data[0]['rank'], 1)

        self.assertEqual(response.data[1]['total_comments'], 1)
        self.assertEqual(response.data[1]['rank'], 2)
         
        self.assertEqual(response.data[2]['total_comments'], 1)
        self.assertEqual(response.data[2]['rank'], 2)