import requests
import csv
import json
from bs4 import BeautifulSoup

# connect to the URL
url = 'https://www.amazon.com/s?k=phone&qid=1611510681&ref=sr_pg_1'
page = requests.get(url)
soup = BeautifulSoup(page.content, "lxml")

# fetching the data from the website
prices_sub_list = [price.text.strip() for price in soup.find_all('a', {'class': 'a-link-normal a-text-normall'})]
print(prices_sub_list)
