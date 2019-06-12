from urllib.request import urlopen
from bs4 import BeautifulSoup
import os


def make_soup(url):
      thepage = urlopen(url)
      soupdata = BeautifulSoup(thepage, "html.parser")
      return soupdata

playerdatasaved=""
soup=make_soup("http://www.sportsmole.co.uk/football/premier-league/table.html")
tablestats = soup.find('table',{"class":"tablehw leaguetable"})
for record in tablestats.findAll('tr'):
      playerdata=""
      for data in record.findAll('td'):
            playerdata=playerdata+","+data.text
      playerdatasaved=playerdatasaved+"\n"+playerdata[1:]

file = open(os.path.expanduser(r"~/Desktop/soccer_league.csv"), "wb")
file.write(bytes(playerdatasaved , encoding="ascii", errors='ignore'))
file.close()
