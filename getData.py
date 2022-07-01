import requests
import json
import csv

URL = 'http://localhost:8000/realestates'

r = requests.get(url = URL)
data = r.json()

data_file = open("../final2.csv", "w", newline='')
csv_writer = csv.writer(data_file)

count = 0

for elem in data:
    if count == 0:
        header = elem.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(elem.values())

data_file.close()