from urllib.request import urlopen
from bs4 import BeautifulSoup
import http.client
import json

connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': 'eb3e492624d444f49e859ba3afa146bf', 'X-Response-Control': 'full' }
connection.request('GET', '/v1/soccerseasons/398/teams', None, headers )
response = json.loads(connection.getresponse().read().decode())
#EPL Teams
for item in response['teams']:
      print (item['name'])
      print(item['squadMarketValue'])
      print(item['crestUrl'])
      print('\n')


