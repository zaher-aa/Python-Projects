import requests
import csv
import json
from bs4 import BeautifulSoup

url = 'https://egypt.souq.com/eg-ar/apple/s/?as=1&section=2&page='
# all lists that contains all pages data
titles, prices, imgs, feauters, sim_cards, links, data = [], [], [], [], [], [], {}
# open csv file
# encoding="utf-8-sig" ==> to allow non English letters (Arabic)
csv_file = open("products.csv", "w", encoding="utf-8-sig")
field_names = ["Title", "Price", "Feauters",
               "Sim Card", "More Info", "Product Image"]
writer = csv.DictWriter(csv_file, fieldnames=field_names)
writer.writeheader()
# open json file
json_file = open("products.json", "w", encoding="utf-8-sig")
for page_num in range(1000):
    try:
        # make a request to allow access to the specified URL
        page = requests.get(url + str(page_num + 1))
        soup = BeautifulSoup(page.content, 'lxml')
        # temporary lists contaning current page data
        sub_titles_list = [title.text.strip()
                           for title in soup.find_all('h1', {'class': 'itemTitle'})]
        sub_prices_list = [price.text.strip()
                           for price in soup.find_all('h3', {'class': 'itemPrice'})]
        sub_imgs_list = [div.find('img')['data-src'] for div in soup.find_all(
            'div', {'class': 'column column-block block-list-large single-item'})]
        sub_feauters = [feature.text.strip().replace("\n", " || ")
                        for feature in soup.find_all('ul', {'class': 'selling-points'})]
        sub_sim_cards = [card.text.strip() for card in soup.find_all(
            'a', {'class': 'sk-clr2 changeVariance is-active'})]
        sub_links = [link['href'] for link in soup.find_all(
            'a', {'class': 'view-product-details sPrimaryLink secondary button expand white tiny'})]
        # extending sublists data into permanent lists
        titles.extend(sub_titles_list)
        prices.extend(sub_prices_list)
        imgs.extend(sub_imgs_list)
        feauters.extend(sub_feauters)
        sim_cards.extend(sub_sim_cards)
        links.extend(sub_links)
    except:
        break
    else:
        # print the page number on the termenal
        print(f"-----{page_num + 1}-----")
# writing data to csv file and adding data to the {data} dict for converting it into json file
for title, price, img, feature, card, link, counter in zip(titles, prices, imgs, feauters, sim_cards, links, range(len(titles))):
    writer.writerow({"Title": title, "Price": price, "Feauters": feature,
                     "Sim Card": card, "More Info": link, "Product Image": img})
    data[f"Product {counter + 1}"] = {"Title": title, "Price": price, "Feauters": feature,
                                      "Sim Card": card, "More Info": link, "Product Image": img}
# writing data to json file
# In JSON files [ensure_ascii=False] ==> to allow non English letters (Arabic)
json.dump(data, json_file, ensure_ascii=False)

csv_file.close()  # close csv file
json_file.close()  # close json file
print("Process Done.")
