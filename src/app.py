"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from admin import setup_admin
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from flask import Flask, request, jsonify, url_for
from models import db, User, Character, Planet, Favorite
from flask_migrate import Migrate
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET', "POST"])
def handle_user():
    if request.method == 'GET':
        users = User.query.all()
        users = list(map(lambda user: user.to_dict(), users))

        return jsonify({
            "data": users
        }), 200
    elif request.method == 'POST':
        print("Prueba2")
        user = User()
        #data = request.json.get()
        user.name = request.json.get("name")
        user.username = request.json.get("username")
        user.password = request.json.get("password")

        db.session.add(user)
        db.session.commit()

        return jsonify({
            "msg": "user created"
        }), 200

@app.route("/user/<int:id>", methods=["PUT", "DELETE"])
def update_user(id):
    if request.method == 'PUT':
        user = User.query.get(id)
        if user is not None:
            data = request.get_json()
            user.name = data["name"]
            user.username = data["username"]
            db.session.commit()
            return jsonify({
                "msg":"user updated"
            }),200
        else:
            return jsonify({
                "msg": "user not found"
            }), 404
    elif request.method == 'DELETE':
        user = User.query.get(id)
        if user is not None:
            db.session.delete(user)
            db.session.commit()

            return jsonify({
                "msg":"user deleted"
            }),202
        else:
            return jsonify({
                "msg":"user not found"
            }), 404

@app.route('/character', methods=['GET', "POST"])
def handle_character():
    if request.method == 'GET':
        characters = Character.query.all()
        characters = list(map(lambda character: character.to_dict(), characters))

        return jsonify({
            "data": characters
        }), 200
    elif request.method == 'POST':
        character = Character()
        data = request.get_json()
        character.name = data["name"]

        db.session.add(character)
        db.session.commit()

        return jsonify({
            "msg": "character created"
        }), 200

@app.route("/character/<int:id>", methods=["PUT", "DELETE"])
def update_character(id):
    if request.method == 'PUT':
        character = Character.query.get(id)
        if character is not None:
            data = request.get_json()
            character.name = data["name"]
            db.session.commit()
            return jsonify({
                "msg":"character updated"
            }),200
        else:
            return jsonify({
                "msg": "character not found"
            }), 404
    elif request.method == 'DELETE':
        character = Character.query.get(id)
        if character is not None:
            db.session.delete(character)
            db.session.commit()

            return jsonify({
                "msg":"character deleted"
            }),202
        else:
            return jsonify({
                "msg":"character not found"
            }), 404

@app.route('/planet', methods=['GET', "POST"])
def handle_planet():
    if request.method == 'GET':
        planets = Planet.query.all()
        planets = list(map(lambda planet: planet.to_dict(), planets))

        return jsonify({
            "data": planets
        }), 200
    elif request.method == 'POST':
        planet = Planet()
        data = request.get_json()
        planet.name = data["name"]

        db.session.add(planet)
        db.session.commit()

        return jsonify({
            "msg": "planet created"
        }), 200

@app.route("/planet/<int:id>", methods=["PUT", "DELETE"])
def update_planet(id):
    if request.method == 'PUT':
        planet = Planet.query.get(id)
        if planet is not None:
            data = request.get_json()
            planet.name = data["name"]
            db.session.commit()
            return jsonify({
                "msg":"planet updated"
            }),200
        else:
            return jsonify({
                "msg": "planet not found"
            }), 404
    elif request.method == 'DELETE':
        planet = Planet.query.get(id)
        if planet is not None:
            db.session.delete(planet)
            db.session.commit()

            return jsonify({
                "msg":"planet deleted"
            }),202
        else:
            return jsonify({
                "msg":"planet not found"
            }), 404

@app.route('/user/<int:id>/favorite', methods=['GET'])
def handle_favorite():
    favorites = Favorite.query.all()
    favorites = list(map(lambda favorite: favorite.to_dict(), favorites))

    return jsonify({
        "data": favorites
    }), 200
    
@app.route('/user/<int:id>/favorite', methods=["POST"])
def handle_favorite():
    favorite = Favorite()
    data = request.get_json()
    if 
    favorite.user_id = data["name"]

    db.session.add(favorite)
    db.session.commit()

    return jsonify({
        "msg": "favorite created"
    }), 200


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
# this only runs if `$ python src/app.py` is executed
