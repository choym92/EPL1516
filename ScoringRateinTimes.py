from urllib.request import urlopen
from bs4 import BeautifulSoup
import os


def make_soup(url):
      thepage = urlopen(url)
      soupdata = BeautifulSoup(thepage, "html.parser")
      return soupdata

playerdatasaved=""
soup=make_soup("http://www.soccerstats.com/timing.asp?league=england")
tablestats = soup.find('table',{"cellpadding":"2"})
for record in tablestats.findAll('tr'):
      playerdata=""
      for data in record.findAll('td'):
            playerdata=playerdata+","+data.text
      playerdatasaved=playerdatasaved+"\n"+playerdata[1:]


print(playerdatasaved)
