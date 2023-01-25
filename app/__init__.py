from flask import Flask
from .views.home import home
from .views.admin import admin
from .views.search import search


app = Flask(__name__)
app.config.from_object("config")

app.register_blueprint(home)
app.register_blueprint(admin)
app.register_blueprint(search)
