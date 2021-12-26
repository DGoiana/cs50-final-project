import requests
import json
import sys
import csv

id = str(48751)
info = "https://www.balldontlie.io/api/v1/stats?game_ids[]=" + id + "&per_page=30"
response = requests.get(url = info).json()
data = []
data.append(response)
for i in range(response['meta']['total_count']):
    print(data[0]['data'][i]['player']['first_name'], data[0]['data'][i]['pts'])