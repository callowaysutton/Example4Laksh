from flask import Blueprint, stream_template

web_logic = Blueprint('web_logic', __name__)

@web_logic.route("/")
def homepage():
    return stream_template("homepage.html")

@web_logic.route("/about")
def about():
    return stream_template("about.html")