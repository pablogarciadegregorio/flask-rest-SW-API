from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String

db = SQLAlchemy()

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(80), unique=False, nullable=False)
#     is_active = db.Column(db.Boolean(), unique=False, nullable=False)

#     def __repr__(self):
#          return '<User %r>' % self.username

#     def serialize(self):
#         return {
#             "id": self.id,
#             "email": self.email,
#             # do not serialize the password, its a security breach
#         }
    

class User(db.Model):
  
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(250), nullable=False)
    lastname = db.Column(String(250), nullable=False)
    email = db.Column(String(250), nullable=False)
    password = db.Column(String(250), nullable=False)
    suscriptiondate = db.Column(String(250), nullable=False)
    # favorito_personaje = Column(Integer, ForeignKey('favoritos_personajes.id.personaje'), nullable=False)
    # favorito_vehiculo = Column(Integer, ForeignKey('favoritos_vehiculos.id_vehiculo'), nullable=False)
    # favorito_planeta = Column(Integer, ForeignKey('favoritos_planetas.id_planeta'), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.email,
            "lastname": self.lastname,
            "email": self.email,
            "password": self.password,
            "suscriptiondate": self.suscriptiondate,

            # do not serialize the password, its a security breach
        }
    
class Planets(db.Model):
  
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(250))
    population = db.Column(String(250))
    size = db.Column(String(250), nullable=False)
    gravity = db.Column(String(250), nullable=False)
    field = db.Column(String(250), nullable=False)
    # favoritos_planetas = relationship('FavoritoPlaneta', backref='planeta', lazy=True)

    def __repr__(self):
        return '<Planets %r>' % self.id
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "size": self.size,
            "gravity": self.gravity,
            "field": self.field,

            
        }


class People(db.Model):
  
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(250))
    height = db.Column(String(250))
    birth = db.Column(String(250), nullable=False)
    gender = db.Column(String(250), nullable=False)
    eyes = db.Column(String(250), nullable=False)
    hair = db.Column(String(250), nullable=False)
    weight = db.Column(String(250), nullable=False)
    # favoritos_personajes = relationship('FavoritoPersonaje', backref='personaje', lazy=True)
    

    def __repr__(self):
        return '<People %r>' % self.id
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "birth": self.birth,
            "gender": self.gender,
            "eyes": self.eyes,
            "hair": self.hair,
            "weight": self.weight,

            
        }
    
class Favorite(db.Model):
  
    id = db.Column(Integer, primary_key=True)
    user_id = db.Column(String(250))
    fav_planet = db.Column(String(250))
    fav_people = db.Column(String(250), nullable=False)
    
   
    

    def __repr__(self):
        return '<Favorite %r>' % self.id
    
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "fav_planet": self.fav_planet,
            "fav_people": self.fav_people,
                       
        }