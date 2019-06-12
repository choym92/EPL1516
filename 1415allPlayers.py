from urllib.request import urlopen
from bs4 import BeautifulSoup
import os


def make_soup(url):
      thepage = urlopen(url)
      soupdata = BeautifulSoup(thepage, "html.parser")
      return soupdata

playerdatasaved=""
soup=make_soup("https://fantasyfootballfirst.co.uk/player-performance-1/players/ ")
tablestats = soup.find('table',{"class":"tablepress tablepress-id-2 dataTable"})
for record in tablestats.findAll('tr'):
      playerdata=""
      for data in record.findAll('td'):
            playerdata=playerdata+","+data.text
      if len(playerdata)!=0:
            playerdatasaved=playerdatasaved+"\n"+playerdata[1:]

file = open(os.path.expanduser(r"~/Desktop/CS327 E/SoccerData/1415allPlayers.csv"), "wb")
header = ",Name, Team, Position, Difficulty, Cost, GW Pts, Tot Pts, Min, GW games, Tot Games, PPG, PPM, PPMPG, Pts L2W, Pts L4W, Games L4W, PPG L4W, PPM L4W, PPMPG L4W" 
file.write(bytes(header, encoding="ascii", errors='ignore'))
file.write(bytes(playerdatasaved , encoding="ascii", errors='ignore'))
file.close()
print(playerdatasaved)
