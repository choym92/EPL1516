from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://www.whoscored.com/Regions/252/Tournaments/2/Seasons/5826/Stages/12496/PlayerStatistics/England-Premier-League-2015-2016")
bsObj = BeautifulSoup(html.read(), "html.parser")
print(bsObj)