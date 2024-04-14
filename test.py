import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Actor, Movie

from settings import TEST_DB_NAME, TEST_DB_USER, TEST_DB_PASSWORD

class AgencyTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.assistant_jwt = os.environ.get('ASSISTANT')
        self.director_jwt = os.environ.get('DIRECTOR')
        self.producer_jwt = os.environ.get('PRODUCER')


    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_retrieve_actors_success(self):
        res = self.client().get('/actors', headers={
        'Authorization': "Bearer {}".format(self.assistant_jwt)})
        data = json(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_400_retrieve_actors_unauthorised(self):
          res = self.client().get('/actors')
          data = json(res.data)

          self.assertEqual(res.status_code, 400)
          self.assertEqual(data['success'], False)

    def test_retrieve_movies_success(self):
        res = self.client().get('/movies', headers={
        'Authorization': "Bearer {}".format(self.assistant_jwt)})
        data = json(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_401_retrieve_movies_unauthorised(self):
        res = self.client().post('/movies')
        data = json(res.data)

        self.assertEqual(res.status_code, 400)

    def test_create_new_actor(self):
        actor = {
        "name": "Joe Bloggs",
        "age": 21,
        "gender": "male"
        }

        res = self.client().post('/actors/create', headers={
        'Authorization': "Bearer {}".format(self.director_jwt)}, json=actor, 'Content-Type': 'application/json')
        data = json(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_422_create_new_actor(self):
         actor = {"age": 21}

         res = self.client().post('/actors/create', headers={
         'Authorization': "Bearer {}".format(self.director_jwt)}, json=actor, 'Content-Type': 'application/json')
         data = json(res.data)

         self.assertEqual(res.status_code, 422)
         self.assertEqual(data['success'], False)

    def test_401_create_new_actor_unauthorised(self):
        actor = {
        "name": "Joe Bloggs",
        "age": 21,
        "gender": "male"
        }

        res = self.client().post('/actors/create', headers={
                 'Authorization': "Bearer {}".format(self.assistant_jwt)}, json=actor, 'Content-Type': 'application/json')
                 data = json(res.data)
        data = json(res.data)

        self.assertEqual(res.status_code, 401)

    def test_create_new_movie(self):
        movie = {
            "title" = "101 Dalmations",
            "release_date" = "1994"
        }

         res = self.client().post('/movies/create', headers={
         'Authorization': "Bearer {}".format(self.producer_jwt)}, json=movie, 'Content-Type': 'application/json')
         data = json(res.data)

         self.assertEqual(res.status_code, 200)
         self.assertEqual(data['success'], True)

    def test_422_create_new_movie(self):
         actor = {"title": "101 Dalmations"}

         res = self.client().post('/movies/create', headers={
         'Authorization': "Bearer {}".format(self.producer_jwt)}, json=movie, 'Content-Type': 'application/json')
         data = json(res.data)

         self.assertEqual(res.status_code, 422)
         self.assertEqual(data['success'], False)

    def test_401_create_new_movie_unauthorised(self):
         movie = {
            "title" = "101 Dalmations",
            "release_date" = "1994"
         }

        res = self.client().post('/actors/create', headers={
        'Authorization': "Bearer {}".format(self.assistant_jwt)}, json=movie, 'Content-Type': 'application/json')
        data = json(res.data)

        self.assertEqual(res.status_code, 401)

    def test_delete_actor(self):
        actor = Actor(name="Morgan Freeman", age="50", gender="male")
        actor.insert()

        res = self.client().delete('/actors/{actor.id}', headers={
        'Authorization': "Bearer {}".format(self.director_jwt)})
        data = json(res.data)

        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], actor.id)

    def test_404_delete_actor_which_does_not_exist(self):
        res = self.client().delete('/actors/1000', headers={
        'Authorization': "Bearer {}".format(self.director_jwt)})
        data = json(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "resource not found")

    def test_401_delete_actor_unauthorised(self):
        actor = Actor(name="Morgan Freeman", age="50", gender="male")
        actor.insert()

        res = self.client().delete('/actors/{actor.id}', headers={
        'Authorization': "Bearer {}".format(self.assistant_jwt)})
        data = json(res.data)

        self.assertEqual(res.status_code, 401)

    def test_delete_movie(self):
        movie = Movie(title="Free Willy", release_date="1994")
        movie.insert()

        res = self.client().delete('/movies/{movie.id}', headers={
        'Authorization': "Bearer {}".format(self.producer_jwt)})
        data = json(res.data)

        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], movie.id)

    def test_404_delete_movie_which_does_not_exist(self):
        res = self.client().delete('/movies/1000', headers={
        'Authorization': "Bearer {}".format(self.producer_jwt)})
        data = json(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "resource not found")

    def test_401_delete_movie_unauthorised(self):
        movie = Movie(title="Free Willy", release_date="1994")
        movie.insert()

        res = self.client().delete('/movies/{movie.id}', headers={
        'Authorization': "Bearer {}".format(self.assistant_jwt)})
        data = json(res.data)

        self.assertEqual(res.status_code, 401)


    def test_edit_actor(self):
         actor = {"name" = "Meryl Streep"}
         res = self.client().patch('/actors/1/edit', headers={
         'Authorization': "Bearer {}".format(self.director_jwt)}, json=actor, 'Content-Type': 'application/json')
         data = json(res.data)

         self.assertEqual(res.status_code, 200)
         self.assertEqual(data['success'], True)


    def test_404_edit_actor_which_does_not_exist(self):
        actor = {"name" = "Meryl Streep"}
        res = self.client().patch('/actors/1000/edit', headers={
        'Authorization': "Bearer {}".format(self.director_jwt)}, json=actor, 'Content-Type': 'application/json')
        data = json(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "resource not found")

    def test_edit_movie(self):
        movie = {"title" = "Peter Pan"}
        res = self.client().patch('/movies/1/edit', headers={
        'Authorization': "Bearer {}".format(self.director_jwt)}, json=movie, 'Content-Type': 'application/json')
        data = json(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    def test_404_edit_movie_which_does_not_exist(self):
        movie = {"title" = "Peter Pan"}
        res = self.client().patch('/movies/1000/edit', headers={
        'Authorization': "Bearer {}".format(self.director_jwt)}, json=movie, 'Content-Type': 'application/json')
        data = json(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "resource not found")


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
