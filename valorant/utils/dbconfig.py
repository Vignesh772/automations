
import sqlite3
import os
def dbconfig():
  try:
    # db = mysql.connector.connect(
    #   host ="localhost",
    #   user ="pm",
    #   passwd ="password"
    # )
    try:
      os.mkdir("C:\\RiotLaucher")
    except Exception as e:
      pass
    db = sqlite3.connect('C:\\RiotLaucher\\database.db')
    
    # printc("[green][+][/green] Connected to db")
  except Exception as e:
    print("An error occurred while trying to connect to the database", e)
    

  return db