import flask

hello = flask.Flask(__name__)

from MyApp import routes
