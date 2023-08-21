from bs4 import BeautifulSoup as bs
import requests
import json
import csv
from requests_html import HTMLSession
from pprint import pprint

info = [
    {
        "name": "Pete Sampras",
        "dob": "12-Aug-1971"
    },
]

player_data = []

for player in info:
    player_object = {
        "name": player['name'],
        "data_wl": [],
        "data_slam": []
    }
    player_data.append(player_object)

pprint(player_data)


years = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

base_url = "https://www.tennisabstract.com/cgi-bin/player.cgi?p=PeteSampras"
session = HTMLSession()

def age_from_two_years(birth_year, year):
    return str(year - birth_year)

def get_age_at_date(birth_date, date):
    birth_year = int((birth_date.split("-"))[2])
    birth_month = years.index((birth_date.split("-"))[1]) + 1
    birth_day = int((birth_date.split("-"))[0])

    year = int((date.split("-"))[2])
    month = years.index((date.split("-"))[1]) + 1
    day = int((date.split("-"))[0])

    age = year - birth_year
    if month < birth_month:
        age -= 1
    elif month == birth_month:
        if day < birth_day:
            age -= 1

    return str(age)

def populate_range(start, end):
    list = []
    for i in range(start, end):
        list.append(str(i))
    return list

player_iterator = 0

for player in info:
    player_url = base_url + player['name'].replace(" ", "")
    page = session.get(base_url)
    page.html.render(timeout=30)

    year_by_year = []

    tour_seasons = page.html.find('#tour-years')[0].find("tbody")[0].find("tr")
    grand_slams = page.html.find('#titles-finals')[0].find("tbody")[0].find("tr")

    slam_wins = 0
    slam_finals = 0

    for season in reversed(tour_seasons):
        tds = season.find("td")
        year = tds[0].text
        win_loss = tds[4].text
        if not year == "Career":
            age = age_from_two_years(int((player['dob'].split("-"))[2]), int(year))
            my_object = {
                "year": year,
                "age": age,
                "winLoss": win_loss
            }
            player_data[player_iterator]['data_wl'].append(my_object)

    for slam in reversed(grand_slams):
        slam_finals += 1
        tds = slam.find("td")
        date = tds[0].text
        year = date.split("-")[2]
        result = tds[6].text
        last_name = player['name'].split(" ")[1]
        index_of_last_name = result.find(last_name)
        index_of_status = result.find("d.")

        if (index_of_last_name < index_of_status):
            slam_wins += 1

        age = get_age_at_date(player['dob'], date)
        my_object = {
            "year": year,
            "age": age,
            "wins": slam_wins,
            "finals": slam_finals,
        }
        player_data[player_iterator]['data_slam'].append(my_object)

    player_data_slam = player_data[player_iterator]['data_slam']
    length_wl = len(player_data_slam)
    lowest_age = player_data_slam[0]['age']
    highest_age = player_data_slam[length_wl - 1]['age']
    all_ages = populate_range(int(lowest_age), int(highest_age) + 1)

    for data_point in player_data[player_iterator]['data_slam']:
        this_age = data_point['age']
        if this_age in all_ages:
            all_ages.remove(this_age)

    print(all_ages)

    treated_data_slam = []
    ignore_ages = []

    for data_point in player_data[player_iterator]['data_slam']:
        this_age = data_point['age']
        
        if not this_age in ignore_ages:
            occurrences = [item for item in player_data_slam if item['age'] == this_age]
            my_object = {
                "age": this_age,
                "wins": occurrences[len(occurrences) - 1]['wins'],
                "finals": occurrences[len(occurrences) - 1]['finals'],
            }
            print(my_object)
            treated_data_slam.append(my_object)


        ignore_ages.append(this_age)

    player_data[player_iterator]['data_slam'] = treated_data_slam


pprint(player_data)