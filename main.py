from bs4 import BeautifulSoup
import re 
import requests

url = 'https://www.nfl.com/players/chauncey-gardner-johnson-x5009/stats/'

page = requests.get(url).content

soup = BeautifulSoup(page, 'html.parser')
tables = soup.find_all("table")

print(tables)