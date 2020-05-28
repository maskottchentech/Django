import json
import requests

name_list = []
home_list = []
resp = requests.get('https://app.oddsapi.io/api/v1/odds?apikey=50d15b50-960e-11ea-991d-0bda95767014')
data = resp.json()
#print(data[1]['league'])

for i in range(0,5):
    x = data[i]['league']['name']
    y = data[i]['event']['home']
    name_list.append(x)
    home_list.append(y)
    #print(x,end=' ')
    #print(y)
