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



@app.route('/sales1', methods = ['GET'])
def table():
    sale = Sale.query.all()
    return jsonify([e.serialize() for e in sale])


@app.route('/sales2', methods = ['GET'])
def getsales():
    all_sales = []
    sales = Sale.query.all()
    for sale in sales:
        result = {
            'sale_id': sale.sale_id,
            'amount': sale.amount,
            'date_sale': sale.date_sale,
            'product_id': sale.product_id,
            'user_id': sale.user_id,
            'store_id': sale.store_id
        }
        all_sales.append(result)
    return jsonify(all_sales)




