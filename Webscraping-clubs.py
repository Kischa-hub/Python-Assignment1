import requests
from bs4 import BeautifulSoup
from itertools import zip_longest
import csv


urlbase = "https://footballdatabase.com/ranking/world/"
url=""
club_names=[]
club_points_ranks=[]
club_ranks =[]
club_points =[]


for i in range(1, 58):
    url= urlbase + str(i)
    markup = requests.get(url).content
    soap = BeautifulSoup(markup, 'lxml')
    markupClubNames = soap.findAll("td", {"class": "club text-left"})
    markupClubRanks = soap.findAll("td", {"class": "rank"})
    for i in markupClubNames:
        club_names.append(i.findNext("a").text)

    for i in markupClubRanks:
        club_points_ranks.append(i.text)



club_points = club_points_ranks[1::2]
club_ranks = club_points_ranks[::2]



data = [club_ranks,club_names,club_points]
exp = zip_longest(*data)

with open("Clubdata.csv", "w") as f:
    f = csv.writer(f)
    f.writerow(["Club Rank","Club Name","Club Points"])
    f.writerows(exp)


'''
print(len(markupClubNames))
print(club_names)
print(club_points)
print(len(club_points))
'''
