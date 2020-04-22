import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, db_create_all, Movie, Actor


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)
    db_create_all()

    # Movie Endpoints #
    @app.route('/movies', methods=['GET'])
    def get_movies():
        movies = Movie.query.order_by(Movie.id).all()

        formatted_movies = [movie.format() for movie in movies]

        return jsonify({
            'success': True,
            'movies': formatted_movies,
        }), 200

    @app.route('/movies/<int:movie_id>', methods=['GET'])
    def get_movie(movie_id):
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()

        try:
            if movie is None:
                abort(404)
            else:
                return jsonify({
                    'success': True,
                    'movie': movie.format()
                }), 200

        except BaseException:
            abort(422)

    @app.route('/movies', methods=['POST'])
    def new_movie():
        body = request.get_json()

        try:
            title = body.get('title', None)
            release_date = body.get('release_date', None)

            movie = Movie(
                title=title,
                release_date=release_date,
            )
            movie.insert()

            return jsonify({
                'success': True,
                'insert': {
                    'title': title,
                    'release_date': release_date,
                }
            }), 200

        except BaseException:
            abort(422)

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    def update_movie(movie_id):
        if movie_id is None:
            abort(404)

        body = request.get_json()

        try:
            movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
            movie.title = body.get('title', None)
            movie.release_date = body.get('release_date', None)
            movie.update()

            return jsonify({
                "success": True,
                "movie": movie.format()
            }), 200

        except BaseException:
            abort(404)

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    def delete_movie(movie_id):
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()

        try:
            if movie is None:
                abort(404)
            else:
                movie.delete()

                return jsonify({
                    'success': True,
                    'delete': movie_id,
                }), 200

        except BaseException:
            abort(422)

    # Actor Endpoints #
    @app.route('/actors', methods=['GET'])
    def get_actors():
        actors = Actor.query.order_by(Actor.id).all()

        formatted_actors = [actor.format() for actor in actors]

        return jsonify({
            'success': True,
            'actors': formatted_actors,
        }), 200

    @app.route('/actors/<int:actor_id>', methods=['GET'])
    def get_actor(actor_id):
        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()

        try:
            if actor is None:
                abort(404)
            else:
                return jsonify({
                    'success': True,
                    'actor': actor.format()
                }), 200

        except BaseException:
            abort(422)

    @app.route('/actors', methods=['POST'])
    def new_actor():
        body = request.get_json()

        try:
            name = body.get('name', None)
            age = body.get('age', None)
            gender = body.get('gender', None)

            actor = Actor(
                name=name,
                age=age,
                gender=gender,
            )
            actor.insert()

            return jsonify({
                'success': True,
                'insert': {
                    'name': name,
                    'age': age,
                    'gender': gender,
                }
            }), 200

        except BaseException:
            abort(422)

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    def update_actor(actor_id):
        if actor_id is None:
            abort(404)

        body = request.get_json()

        try:
            actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
            actor.name = body.get('name', None)
            actor.age = body.get('age', None)
            actor.gender = body.get('gender', None)
            actor.update()

            return jsonify({
                "success": True,
                "actor": actor.format()
            }), 200

        except BaseException:
            abort(404)

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    def delete_actor(actor_id):
        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()

        try:
            if actor is None:
                abort(404)
            else:
                actor.delete()

                return jsonify({
                    'success': True,
                    'delete': actor_id,
                }), 200

        except BaseException:
            abort(422)

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Not found',
        }), 404

    @app.errorhandler(422)
    def unproccesable(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'Unproccesable entity',
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'Bad request',
        }), 400

    @app.errorhandler(405)
    def not_allowed(error):
        return jsonify({
            'success': False,
            'error': 405,
            'message': 'Method not allowed',
        }), 405

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': 'Internal server error',
        }), 500

    return app  # TODO Careful !!


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
