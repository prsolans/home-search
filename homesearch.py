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

def get_listing_data():

    try:
        client = slack.WebClient(token=os.environ['SLACK_BOT_TOKEN'])
        """## Enter the URL we are looking to crawl
        """
        raw_html = simple_get('https://chicago.craigslist.org/search/apa?hasPic=1&postedToday=1&bundleDuplicates=1&search_distance=6&postal=60601&min_price=2750&max_price=5000&min_bedrooms=3&min_bathrooms=2&availabilityMode=0&pets_dog=1&housing_type=4&housing_type=6&housing_type=9&laundry=1&parking=1&parking=2&parking=3&parking=4&sale_date=all+dates')
        html = BeautifulSoup(raw_html, 'html.parser')



        listings = set(html.find('ul', {'class':'rows'}).findAll('li', {'class': 'result-row'}))
        duplicateListings = set(html.find('ul', {'class':'rows'}).findAll('li', {'class': 'duplicate-row'}))
        listings = listings - duplicateListings

        listingsCount = len(listings)

        # print(type(listings))
        # print('Count: ')
        # print(listingsCount)

        listingTitles = []
        listingPrices = []

        for item in listings:
          title = item.find('a', {'class': 'result-title'}).text
          price = item.find('span', {'class':'result-price'}).text
          hood = item.find('span', {'class':'result-hood'}).text
          link = item.find('a', {'class': 'result-title'})['href']
          about = item.find('span', {'class': 'housing'}).text
          about = about.replace(' ', '')
          about = about.replace('-', '')
          
          text = ( 
                title + '\n' +
                link + '\n' +                
                price + ' |' +
                hood + 
                about
                )                

          print(text)

          TEXT_BLOCK = {
            'type': 'section',
            'text': {
              'type': 'mrkdwn',
              'text': text
            }
          }

          craft_message(client, TEXT_BLOCK)

        
        listingDetails = []

        for i in range(0, listingsCount): 
          break
          # print('TITLE: ' + listingTitles[i].text)
          # print('PRICE: ' + listingPrices[i].text)

    except Error as e:
        print(e)

def craft_message(client, TEXT_BLOCK):
    # WELCOME_BLOCK = {
    #   'type': 'section',
    #   'text': {
    #     'type': 'mrkdwn',
    #     'text': '*A new listing has been added*'
    #   }
    # }

    # DIVIDER_BLOCK = {'type': 'divider'}


    text = '['+str(TEXT_BLOCK)+']'

    print(text)


    response = client.chat_postMessage(
            channel='#housing',
            icon_emoji=":house_buildings:",
            blocks= text
            )

# if __name__ == "__main__":
#     text = 'THIS NEW PLACE IS DOPE'
#     craft_message(client, text)

get_listing_data()
 
