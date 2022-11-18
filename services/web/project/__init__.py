import os

from flask import (
    Flask,
    jsonify,
    send_from_directory,
    request,
)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)

######## Raus ################################################

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, email):
        self.email = email

class Events(db.Model):
    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)
    identifier = db.Column(db.String(128), unique=True, nullable=False)


    def __init__(self, identifier):
        self.identifier = identifier


######## ################################################################

class Country(db.Model):
    __tablename__ = "country"
    
    country_id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String(450))

    def __init__(self, country_id, country_name):
        self.country_id = country_id
        self.country_name = country_name



class Product(db.Model):
    __tablename__ = "products"
    
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)

    def __init__(self, product_id, name):
        self.product_id = product_id
        self.name = name





class City(db.Model):
    __tablename__ = "city"
    
    city_id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String(450), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('country.country_id'), nullable=False)

    def __init__(self, city_id, city_name, country_id):
        self.city_id = city_id
        self.city_name = city_name
        self.country_id = country_id


class Store(db.Model):
    __tablename__ = "store"
    
    store_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    city_id = db.Column(db.Integer, nullable=False)
    city = db.relationship('City', backref=db.backref('stores', uselist=True, cascade='delete,all'))

    def __init__(self, name, city_id):
        self.name = name
        self.city_id = city_id



class User(db.Model):
    __tablename__ = "user"
    
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)

    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name


class StatusName(db.Model):
    __tablename__ = "status_name"
    
    status_name_id = db.Column(db.Integer, primary_key=True)
    status_name = db.Column(db.String(450), nullable=False)

    def __init__(self, status_name_id, status_name):
        self.status_name_id = status_name_id
        self.status_name = status_name


class Sale(db.Model):
    __tablename__ = "sale"
    
    sale_id = db.Column(db.String(200), primary_key=True)
    amount = db.Column(db.DECIMAL(20,3))
    date_sale = db.Column(db.TIMESTAMP)
    product_id = db.Column(db.INT, db.ForeignKey('product.product_id'), nullable=False)
    user_id = db.Column(db.INT, db.ForeignKey('users.user_id'), nullable=False)
    store_id = db.Column(db.INT, db.ForeignKey('store.store_id'), nullable=False)
    
    def __init__(self, sale_id, amount, date_sale, product_id, user_id, store_id):
        self.sale_id = sale_id
        self.amount = amount
        self.date_sale = date_sale
        self.product_id = product_id
        self.user_id = user_id
        self.store_id = store_id



class OrderStatus(db.Model):
    __tablename__ = "order_status"

    order_status_id = db.Column(db.String(200), primary_key=True)
    update_at = db.Column(db.TIMESTAMP)
    sale_id = db.Column(db.String(200), db.ForeignKey('sale.sale_id'))
    status_name_id = db.Column(db.Integer, db.ForeignKey('status_name.status_name_id'))

    def __init__(self, order_status_id, update_at, sale_id, status_name_id):
        self.order_status_id = order_status_id
        self.update_at = update_at
        self.sale_id = sale_id
        self.status_name_id = status_name_id










@app.route("/")
def hello_world():
    return jsonify(hello="world")


@app.route('/events', methods = ['GET'])
def getevents():
     all_events = []
     events = Events.query.all()
     for event in events:
          results = {
                    "id":event.id,
                    "identifier":event.identifier,
          }
          all_events.append(results)

     return jsonify(all_events)


@app.route("/static/<path:filename>")
def staticfiles(filename):
    return send_from_directory(app.config["STATIC_FOLDER"], filename)


@app.route("/media/<path:filename>")
def mediafiles(filename):
    return send_from_directory(app.config["MEDIA_FOLDER"], filename)


@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["file"]
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["MEDIA_FOLDER"], filename))
    return """
    <!doctype html>
    <title>upload new File</title>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file><input type=submit value=Upload>
    </form>
    """