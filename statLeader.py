from urllib.request import urlopen
from bs4 import BeautifulSoup
import os


def make_soup(url):
      thepage = urlopen(url)
      soupdata = BeautifulSoup(thepage, "html.parser")
      return soupdata

playerdatasaved=""
soup=make_soup("http://scores.nbcsports.msnbc.com/epl/player_leaders.asp?category=202")
tablestats = soup.find('table',{"class":"shsTable shsBorderTable"})   
for record in tablestats.findAll('tr'):
      playerdata=""
      for data in record.findAll('td'):
            playerdata=playerdata+","+data.text
      playerdatasaved=playerdatasaved+"\n"+playerdata[1:]

file = open(os.path.expanduser(r"~/Desktop/CS327 E/SoccerData/Statistical Leaders.csv"), "wb")
file.write(b" statLeaders")
file.write(bytes(playerdatasaved , encoding="ascii", errors='ignore'))
file.close()
print(playerdatasaved)
