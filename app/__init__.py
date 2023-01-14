from flask import Flask, url_for


app = Flask(
    __name__, template_folder="../templates", static_folder="../static"
)

from app import views
