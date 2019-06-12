import pymysql
def main(): 
 #connect to database
 conn = pymysql.connect(host='127.0.0.1', user='root', passwd='Yusarang10101993!', db='soccer')
 cur = conn.cursor()
 cur.execute("USE soccer")
 
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
	
   
  if match_response == 2:
   print("\n"+"----------------------------------")
   match_team = input("Please enter the name of the home team: ")
   cur.execute("SELECT g.game_date, t.team_name, h.home_goals FROM game g, team t, home_team h WHERE g.game_id = h.game_id AND h.team_id = t.team_id AND t.team_name = %s", match_team)
   for line in cur:
    print("Date: ",line[0])
    print("Home Team: ",line[1])
    print("Goals Made: ",line[2],"\n")
   
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
    print("yes")
	#fix code here
    cur.execute("SELECT p.f_name, p.l_name FROM player p, team t, WHERE p.team_id = t.team_id AND t.team_name = %s",team_input)
   if team_data == 2:
    print("no")

  if team_question == 2:
   print("\n"+"----------------------------------")
   team_input = input("Enter the name of the team you would like to search: ")
   print("\n"+team_input + " has been selected")
   team_data = int(input("\n"+"Select the information you would like:"+"\n"+"1. Players"+"\n"+"2. Total Wins"+"\n"+"3. Total Losses"+"\n"))
  
  
 #player search
 if response == 4:
  print("\n"+"----------------------------------")
  player_selection = int(input("Would you like to search for player by first or last name?"+"\n"+"1. First Name" + "\n" + "2. Last Name"+"\n"))
  
  #last or first name
  if player_selection == 1:
   print("\n"+"----------------------------------")
   first_name = input("\n"+"Enter the first name of the player: ")
   cur.execute("SELECT f_name, l_name FROM player WHERE f_name = %s",first_name)
   print("\n"+"Players"+"\n")
   for line in cur:
    print(line[0],line[1])
	
   print("\n"+"----------------------------------")
   player_selection = input("Select Player: ")
   print("\n"+"----------------------------------")
   player_stat = int(input("Select the information you would like"+"\n"+"1. General Information"+"\n"+"2. Offensive Stats"+"\n"+"3. Defensive Stats"+"\n"))
   
  if player_selection == 2:
   print("\n"+"----------------------------------")
   last_name = input("\n"+"Enter the last name of the player: ")
   cur.execute("SELECT f_name, l_name FROM player WHERE l_name = %s",last_name)
   print("\n"+"Players"+"\n")
   for line in cur:
    print(line[0],line[1])

 
 
main()