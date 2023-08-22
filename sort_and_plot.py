import json
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 10))

f = open('rawData.json')
player_data = json.load(f)

def plot_slams_by_year(data):
    iterator = 1
    for player in data:
        x = []
        y = []
        for data_point in player['data_slam']:
            x.append(int(data_point['year']))
            y.append(data_point['wins'])

        if iterator <= 1:
            plt.plot(x, y, '--', label=player['name'])
        else:
            plt.plot(x, y, label=player['name'])
        iterator += 1
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.legend()
    plt.show()

def plot_finals_by_year(data):
    iterator = 1
    for player in data:
        x = []
        y = []
        for data_point in player['data_slam']:
            x.append(int(data_point['year']))
            y.append(data_point['finals'])

        if iterator <= 1:
            plt.plot(x, y, '--', label=player['name'])
        else:
            plt.plot(x, y, label=player['name'])
        iterator += 1
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.legend()
    plt.show()

def plot_slams_by_age(data):
    iterator = 1
    for player in data:
        x = []
        y = []
        for data_point in player['data_slam']:
            x.append(int(data_point['age']))
            y.append(data_point['wins'])

        if iterator <= 1:
            plt.plot(x, y, '--', label=player['name'])
        else:
            plt.plot(x, y, label=player['name'])
        iterator += 1
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.legend()
    plt.show()

def plot_finals_by_age(data):
    iterator = 1
    for player in data:
        x = []
        y = []
        for data_point in player['data_slam']:
            x.append(int(data_point['age']))
            y.append(data_point['finals'])

        if iterator <= 1:
            plt.plot(x, y, '--', label=player['name'])
        else:
            plt.plot(x, y, label=player['name'])
        iterator += 1
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.legend()
    plt.show()

def plot_winloss_by_age(data):
    iterator = 1
    for player in data:
        x = []
        y = []
        for data_point in player['data_wl']:
            x.append(int(data_point['age']))
            ratio = data_point['winLoss'][:-1]
            y.append(float(ratio))

        if iterator <= 1:
            plt.plot(x, y, '--', label=player['name'])
        else:
            plt.plot(x, y, label=player['name'])
        iterator += 1
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.legend()
    plt.show()

def plot_winloss_by_year(data):
    iterator = 1
    for player in data:
        x = []
        y = []
        for data_point in player['data_wl']:
            x.append(int(data_point['year']))
            ratio = data_point['winLoss'][:-1]
            y.append(float(ratio))

        if iterator <= 1:
            plt.plot(x, y, '--', label=player['name'])
        else:
            plt.plot(x, y, label=player['name'])
        iterator += 1
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.legend()
    plt.show()

plot_slams_by_year(player_data)
plot_finals_by_year(player_data)
plot_slams_by_age(player_data)
plot_finals_by_age(player_data)
plot_winloss_by_year(player_data)
plot_winloss_by_age(player_data)



