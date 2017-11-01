""" This main application initialisation """
from flask import Flask

APP = Flask(__name__)

from app import views
