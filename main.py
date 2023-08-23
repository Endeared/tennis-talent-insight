from bs4 import BeautifulSoup as bs
import requests
import json
import csv
from requests_html import HTMLSession
from pprint import pprint

info = [
    {
        "name": "Jimmy Connors",
        "dob": "2-Sep-1952"
    },
    {
        "name": "Bjorn Borg",
        "dob": "6-Jun-1956"
    },
    {
        "name": "John Mcenroe",
        "dob": "16-Feb-1959"
    },
    {
        "name": "Ivan Lendl",
        "dob": "7-Mar-1960"
    },
    {
        "name": "Mats Wilander",
        "dob": "22-Aug-1964"
    },
    {
        "name": "Stefan Edberg",
        "dob": "19-Jan-1966"
    },
    {
        "name": "Boris Becker",
        "dob": "22-Nov-1967"
    },
    {
        "name": "Pete Sampras",
        "dob": "12-Aug-1971"
    },
    {
        "name": "Andre Agassi",
        "dob": "29-Apr-1970"
    },
    {
        "name": "Roger Federer",
        "dob": "8-Aug-1981"
    },
    {
        "name": "Rafael Nadal",
        "dob": "3-Jun-1986"
    },
    {
        "name": "Novak Djokovic",
        "dob": "22-May-1987"
    },
    {
        "name": "Andy Murray",
        "dob": "15-May-1987"
    },
    {
        "name": "Stan Wawrinka",
        "dob": "28-Mar-1985"
    },
    {
        "name": "Carlos Alcaraz",
        "dob": "5-May-2003"
    }
]

grand_slam_names = ["Australian Open", "Roland Garros", "Wimbledon", "US Open"]
player_data = []

for player in info:
    player_object = {
        "name": player['name'],
        "data_wl": [],
        "data_slam": []
    }
    player_data.append(player_object)

years = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

base_url = "https://www.tennisabstract.com/cgi-bin/player.cgi?p="
backup_url = "https://www.tennisabstract.com/cgi-bin/player-classic.cgi?p="
session = HTMLSession()

def age_from_two_years(birth_year, year):
    return str(year - birth_year)

def get_age_at_date(birth_date, date):
    birth_year = int((birth_date.split("-"))[2])
    birth_month = years.index((birth_date.split("-"))[1]) + 1
    birth_day = int((birth_date.split("-"))[0])

    year = None
    month = None
    day = None

    try:
        year = int((date.split("-"))[2])
        month = years.index((date.split("-"))[1]) + 1
        day = int((date.split("-"))[0])
    except:
        year = int((date.split("‑"))[2])
        month = years.index((date.split("‑"))[1]) + 1
        day = int((date.split("‑"))[0])

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

def check_if_slam(tournament):
    if tournament in grand_slam_names:
        return True
    else:
        return False

player_iterator = 0

for player in info:
    player_url = base_url + player['name'].replace(" ", "")
    player_url_backup = backup_url + player['name'].replace(" ", "") + "&f=ACareerqqE0"
    page = session.get(player_url)
    page.html.render(timeout=30)

    year_by_year = []

    tour_seasons = page.html.find('#tour-years')[0].find("tbody")[0].find("tr")
    grand_slams = None
    try:
        grand_slams = page.html.find('#titles-finals')[0].find("tbody")[0].find("tr")
    except:
        page_backup = session.get(player_url_backup)
        page_backup.html.render(timeout=30)
        grand_slams = page_backup.html.find('#matches')[0].find("tbody")[0].find("tr")


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
        tds = slam.find("td")
        date = tds[0].text
        tournament = tds[1].text
        year = None
        try:
            year = date.split("-")[2]
        except:
            year = date.split("‑")[2]
        result = tds[6].text
        last_name = player['name'].split(" ")[1]
        index_of_last_name = result.find(last_name)
        index_of_status = result.find("d.")
        is_slam = check_if_slam(str(tournament))

        if is_slam:
            slam_finals += 1
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
    player_data_wl = player_data[player_iterator]['data_wl']
    length_wl = len(player_data_wl)
    length_slam = len(player_data_slam)
    lowest_age_wl = player_data_wl[0]['age']
    highest_age_wl = player_data_wl[length_wl - 1]['age']
    lowest_age_slam = player_data_slam[0]['age']
    highest_age_slam = player_data_slam[length_slam - 1]['age']
    all_ages = populate_range(int(lowest_age_wl), int(highest_age_wl) + 1)
    player_birth_year = int((player['dob'].split("-"))[2])

    for data_point in player_data[player_iterator]['data_slam']:
        this_age = data_point['age']
        if this_age in all_ages:
            all_ages.remove(this_age)

    pre_slams = []
    post_slams = []
    treated_data_slam = []
    ignore_ages = []
    most_recent_age = None
    most_recent_wins = None
    most_recent_finals = None
    most_recent_year = None

    for data_point in player_data_slam:
        this_age = data_point['age']
        this_year = data_point['year']
        
        if this_age not in ignore_ages:
            if this_age not in all_ages:
                occurrences = [item for item in player_data_slam if item['age'] == this_age]
                my_object = {
                    "age": this_age,
                    "year": int(this_age) + player_birth_year,
                    "wins": occurrences[len(occurrences) - 1]['wins'],
                    "finals": occurrences[len(occurrences) - 1]['finals'],
                }
                most_recent_age = this_age
                most_recent_wins = occurrences[len(occurrences) - 1]['wins']
                most_recent_finals = occurrences[len(occurrences) - 1]['finals']
                most_recent_year = this_year
                treated_data_slam.append(my_object)
            else:
                my_object = {
                    "age": this_age,
                    "year": int(this_age) + player_birth_year,
                    "wins": most_recent_wins,
                    "finals": most_recent_finals,
                }
                treated_data_slam.append(my_object)
        ignore_ages.append(this_age)

    for age in all_ages:
        if int(age) < int(lowest_age_slam):
            my_object = {
                "age": age,
                "year": int(age) + player_birth_year,
                "wins": 0,
                "finals": 0,
            }
            pre_slams.append(my_object) 
        elif int(age) > int(highest_age_slam):
            my_object = {
                "age": age,
                "year": int(age) + player_birth_year,
                "wins": most_recent_wins,
                "finals": most_recent_finals,
            }
            post_slams.append(my_object)
    
    for year_pre in reversed(pre_slams):
        treated_data_slam.insert(0, year_pre)
    for year_post in post_slams:
        treated_data_slam.append(year_post)

    player_data[player_iterator]['data_slam'] = treated_data_slam
    player_iterator += 1

with open('rawData.json', 'w') as outfile:
    json.dump(player_data, outfile, indent=4)