import mysql.connector

import sqlite3
def dbconfig():
  try:
    # db = mysql.connector.connect(
    #   host ="localhost",
    #   user ="pm",
    #   passwd ="password"
    # )
    db = sqlite3.connect('test.db')
    
    # printc("[green][+][/green] Connected to db")
  except Exception as e:
    print("An error occurred while trying to connect to the database", e)
    

  return db