import os
from flask import Flask, request, abort, jsonify
from models import Actor, Movie, setup_db, db
from flask_cors import CORS
import json
from auth.auth import AuthError, requires_auth

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)
#     app.app_context().push()

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type,Authorization,true'
        )
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET,PATCH,POST,DELETE,OPTIONS'
        )
        return response

    @app.route('/hello')
    def init():
        return 'hello world'

    @app.route('/actors')
    @requires_auth('get:actors')
    def actors(payload):
        actors = Actor.query.all()

        if len(actors) == 0:
            abort(404)

        actors_long = [actor.long() for actor in actors]

        return jsonify({
            'success': True,
            'actors': actors_long
        })

    @app.route('/movies')
    @requires_auth('get:movies')
    def movies():
        movies = Movie.query.all()

        if len(movies) == 0:
            abort(404)

        movies_long = [movie.long() for movie in movies]

        return jsonify({
            'success': True,
            'movies': movies_long
        })

    @app.route('/actors/<int:id>', methods=['DELETE'])
    @requires_auth('delete:actor')
    def delete_actor(id):
        actor = Actor.query.get(id)

        if actor is None:
            abort(404)

        try:
            actor.delete()
            return jsonify({
                 'success': True,
                 'deleted': id
            })

        except:
            abort(422)

    @app.route('/movies/<int:id>', methods=['DELETE'])
    @requires_auth('delete:movie')
    def delete_movie(movie_id):
        movie = Movie.query.get(id)

        if movie is None:
            abort(404)

        try:
            movie.delete()
            return jsonify({
                 'success': True,
                 'deleted': id
            })

        except:
            abort(422)


    @app.route('/actors/create', methods=['POST'])
    @requires_auth('create:actor')
    def create_actor():
        body = request.get_json()
        try:
            actor = Actor(name=body['name'], age=body['age'], gender=body['gender'])
            actor.insert()
            return jsonify({
                        'success': True,
                        'actor': actor.serialize()
            })

        except Exception as e:
            print(e)
            abort(422)


    @app.route('/movies/create', methods=['POST'])
    @requires_auth('create:movie')
    def create_movie():
        body = request.get_json()
        title = body.get('title')
        release_date = body.get('release_date')

        try:
           movie = Movie(title=body['title'], release_date=['release_date'])
           movie.insert()

           return jsonify({
                        'success': True,
                        'movie': movie.serialize()
           })

        except:
            abort(422)


    @app.route('/actors/<int:id>/edit', methods=['PATCH'])
    @requires_auth('edit:actor')
    def edit_actor(id):
        body = request.get_json()
        actor = Actor.query.filter(Actor.id == id).one_or_none()

        if actor is None:
            abort(404)

        try:
            name = body.get('name', None)
            age = body.get('age', None)
            gender = body.get('gender', None)

            if name:
                actor.name = name
            if age:
                actor.age = age
            if gender:
                actor.gender = gender
            actor.update()

            return jsonify({
                            'success': True,
                            'actor': actor.serialize()
                            })
        except:
            abort(422)


    @app.route('/movies/<int:id>/edit', methods=['PATCH'])
    @requires_auth('edit:movie')
    def edit_movie(id):
            body = request.get_json()

            movie = Movie.query.filter(Movie.id == id).one_or_none()

            if movie is None:
                abort(404)

            try:
                title = body.get('title', None)
                release_date = body.get('release_date', None)

                if title:
                    movie.title = title
                if release_date:
                    movie.release_date = age

                movie.update()

                return jsonify({
                                'success': True,
                                'movie': movie.serialize()
                                })
            except:
                abort(422)

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(AuthError)
    def auth_error(auth_error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": auth_error.error['description']
        }), 400

    return app

app = create_app()

if __name__ == '__main__':
    app.run()
