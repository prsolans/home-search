# application.py
from flask import Flask
import os
import logging
import schedule
import time

from utilities.house_search import get_listing_data

app = Flask(__name__)

def job():
    get_listing_data()
    return ('we are working here...')

@app.route("/")
def hello():
    # listings = get_listing_data()
    # return listings[0]
    print('FINALLY!!')
    return ('starting...')

job()
# schedule.every().hour.do(job)
schedule.every().day.at("07:30").do(job)
schedule.every().day.at("14:30").do(job)


if __name__ == '__main__':
    app.run()
