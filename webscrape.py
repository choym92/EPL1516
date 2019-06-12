from urllib.request import urlopen
from bs4 import BeautifulSoup
import http.client
import json
import pymysql
import unicodedata

def addvalues(name, team, position, number, dateofbirth, nationality, salary):

 conn = pymysql.connect(host = '127.0.0.1', user = 'root',passwd = 'Yusarang10101993!', db = 'soccer')
 cur = conn.cursor()
 cur.execute ('USE soccer')

 data = (name, team, position, number, dateofbirth, nationality, salary)
 cur.execute('INSERT INTO player (name, team_name, position, shirt_number, dateofbirth, nationality, salary) VALUES (%s,%s,%s,%s,%s,%s, %s)',data)
 cur.connection.commit()


            
def stripaccents(s):
 return ''.join(c for c in unicodedata.normalize('NFD',s) if unicodedata.category(c) != 'Mn')

def addteamvalues(rank,name):
 conn = pymysql.connect(host = '127.0.0.1', user = 'root', passwd = 'Yusarang10101993!', db = 'soccer')
 cur = conn.cursor()
 cur.execute('USE soccer')
 
 data1 = (rank,name)
 cur.execute('INSERT INTO team (rank,team_name) VALUES (%s,%s)',data1)
 cur.connection.commit()
 
def addteamtotalvalues(games,wins,draws,losses,goals,goals_lost,goal_difference,points):
 conn = pymysql.connect(host = '127.0.0.1', user = 'root', passwd = 'Yusarang10101993!', db = 'soccer')
 cur = conn.cursor()
 cur.execute('USE soccer')

 data2 = (games,wins,draws,losses,goals,goals_lost,goal_difference,points)
 cur.execute('INSERT INTO team_totals (team_games, team_wins, team_draws, team_losses, team_goals, team_goals_conceded, team_difference, team_points) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',data2)
 cur.connection.commit()

def main():

 connection = http.client.HTTPConnection('api.football-data.org')
 headers = { 'X-Auth-Token': 'eb3e492624d444f49e859ba3afa146bf', 'X-Response-Control': 'full' }
 connection.request('GET', '/v1/soccerseasons/398/leagueTable', None, headers )
 response = json.loads(connection.getresponse().read().decode())

 teamRank = []
 teamName = []
 teamGamesPlayed = []
 teamWins = []
 teamDraws = []
 teamLosses = []
 teamGoals = []
 teamGoalsLost = []
 teamGoalsDifference = []
 teamPoints = []

 for item in response["standing"]:
  teamRank.append(item['position'])
  teamName.append(item['teamName'])
  teamGamesPlayed.append(item['playedGames'])
  teamWins.append(item['wins'])
  teamDraws.append(item['draws'])
  teamLosses.append(item['losses'])
  teamGoals.append(item['goals'])
  teamGoalsLost.append(item['goalsAgainst'])
  teamGoalsDifference.append(item['goalDifference'])
  teamPoints.append(item['points'])
 for i in range(0,len(teamRank)):
  addteamvalues(teamRank[i],teamName[i])
 for i in range(0,len(teamRank)):
  addteamtotalvalues(teamGamesPlayed[i],teamWins[i],teamDraws[i],teamLosses[i],teamGoals[i],teamGoalsLost[i],teamGoalsDifference[i],teamPoints[i])
  


 connection = http.client.HTTPConnection('api.football-data.org')
 headers = { 'X-Auth-Token': 'eb3e492624d444f49e859ba3afa146bf', 'X-Response-Control': 'minified' }
 connection.request('GET', '/v1/soccerseasons/398/teams', None, headers )
 response = json.loads(connection.getresponse().read().decode())

 conn = pymysql.connect(host = '127.0.0.1', user = 'root',passwd = 'Yusarang10101993!', db = 'soccer')
 cur = conn.cursor()
 cur.execute ('USE soccer')

 playerName = []
 playerTeam = []
 playerPosition = []
 playerNumber = []
 playerDateOfBirth = []
 playerNationality = []
 playerMarketValue = []
 playerSalary = []
 salary = ''

 for item in response['teams']:
  teamName = item['name']

  api_key = '/v1/teams/' + str(item['id'] ) + '/players'
  connection.request('GET', api_key, None, headers)
  response2 = json.loads(connection.getresponse().read().decode())
  for item2 in response2['players']:

   playerName.append(stripaccents(item2['name']))
   playerTeam.append(teamName)
   playerPosition.append(stripaccents(item2['position']))
   playerNumber.append(item2['jerseyNumber'])
   playerDateOfBirth.append(item2['dateOfBirth'])
   playerNationality.append(item2['nationality'])
   playerMarketValue.append(item2['marketValue'])
		  
 for i in range(0, len(playerMarketValue)):
  if playerMarketValue[i] == None:
   playerMarketValue[i] = 'No Information'
  salary = playerMarketValue[i].replace(u"\u20AC","")
  playerSalary.append(salary)
  
 for i in range(0, len(playerName)):
  addvalues(playerName[i], playerTeam[i], playerPosition[i], playerNumber[i], playerDateOfBirth[i], playerNationality[i], playerSalary[i])

main()
