import json
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 10))

f = open('rawData.json')
player_data = json.load(f)

iterator = 1

for player in player_data:
    x = []
    y = []

    for data_point in player['data_slam']:
        x.append(int(data_point['year']))
        y.append(data_point['wins'])
    
    if iterator <= 10:
        plt.plot(x, y, '--', label=player['name'])
    else:
        plt.plot(x, y, label=player['name'])
    
    iterator += 1

plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
plt.legend()
plt.show()


