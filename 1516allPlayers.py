from urllib.request import urlopen
from bs4 import BeautifulSoup
import os


def make_soup(url):
      thepage = urlopen(url)
      soupdata = BeautifulSoup(thepage, "html.parser")
      return soupdata

playerdatasaved=""
soup=make_soup("https://fantasyfootball.telegraph.co.uk/premierleague/players/")
tablestats = soup.find('div',{"class":"table-container"})
for record in tablestats.findAll('tr'):
      playerdata=""
      for data in record.findAll('td'):
            playerdata=playerdata+","+data.text
      if len(playerdata)!=0:
            playerdatasaved=playerdatasaved+"\n"+playerdata[1:]

file = open(os.path.expanduser(r"~/Desktop/CS327 E/SoccerData/1516allPlayers.csv"), "wb")
header = "Player,FNameInit,Team,Value,Start,Sub,Goals,Penalty Missed,Key Contributions,Clean Sheet Full, Clean Sheet Part,Goal Conceded, Penalty Save,Red Card,Yellow Card,Own Goal, Points Per Value,Total Points" 
file.write(bytes(header, encoding="ascii", errors='ignore'))
file.write(bytes(playerdatasaved , encoding="ascii", errors='ignore'))
file.close()
print(playerdatasaved)
