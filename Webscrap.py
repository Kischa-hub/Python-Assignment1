#Web-Scrapping
# Liberary requests, Beautifulsoap, csv
# command on Terminal
#pip install requests

import requests
from bs4 import BeautifulSoup
import csv


result = requests.get("https://www.imdb.com/chart/top/?sort=rk,asc&mode=simple&page=1").content
#src = result.content
soap = BeautifulSoup(result, 'lxml')

movies = soap.findAll("td",{"class":"titleColumn"})

movies_name=[]
movies_dates=[]
for i in movies:
    print(i.findNext("a").text, i.findNext("span").text)

for i in movies:
    movies_name.append(i.findNext("a").text)
    movies_dates.append(i.findNext("span").text)

#W = write
#R = read
#a Append

from itertools import zip_longest

data = [movies_name,movies_dates]
exp = zip_longest(*data)

with open("data3.csv", "w") as f:
    f = csv.writer(f)
    f.writerow(["Movie Name","Movie date"])
    f.writerows(exp)

#print(movies)
