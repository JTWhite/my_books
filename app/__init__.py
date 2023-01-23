from flask import Flask, Blueprint
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from .views.home import home
from .views.admin import admin
from .views.search import search

from .models import GetBook


app = Flask(__name__)
app.config.from_object("config")

# api_bp = Blueprint("api", __name__)
api = Api(app)

# db = SQLAlchemy(app)

app.register_blueprint(home)
app.register_blueprint(admin)
app.register_blueprint(search)


api.add_resource(GetBook, "/book/<string:title>")
