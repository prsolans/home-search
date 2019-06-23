# __init__.py
from flask import Flask
import os
import logging
import sqlite3
import slack
import ssl as ssl_lib
import certifi

from sqlite3 import Error
from bs4 import BeautifulSoup
from utilities.utility_scrape import simple_get
from utilities.house_listing import HouseListing
from utilities.house_search import get_listing_data

app = Flask(__name__)

@app.route("/")
def hello():
    listings = get_listing_data()
    return listings


