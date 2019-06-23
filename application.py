# application.py
from flask import Flask
import os
import logging

from utilities.house_search import get_listing_data

app = Flask(__name__)

@app.route("/")
def hello():
    listings = get_listing_data()
    return listings[0]


