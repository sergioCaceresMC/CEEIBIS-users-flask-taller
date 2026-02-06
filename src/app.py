from flask import Flask
from flask_cors import CORS
from utils.db import db
import os
from dotenv import load_dotenv

# Variables de entorno
config = load_dotenv("../.env")

# Blueprints
from routes.user import user

# Configuraciones básicas
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
#CORS(app, origins=["http://localhost:5173"])
dir = f"mysql://{os.environ['SQL_USER']}:{os.environ['SQL_PASSWORD']}@{os.environ['SQL_HOST']}/{os.environ['SQL_DATABASE']}"
app.config['SQLALCHEMY_DATABASE_URI'] = dir
#'mysql://root:1234@localhost/pruebadb'

# Base de datos
db.init_app(app)

# Páginas principales
app.register_blueprint(user)
