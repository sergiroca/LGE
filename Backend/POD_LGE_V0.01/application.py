import os
import flask
import zipfile
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, make_response, send_from_directory
from application import db, application

import sys
sys.path.insert(0, 'app_basculas/')
from app_basculas import app_basculas
sys.path.insert(0, 'app_pedidos_fresco/')
from app_pedidos_fresco import app_pedidos_fresco 

from werkzeug.utils import secure_filename

from sqlalchemy import func

# PDF
import pdfkit

# DATES
import datetime
from datetime import date

# LOGIN IMPORT AND SET UP

from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

from functools import wraps
# Admin
from flask_admin import Admin, BaseView, expose
# from flask_admin.contrib.sqla import ModelView

# Email

from flask import Flask, request, url_for
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired

# CORS to be able to comunicate to port 8080
from flask_cors import CORS

CORS(application)

admin = Admin(application)

login_manager = LoginManager()
login_manager.init_app(application)
login_manager.login_view = 'login'

# test
# SQLALCHEMY_TRACK_MODIFICATIONS = True

# Being able to store files
UPLOAD_FOLDER = os.path.join(application.root_path, '../Documents')
UPLOAD_FOLDER_ORDERS = os.path.join(application.root_path, '../Documents/Orders')
UPLOAD_FOLDER_BALANZAS = os.path.join(application.root_path, '../Documents/Datos_para_balanza')
UPLOAD_FOLDER_PEDIDOS_FRESCO = os.path.join(application.root_path, '../Documents/Pedidos_fresco')
ALLOWED_EXTENSIONS = set(['csv' , 'xlsx'])

# Elastic Beanstalk initalization
# application = Flask(__name__)
application.debug = True

# Must be secret
application.secret_key = 'keyman'

# Set Upload folder
application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER_BALANZAS


#allowed files to upload
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# routes

@application.route('/', methods=['GET'])
def home():
    return 'Hello world'

    
# API Balanzas uploads
@application.route("/uploadbalanza/", methods=['POST'])
def uploadBalanza():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        file = request.files['file']
        print file.filename
        if file and allowed_file(file.filename) and file.filename == 'Datos_para_balanza.csv':
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER_BALANZAS, filename))
            filepath = os.path.join(UPLOAD_FOLDER_BALANZAS, filename)
            app_basculas(filepath)
            # parseCSV.parsecsv(filename)

            response_object['message'] = 'Order processed!'
            return jsonify(response_object)
        response_object['message'] = 'Order not processed properly!'
    return jsonify(response_object)

# API Balanzas downloads
@application.route("/downloadbalanza/", methods=['POST'])
def downloadBalanza():

    zip_path = os.path.join(UPLOAD_FOLDER_BALANZAS, '../Salida.zip')
    if os.path.exists(zip_path):
        os.remove(zip_path)
        
    zipf = zipfile.ZipFile(zip_path,'w', zipfile.ZIP_DEFLATED)
    for root,dirs, files in os.walk(UPLOAD_FOLDER_BALANZAS):
        for file in files:
            zipf.write(os.path.relpath(os.path.join(root, file)))
            os.remove(os.path.join(root,file))
            # os.path.relpath(os.path.join(root, file), os.path.join(path, '..'))
    zipf.close()

    return send_from_directory(UPLOAD_FOLDER, 'Salida.zip')

# API Pedidos Fresco uploads
@application.route("/upload_pedidos_fresco/", methods=['POST'])
def uploadPedidosFresco():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        file = request.files['file']
        #type_pedido = request.files['type']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER_PEDIDOS_FRESCO, filename))
            filepath = os.path.join(UPLOAD_FOLDER_PEDIDOS_FRESCO, filename)
            # app_basculas(filepath)

            response_object['message'] = 'Order processed!'
            return jsonify(response_object)
        response_object['message'] = 'Order not processed properly!'
    return jsonify(response_object)

# API Pedidos Fresco upload_type_fresco
@application.route("/upload_type_fresco/", methods=['GET','POST'])
def uploadTypeFresco():
    # mirar type
    # mirar si los 3/4 archivos estan
    # ejecutar app_pedidos_fresco
    data = request.get_json()
    typePedido = data.get('type') 
    path = UPLOAD_FOLDER_PEDIDOS_FRESCO
    datos_para_balanza = path + '/Datos_para_balanza.csv'
    sales_online = path + '/Productos_por_proveedor_online.csv'
    sales_physical = path + '/Productos_por_proveedor_tienda.csv'
    fresco_1 = path + '/FRESCO_1.xlsx'
    fresco_2 = path + '/FRESCO_2.xlsx'
    zipToDelete = UPLOAD_FOLDER + '/Pedidos_fresco.zip'
    print 'UPLOAD OK'
    print type(typePedido)
    print zipToDelete

    if os.path.exists(zipToDelete):
        os.remove(zipToDelete)

    if typePedido == '1':
        print 'Viernes OK'
        print datos_para_balanza
        print os.path.exists(datos_para_balanza)
        print sales_online
        print os.path.exists(sales_online)
        print sales_physical
        print os.path.exists(sales_physical)
        if os.path.exists(datos_para_balanza) and os.path.exists(sales_online) and os.path.exists(sales_physical):
            print 'Files OK'
            lunes = False;
            app_pedidos_fresco(lunes, path)
            zip_path = os.path.join(UPLOAD_FOLDER_PEDIDOS_FRESCO, '../Pedidos_fresco.zip')
            zipf = zipfile.ZipFile(zip_path,'w', zipfile.ZIP_DEFLATED)
            for root,dirs, files in os.walk(UPLOAD_FOLDER_PEDIDOS_FRESCO):
                for file in files:
                    if 'FRESCO' in file:
                        zipf.write(os.path.relpath(os.path.join(root, file)))
                    os.remove(os.path.join(root,file))
            zipf.close()
        
    if typePedido == '2':
        if os.path.exists(datos_para_balanza) and os.path.exists(sales_online) and os.path.exists(fresco_1) and os.path.exists(fresco_2):
            lunes = True;
            app_pedidos_fresco(lunes, path)
            zip_path = os.path.join(UPLOAD_FOLDER_PEDIDOS_FRESCO, '../Pedidos_fresco.zip')
            zipf = zipfile.ZipFile(zip_path,'w', zipfile.ZIP_DEFLATED)
            for root,dirs, files in os.walk(UPLOAD_FOLDER_PEDIDOS_FRESCO):
                for file in files:
                    if 'FRESCO' in file:
                        zipf.write(os.path.relpath(os.path.join(root, file)))
                    os.remove(os.path.join(root,file))
            zipf.close()
    
    return send_from_directory(UPLOAD_FOLDER, 'Pedidos_fresco.zip')

# API Pedidos Fresco download
@application.route("/download_pedidos_fresco/")
def downloadPedidosFresco():
    print 'DOWNLOAD OK'
    return send_from_directory(UPLOAD_FOLDER, 'Pedidos_fresco.zip')


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000)