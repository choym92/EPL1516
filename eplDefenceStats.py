from urllib.request import urlopen
from bs4 import BeautifulSoup
import os


def make_soup(url):
      thepage = urlopen(url)
      soupdata = BeautifulSoup(thepage, "html.parser")
      return soupdata

playerdatasaved=""
soup=make_soup("http://www.sportsmole.co.uk/football/premier-league/best-defence.html ")
tablestats = soup.find('table',{"class":"leaguetable full"})
for record in tablestats.findAll('tr'):
      playerdata=""
      for data in record.findAll('td'):
            playerdata=playerdata+","+data.text
      playerdatasaved=playerdatasaved+"\n"+playerdata[1:]

file = open(os.path.expanduser(r"~/Desktop/CS327 E/SoccerData/eplDefenceStats.csv"), "wb")
file.write(b"English Premier League Defence Stats")
file.write(bytes(playerdatasaved , encoding="ascii", errors='ignore'))
file.close()
print(playerdatasaved)
