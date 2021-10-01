from bs4 import BeautifulSoup
import re 
import requests
import pandas as pd
import numpy as np
import csv

url = 'https://www.nfl.com/players/chauncey-gardner-johnson-x5009/stats/'

page = requests.get(url).content

soup = BeautifulSoup(page, 'html.parser')
stat_table = soup.find_all("table", {'summary': 'Career Stats'})
headers = soup.find_all('th', {'class': 'nfl-t-stats__col-14'})
header_text = []

for element in headers:
    header_text.append(element.get_text())

refined_headers = []

for n in header_text:
    refined_headers.append(n.strip())

raw_stat_data = soup.find_all('td', {"class" : 'nfl-t-stats__col-14'})
stat_data = []

for data in raw_stat_data:
    stat_data.append(data.get_text())

refined_stat_data = []

for data in stat_data:
    try:
        refined_stat_data.append(int(data.strip()))
    except:
        if data == '':
            refined_stat_data.append(0)
        else:
            refined_stat_data.append(data.strip())

first_3 = refined_stat_data[:16]
second_3 = refined_stat_data[16:32]
last_3 = refined_stat_data[32:]
teams = first_3[0], second_3[0], last_3[0]

complete_stats = {}


for header in refined_headers:
    i = refined_headers.index(header)
    complete_stats[header] = first_3[i], second_3[i], last_3[i]


df = pd.DataFrame(complete_stats)

print(df)


