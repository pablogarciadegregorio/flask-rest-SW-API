"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Planets, People, Favorite
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
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



# ---------- ENDPOINTS ------------#

####GET ALL ####

@app.route('/users', methods=['GET'])
def get_all_users():
    users_query = User.query.all()
    results = list(map(lambda item: item.serialize(),users_query))
    print(users_query)
    print(results)

    response_body = {
        "msg": "Hello, this is your GET /user response ",   
        "results": results 
    }

    return jsonify(response_body), 200


@app.route('/planets', methods=['GET'])
def get_all_planets():
    planets_query = Planets.query.all()
    results = list(map(lambda item: item.serialize(),planets_query))
    print(planets_query)
    print(results)

    response_body = {
        "msg": "Hello, this is your GET /Planets response ",   
        "results": results 
    }

    return jsonify(response_body), 200


@app.route('/people', methods=['GET'])
def get_all_people():
    people_query = People.query.all()
    results = list(map(lambda item: item.serialize(),people_query))
    print(people_query)
    print(results)

    response_body = {
        "msg": "Hello, this is your GET /people response ",   
        "results": results 
    }

    return jsonify(response_body), 200


@app.route('/favorite', methods=['GET'])
def get_all_favorite():
    favorite_query = Favorite.query.all()
    results = list(map(lambda item: item.serialize(),favorite_query))
    print(favorite_query)
    print(results)

    response_body = {
        "msg": "Hello, this is your GET /favorite response ",   
        "results": results 
    }

    return jsonify(response_body), 200


#### GET SINGLE ####

@app.route('/users/<int:user_id>', methods=['GET'])
def get_one_user(user_id):
    user_query = User.query.filter_by(id=user_id).first()
    
    print(user_id)
    print(user_query)

    response_body = {
        "msg": "ok ",   
        "results": user_query.serialize() 
    }

    return jsonify(response_body), 200


@app.route('/planets/<int:user_id>', methods=['GET'])
def get_one_planet(user_id):
    planet_query = Planets.query.filter_by(id=user_id).first()
    
    print(user_id)
    print(planet_query)

    response_body = {
        "msg": "ok ",   
        "results": planet_query.serialize() 
    }

    return jsonify(response_body), 200


@app.route('/people/<int:user_id>', methods=['GET'])
def get_one_person(user_id):
    people_query = People.query.filter_by(id=user_id).first()
    
    print(user_id)
    print(people_query)

    response_body = {
        "msg": "ok ",   
        "results": people_query.serialize() 
    }

    return jsonify(response_body), 200


@app.route('/favorite/<int:user_id>', methods=['GET'])
def get_one_favorite(user_id):
    favorite_query = Favorite.query.filter_by(id=user_id).first()
    
    print(user_id)
    print(favorite_query)

    response_body = {
        "msg": "ok ",   
        "results": favorite_query.serialize() 
    }

    return jsonify(response_body), 200



#### POST ####

@app.route('/users', methods=['POST'])
def create_user():

    request_body = request.get_json(force=True)   
    user = User(name=request_body["name"],lastname=request_body["lastname"], email=request_body["email"], password=request_body["password"], suscriptiondate=request_body["suscriptiondate"])
    db.session.add(user)
    db.session.commit()

    response_body = {
        "msg": "user created ",  
        
    }

    return jsonify(response_body), 200


@app.route('/planets', methods=['POST'])
def create_planet():

    request_body = request.get_json(force=True)   
    planet = Planets(name=request_body["name"],population=request_body["population"], size=request_body["size"], gravity=request_body["gravity"], field=request_body["field"])
    db.session.add(planet)
    db.session.commit()

    response_body = {
        "msg": "planet created ",  
        
    }

    return jsonify(response_body), 200


@app.route('/people', methods=['POST'])
def create_person():

    request_body = request.get_json(force=True)   
    person = People(name=request_body["name"],height=request_body["height"], birth=request_body["birth"], gender=request_body["gender"], eyes=request_body["eyes"], hair=request_body["hair"],weight=request_body["weight"])
    db.session.add(person)
    db.session.commit()

    response_body = {
        "msg": "person created ",  
        
    }

    return jsonify(response_body), 200


@app.route('/favorite', methods=['POST'])
def create_favorite():

    request_body = request.get_json(force=True)   
    favorite = Favorite(user_id=request_body["user_id"],fav_planet=request_body["fav_planet"], fav_people=request_body["fav_people"])
    db.session.add(favorite)
    db.session.commit()

    response_body = {
        "msg": "favorite created ",  
        
    }

    return jsonify(response_body), 200


#### DELETE ####

@app.route('/users/<int:user_id>/favoritos/', methods=['DELETE'])
def del_favorite(user_id):

    body = request.get_json(force=True)
    
    if body["characters_id"] is None:
        favorito_query= Favorite.query.filter_by(user_id=user_id).filter_by(planet_id=body["planet_id"]).first()
    
    else:
        favorito_query= Favorite.query.filter_by(user_id=user_id).filter_by(people_id=body["people_id"]).first()
   

    db.session.delete(favorito_query)
    db.session.commit()


    response_body = {
        'msg':'ok',
        "results": 'Favorite deleted'
    }

    return jsonify(response_body), 200


##### PUT  ####

@app.route('/users/<int:user_id>', methods=['PUT', 'GET'])
def get_single_user(user_id):

    body = request.get_json(force=True) #{ 'username': 'new_username'}
    if request.method == 'PUT':
        user1 = User.query.get(user_id)
        user1.email = body["email"]
        db.session.commit()
        return jsonify(user1.serialize()), 200
    if request.method == 'GET':
        user1 = User.query.get(user_id)
        return jsonify(user1.serialize()), 200

    return "Invalid Method", 404


# ------- FIN ENDPOINTS -----------------#




# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
