from application import db

import datetime
from datetime import date
import time

from flask_wtf import FlaskForm
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from wtforms import StringField, PasswordField, BooleanField, SelectField, IntegerField
from wtforms.validators import InputRequired, Email, Length


class User(UserMixin, db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    user_role = db.Column(db.String(80))
    is_active = db.Column(db.Boolean)

# ##### STEAKHOLDERS
class Provider(db.Model):
    __tablename__ = 'provider'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(90), nullable=False, unique=True)
    NIF = db.Column(db.String(10))
    ref = db.Column(db.Integer, unique=True, nullable=False)
    business_name = db.Column(db.String(90))
    comment = db.Column(db.String(90))
    country = db.Column(db.String(90))
    IBAN = db.Column(db.String(90))
    invoice_address = db.Column(db.String(90))
    city = db.Column(db.String(90))
    cp = db.Column(db.String(90))
    region = db.Column(db.String(90))
    email = db.Column(db.String(90))
    phone = db.Column(db.String(90))
    web = db.Column(db.String(90))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'NIF': self.NIF,
            'ref': self.ref,
            'business_name': self.business_name,
            'comment': self.comment,
            'IBAN': self.IBAN,
            'invoice_address': self.invoice_address,
            'city': self.city,
            'cp': self.cp,
            'region': self.region,
            'email': self.email,
            'phone': self.phone,
            'web': self.web,
            'country': self.country

        }

    def __repr__(self):
        return '<Proveedor %r>' % self.name

class CustomerGroup(db.Model):
    __tablename__ = 'customergroup'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(90), nullable=False, unique=True)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }    

class Customer(db.Model):
    __tablename__ = 'customer'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(90), nullable=False, unique=True)
    NIF = db.Column(db.String(10))
    ref = db.Column(db.Integer, unique=True, nullable=False)
    business_name = db.Column(db.String(90))
    comment = db.Column(db.String(90))
    country = db.Column(db.String(90))
    IBAN = db.Column(db.String(90))
    invoice_address = db.Column(db.String(90))
    city = db.Column(db.String(90))
    cp = db.Column(db.String(90))
    region = db.Column(db.String(90))
    email = db.Column(db.String(90))
    phone = db.Column(db.String(90))
    web = db.Column(db.String(90))
    group_id = db.Column(db.Integer, db.ForeignKey('customergroup.id'))
    group = db.relationship(CustomerGroup)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'NIF': self.NIF,
            'ref': self.ref,
            'business_name': self.business_name,
            'comment': self.comment,
            'IBAN': self.IBAN,
            'invoice_address': self.invoice_address,
            'city': self.city,
            'cp': self.cp,
            'region': self.region,
            'email': self.email,
            'phone': self.phone,
            'web': self.web,
            'country': self.country,
            'group_id': self.group_id

        }

    def __repr__(self):
        return '<Cliente %r>' % self.name
# ##### END OF STEAKHOLDERS

# #### PRODUCTOS
class Category(db.Model):
	__tablename__ = 'category'

	id = db.Column(db.Integer, primary_key=True)
	category = db.Column(db.String(90))
	ref = db.Column(db.String(2), nullable=False, unique=True)

	@property
	def serialize(self):
		return {
			'id': self.id,
			'category': self.category,
			'ref': self.ref
		}
	def __repr__(self):
		return '<Categoria %r>' % self.category

class SubCategory(db.Model):
	__tablename__ = 'subcategory'

	id = db.Column(db.Integer, primary_key=True)
	subcategory = db.Column(db.String(90))

	@property
	def serialize(self):
		return {
			'id': self.id,
			'subcategory':self.subcategory
		}
	def __repr__(self):
		return '<Subcategoria %r>' % self.subcategory

class Format(db.Model):
    __tablename__ = 'format'

    id = db.Column(db.Integer, primary_key=True)
    qty_box = db.Column(db.Integer)
    units = db.Column(db.String(9))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'qty_box':self.qty_box,
            'units': self.units
        }
    def __repr__(self):
        return '<Formato %r>' % self.id

class Origin(db.Model):
    __tablename__ = 'origin'

    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String(90))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'origin':self.origin
        }
    def __repr__(self):
        return '<Origen %r>' % self.origin

class ProductComments(db.Model):
    __tablename__ = 'productcomments'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(90))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'comment':self.comment
        }
    def __repr__(self):
        return '<Comentario %r>' % self.comment

class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(90), nullable=False, unique=True)
    price = db.Column(db.Float(8))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship(Category)
    subcategory_id = db.Column(db.Integer, db.ForeignKey('subcategory.id'))
    subcategory = db.relationship(SubCategory)
    format_id = db.Column(db.Integer, db.ForeignKey('format.id'))
    formating = db.relationship(Format)
    origin_id = db.Column(db.Integer, db.ForeignKey('origin.id'))
    origin = db.relationship(Origin)
    comment_id = db.Column(db.Integer, db.ForeignKey('productcomments.id'))
    comment = db.relationship(ProductComments)
    

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'category_id': self.category_id,
            'subcategory_id': self.subcategory_id,
            'format_id':self.format_id,
            'origin_id':self.origin_id,
            'comment_id':self.comment_id,
            'price':self.price,
        }

    def __repr__(self):
        return '<Producto %r>' % self.name
