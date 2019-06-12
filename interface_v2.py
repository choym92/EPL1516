import pymysql
def main(): 
 #connect to database
 conn = pymysql.connect(host='127.0.0.1', user='root', passwd='Yusarang10101993!', db='soccer')
 cur = conn.cursor()
 cur2 = conn.cursor()
 cur.execute("USE soccer")
 cur2.execute("USE soccer")
 
 #welcome statements
 print ("Welcome to the English Premeire League Database.")
 print ("Please Select one of the following options.")
 
 response = int(input("1. Exit"+"\n"+"2. Matches"+"\n"+"3. Teams"+"\n"+"4. Players"+"\n"))
 
 #user inputs
 if response == 1:
  print("Good Bye!")
 
 #match search 
 if response == 2:
  print("\n"+"----------------------------------")
  print("Would you like to search matches by the match date or home team?")
  match_response = int(input("1. Match Date"+"\n" + "2. Home Team"+"\n"))
  
  if match_response == 1:
   print("\n"+"----------------------------------")
   match_date = input("Please enter the date of the match (YYYY-MM-DD): ")
   cur.execute("SELECT g.game_date, t.team_name, h.home_goals FROM game g, team t, home_team h WHERE g.game_id = h.game_id AND h.team_id = t.team_id AND g.game_date = %s", match_date)
   for line in cur:
    print("Date: ",line[0])
    print("Home Team: ",line[1])
    print("Goals Made: ",line[2],"\n")
   cur.execute("SELECT t.team_name, a.away_goals FROM game g, team t, away_team a WHERE g.game_id = a.game_id AND a.team_id = t.team_id AND g.game_date = %s", match_date)
   for line in cur:
    print("Away Team: ",line[0])
    print("Goals Made: ",line[1])
	
   
  if match_response == 2:
   print("\n"+"----------------------------------")
   match_team = input("Please enter the name of the home team: ")
   cur.execute("SELECT g.game_date, t.team_name, h.home_goals FROM game g, team t, home_team h WHERE g.game_id = h.game_id AND h.team_id = t.team_id AND t.team_name = %s", match_team)
   for line in cur:
    print("Date: ",line[0])
    print("Home Team: ",line[1])
    print("Goals Made: ",line[2],"\n")
   cur.execute("SELECT t.team_name, a.away_goals FROM game g, team t, away_team a WHERE g.game_id = a.game_id AND a.team_id = t.team_id AND g.game_date = %s", match_date)
   for line in cur:
    print("Away Team: ",line[0])
    print("Goals Made: ",line[1])
   
 #team search
 if response == 3:
  print("\n"+"----------------------------------")
  team_question = int(input("Would you like to see a list of teams to choose from?"+"\n"+"1. Yes"+"\n"+"2. No" +"\n"))
  if team_question == 1:
   print("\n"+"----------------------------------")
   cur.execute("SELECT team_name FROM team")
   for line in cur:
    print(line[0])
   print("\n"+"----------------------------------")
   team_input = input("Enter the name of the team you would like to search: ")
   print("\n"+team_input + " has been selected")
   team_data = int(input("\n"+"Select the information you would like:"+"\n"+"1. Players"+"\n"+"2. Total Wins"+"\n"+"3. Total Losses"+"\n"))
   
   if team_data == 1:
    print("\n"+"----------------------------------")
    cur.execute("SELECT p.f_name, p.l_name FROM player p, team t WHERE p.team_id = t.team_id AND t.team_name = %s",team_input)
    for line in cur:
     print(line[0],line[1])
	 
   if team_data == 2:
    cur.execute("SELECT t.team_wins FROM team_totals t, team x WHERE t.team_id = x.team_id AND x.team_name = %s",team_input)
    for line in cur:
     print("Total Wins",line[0])
	 
   if team_data == 3:
    cur.execute("SELECT t.team_losses FROM team_totals t, team x WHERE t.team_id = x.team_id AND x.team_name = %s",team_input)
    for line in cur:
     print("Total Losses",line[0])
   
  # dont list the team names
  if team_question == 2:
   print("\n"+"----------------------------------")
   team_input = input("Enter the name of the team you would like to search: ")
   print("\n"+team_input + " has been selected")
   team_data = int(input("\n"+"Select the information you would like:"+"\n"+"1. Players"+"\n"+"2. Total Wins"+"\n"+"3. Total Losses"+"\n"))
   
   if team_data == 1:
    print("\n"+"----------------------------------")
    cur.execute("SELECT p.f_name, p.l_name FROM player p, team t WHERE p.team_id = t.team_id AND t.team_name = %s",team_input)
    for line in cur:
     print(line[0],line[1])
	 
   if team_data == 2:
    cur.execute("SELECT t.team_wins FROM team_totals t, team x WHERE t.team_id = x.team_id AND x.team_name = %s",team_input)
    for line in cur:
     print("Total Wins",line[0])
	 
   if team_data == 3:
    cur.execute("SELECT t.team_losses FROM team_totals t, team x WHERE t.team_id = x.team_id AND x.team_name = %s",team_input)
    for line in cur:
     print("Total Losses",line[0])
  
  
 #player search
 if response == 4:
  print("\n"+"----------------------------------")
  player_selection = int(input("Would you like to search for player by first or last name?"+"\n"+"1. First Name" + "\n" + "2. Last Name"+"\n"))
  
  #last or first name
  if player_selection == 1:
   print("\n"+"----------------------------------")
   first_name = input("\n"+"Enter the first name of the player: ")
   cur.execute("SELECT player_id, f_name, l_name FROM player WHERE f_name = %s",first_name)
   print("\n"+"Players"+"\n")
   for line in cur:
    print("Player ID:",line[0])
    print("Player Name:",line[1],line[2])
	
   #choose information
   print("\n"+"----------------------------------")
   player_selection = input("Select Player Last Name: ")
   print("\n"+"----------------------------------")
   player_stat = int(input("Select the information you would like"+"\n"+"1. General Information"+"\n"+"2. Offensive Stats"+"\n"+"3. Defensive Stats"+"\n"))
   
   if player_stat == 1:
    print("\n"+"----------------------------------")
    cur.execute("SELECT p.f_name, p.l_name, t.team_name, p.nationality, p.salary, p.height, p.weight, p.dominant_foot FROM player p, team t WHERE p.team_id = t.team_id AND p.l_name = %s",player_selection)
    for line in cur:
     print("Player Name:",line[0],line[1])
     print("Team:",line[2])
     print("Nationality:",line[3])
     print("Salary:",line[4])
     print("Height(cm):",line[5])
     print("Weight(kg):",line[6])
     print("Dominant Foot:", line[7])
	 
   if player_stat == 2:	
    cur.execute("SELECT p.f_name, p.l_name, o.goals, o.assists, o.playing_time_minutes FROM player p, offense o, WHERE p.l_name = %s", player_selection)
    for line in cur:
     print("Player Name:",line[0],line[1])
     print("Number of Goals:",line[2])
     print("Number of Assists:",line[3])
     print("Playing Time (minutes):",line[4])
	 
   if player_stat == 3:
    cur.execute("SELECT p.f_name, p.l_name, d.goals_lost, d.tackles_made, d.fouls, d.saves, d.clean_sheet FROM player p, defense d WHERE p.player_id = d.player_id AND p.l_name = %s",player_selection)
    for line in cur:
     print("Player Name:",line[0],line[1])
     print("Goals Lost:",line[2])
     print("Tackles Made:", line[3])
     print("Fouls:", line[4])
     print("Saves:",line[5])
     print("Clean Sheets:",line[6])
	 
  if player_selection == 2:
   print("\n"+"----------------------------------")
   last_name = input("\n"+"Enter the last name of the player: ")
   cur.execute("SELECT player_id, f_name, l_name FROM player WHERE l_name = %s",last_name)
   for line in cur:
    print("Player ID:",line[0])
    print("Player Name:",line[1],line[2])
	
   #choose information
   print("\n"+"----------------------------------")
   player_selection = input("Select Player First Name: ")
   print("\n"+"----------------------------------")
   player_stat = int(input("Select the information you would like"+"\n"+"1. General Information"+"\n"+"2. Offensive Stats"+"\n"+"3. Defensive Stats"+"\n"))
   
   if player_stat == 1:
    print("\n"+"----------------------------------")
    cur.execute("SELECT p.f_name, p.l_name, t.team_name, p.nationality, p.salary, p.height, p.weight, p.dominant_foot FROM player p, team t WHERE p.team_id = t.team_id AND p.f_name = %s",player_selection)
    for line in cur:
     print("Player Name:",line[0],line[1])
     print("Team:",line[2])
     print("Nationality:",line[3])
     print("Salary:",line[4])
     print("Height(cm):",line[5])
     print("Weight(kg):",line[6])
     print("Dominant Foot:", line[7])
	 
   if player_stat == 2:	
    cur.execute("SELECT p.f_name, p.l_name, o.goals, o.assists, o.playing_time_minutes FROM player p, offense o, WHERE p.player_id = o.player_id AND p.f_name = %s", player_selection)
    for line in cur:
     print("Player Name:",line[0],line[1])
     print("Number of Goals:",line[2])
     print("Number of Assists:",line[3])
     print("Playing Time (minutes):",line[4])
	 
   if player_stat == 3:
    cur.execute("SELECT p.f_name, p.l_name, d.goals_lost, d.tackles_made, d.fouls, d.saves, d.clean_sheet FROM player p, defense d WHERE p.player_id = d.player_id AND p.f_name = %s",player_selection)
    for line in cur:
     print("Player Name:",line[0],line[1])
     print("Goals Lost:",line[2])
     print("Tackles Made:", line[3])
     print("Fouls:", line[4])
     print("Saves:",line[5])
     print("Clean Sheets:",line[6])
 
main()