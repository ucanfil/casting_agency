import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Movie, Actor, db_create_all


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "casting_test"
        self.database_path = "postgres://{}/{}".format(
            'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.movie = {
            'title': 'The Hook',
            'release_date': '04-23-1991'
        }

        self.actor = {
            'name': 'Jude Law',
            'age': '48',
            'gender': 'M',
        }

        # Authorization headers
        self.JWTCA = {"Authorization": "Bearer {}".format(
            os.environ['JWT_CASTING_ASSISTANT'])}

        self.JWTCD = {"Authorization": "Bearer {}".format(
            os.environ['JWT_CASTING_DIRECTOR'])}

        self.JWTEP = {"Authorization": "Bearer {}".format(
            os.environ['JWT_EXECUTIVE_PRODUCER'])}

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_movies(self):
        res = self.client().get('/movies', headers=self.JWTCA)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_404_get_movies(self):
        res = self.client().get('/movies/starred')

        self.assertEqual(res.status_code, 404)

    def test_get_movie(self):
        res = self.client().get('/movies/1', headers=self.JWTCA)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    def test_404_get_movie(self):
        res = self.client().get('/movie/1000')

        self.assertEqual(res.status_code, 404)

    def test_post_movie(self):
        res = self.client().post('/movies', headers=self.JWTEP,
                                 json=self.movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['insert'])

    def test_422_post_movie(self):
        res = self.client().post('/movies', headers=self.JWTEP)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unproccesable entity')

    def test_patch_movie(self):
        res = self.client().patch('/movies/2', headers=self.JWTEP, json={
                                "title": "Lock",
                                "release_date": "08-08-1933"
                            })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    def test_404_patch_movie(self):
        res = self.client().patch('/movies/2', headers=self.JWTEP)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not found')

    def test_delete_movie(self):
        res = self.client().delete('/movies/3', headers=self.JWTEP)
        data = json.loads(res.data)

        movie = Movie.query.filter(Movie.id == 3).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['delete'], 3)

    def test_404_delete_movie(self):
        res = self.client().delete('/movies/1000', headers=self.JWTEP)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    # Fix below HERE TODO FIXME
    def test_get_actors(self):
        res = self.client().get('/actors', headers=self.JWTCA)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_404_get_actors(self):
        res = self.client().get('/actors/starred')

        self.assertEqual(res.status_code, 404)

    def test_get_actor(self):
        res = self.client().get('/actors/1', headers=self.JWTCA)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

    def test_404_get_actor(self):
        res = self.client().get('/actor/1000')

        self.assertEqual(res.status_code, 404)

    def test_post_actor(self):
        res = self.client().post('/actors', headers=self.JWTEP,
                                 json=self.actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['insert'])

    def test_422_post_actor(self):
        res = self.client().post('/actors', headers=self.JWTEP)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unproccesable entity')

    def test_patch_actor(self):
        res = self.client().patch('/actors/2', headers=self.JWTEP, json={
                                "name": "John Doe",
                                "age": "33",
                                "gender": "M"
                            })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

    def test_404_patch_actor(self):
        res = self.client().patch('/actors/2', headers=self.JWTEP)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not found')

    def test_delete_actor(self):
        res = self.client().delete('/actors/3', headers=self.JWTEP)
        data = json.loads(res.data)

        actor = Actor.query.filter(Actor.id == 3).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['delete'], 3)

    def test_404_delete_actor(self):
        res = self.client().delete('/actors/1000', headers=self.JWTEP)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