# ##### END OF PRODUCTS

# ##### OFFERS
class Offer(db.Model):
    __tablename__ = 'offer'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(90), nullable=False, unique=True)
    margin = db.Column(db.Float(8))
    is_base = db.Column(db.Boolean)
    base_id = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    ref = db.Column(db.String(90), nullable=False, unique=True)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'margin': self.margin,
            'is_base': self.is_base,
            'base_id':self.base_id,
            'date': self.date,
            'ref': self.ref
        }

    def __repr__(self):
        return '<Oferta %r>' % self.name

class Offerchild(db.Model):
    __tablename__ = 'offerchild'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(90), nullable=False, unique=True)
    margin = db.Column(db.Float(8))
    base_id = db.Column(db.Integer, db.ForeignKey('offer.id'))
    base = db.relationship(Offer)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    ref = db.Column(db.String(90), nullable=False, unique=True)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'margin': self.margin,
            'base_id':self.base_id,
            'date': self.date,
            'ref': self.ref
        }

    def __repr__(self):
        return '<Oferta %r>' % self.name

class OfferClients(db.Model):
    __tablename__ = 'offerclients'

    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('customergroup.id'))
    group = db.relationship(CustomerGroup)
    offer_id = db.Column(db.Integer, db.ForeignKey('offer.id'))
    offer = db.relationship(Offer)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'group_id': self.group_id,
            'offer_id': self.offer_id,
        }

    def __repr__(self):
        return '<Offercli %r>' % self.id

class OfferProducts(db.Model):
    __tablename__ = 'offerproducts'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    product = db.relationship(Product)
    offerprice = db.Column(db.Float(8))
    offer_id = db.Column(db.Integer, db.ForeignKey('offer.id'))
    offer = db.relationship(Offer)
    comment = db.Column(db.String(90))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'product_id': self.product_id,
            'offerprice': self.offerprice,
            'offer_id': self.offer_id,
            'comment': self.comment,
        }
# ##### END OF OFFERS

# ##### ORDERS
class Order(db.Model):
    __tablename__ = 'order'

    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    customer = db.relationship(Customer)
    offer_id = db.Column(db.Integer, db.ForeignKey('offer.id'))
    offer = db.relationship(Offer)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'client_id': self.client_id,
            'offer_id' : self.offer_id,
            'date' : self.date,
        }
    def __repr__(self):
        return '<Pedido %r>' % self.id

class OrderProducts(db.Model):
    __tablename__ = 'orderproduct'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    order = db.relationship(Order)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    product = db.relationship(Product)
    quantity = db.Column(db.Float(8))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'order_id': self.order_id,
            'product_id': self.product_id,
            'quantity': self.quantity,
        }

    def __repr__(self):
        return '<Precio %r>' % self.product_id

# ##### END OF ORDERS


class Lote(db.Model):
    __tablename__ = 'lote'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    provider_id = db.Column(db.Integer, db.ForeignKey('provider.id'))
    provider = db.relationship(Provider)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'date': self.date,
            'provider_id': self.provider_id

        }

    def __repr__(self):
        return '<Lote %r>' % self.name

class ProdLote(db.Model):
    __tablename__ = 'prodlote'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    product = db.relationship(Product)
    price_entry = db.Column(db.Float(8))
    tax = db.Column(db.Float(8))
    qty_box = db.Column(db.Float(8))
    qty = db.Column(db.Float(8))
    origin = db.Column(db.String(90))
    lote_id = db.Column(db.Integer, db.ForeignKey('lote.id'))
    lote = db.relationship(Lote)
    units = db.Column(db.String(10))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'product_id': self.product_id,
            'price_entry': self.price_entry,
            'tax': self.tax,
            'qty_box': self.qty_box,
            'qty': self.qty,
            'origin': self.origin,
            'lote_id': self.lote_id,
            'lote': self.lote,
            'units': self.units

        }

    def __repr__(self):
        return '<Producto de lote %r>' % self.product_id

class Stock(db.Model):
    __tablename__ = 'stock'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    product = db.relationship(Product)
    stock = db.Column(db.Float(8))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'product_id': self.product_id,
            'stock': self.stock

        }

    def __repr__(self):
        return '<Stock %r>' % self.stock


class StockLote(db.Model):
    __tablename__ = 'stocklote'

    id = db.Column(db.Integer, primary_key=True)
    prodlote_id = db.Column(db.Integer, db.ForeignKey('prodlote.id'))
    prodlote = db.relationship(ProdLote)
    stock = db.Column(db.Float(8))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'prodlote_id': self.prodlote_id,
            'stock': self.stock

        }

    def __repr__(self):
        return '<Stock en lote %r>' % self.stock


class Price(db.Model):
    __tablename__ = 'price'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    product = db.relationship(Product)
    price = db.Column(db.Float(8))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'product_id': self.product_id,
            'price': self.price

        }

    def __repr__(self):
        return '<Precio %r>' % self.price





# FORMS

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(message='Introduce un mail'), Email(message='Introduce un mail'), Length(max=50)])
    password = PasswordField('Password', validators=[InputRequired(message='Introduce una password entre 8 y 80 caracteres'), Length(min=8, max=80, message='Introduce una password entre 8 y 80 caracteres')])
    remember = BooleanField('Recordar')