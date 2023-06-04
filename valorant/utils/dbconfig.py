
import sqlite3
import os
def dbconfig():
  try:
    # db = mysql.connector.connect(
    #   host ="localhost",
    #   user ="pm",
    #   passwd ="password"
    # )
    if not os.path.exists("C:\\RiotLauncher"):
        os.mkdir("C:\\RiotLauncher")

    db = sqlite3.connect('C:\\RiotLauncher\\database.db')
    
    # printc("[green][+][/green] Connected to db")
  except Exception as e:
    print("An error occurred while trying to connect to the database", e)
    

  return db