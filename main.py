from bs4 import BeautifulSoup as bs
import requests
import json
import csv
from requests_html import HTMLSession
from pprint import pprint

slam_info = [
    {
        "name": "Australian Open",
        "date": "2/2"
    },
    {
        "name": "French Open",
        "datee": "5/5"
    },
    {
        "name": "Wimbledon",
        "date": "7/7"
    },
    {
        "name": "US Open",
        "date": "9/9"
    }
]

info = [
    {
        "name": "Pete Sampras",
        "dob": "8/12/1971"
    }
]

base_url = "https://www.tennisabstract.com/cgi-bin/player.cgi?p="
session = HTMLSession()

for player in info:
    player_url = base_url + player['name'].replace(" ", "")
    page = session.get(player_url)
    page.html.render()

    test = page.html.find('#tour-years')
    print(page.html)
    # tour_seasons = soup.find('table', id="tour-years").find('tbody').find_all('tr')

    # for season in tour_seasons:
    #     print(season)
    #     this_year = season.find('td').find('b').find('a').text
    #     print(this_year)