import os
import sys
import string
import random
import hashlib
import sys
from getpass import getpass
import sqlite3
from utils.dbconfig import dbconfig



def checkConfig():
	db = dbconfig()
	cursor = db.cursor()
	query = ''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='secrets' '''

	if cursor.execute(query).fetchone()[0] == 1:
		db.close()
		return True
	else:
		db.close()
		return False
	
	
	


def generateDeviceSecret(length=10):
	return ''.join(random.choices(string.ascii_uppercase + string.digits, k = length))


def make(mp):
	
	print("Creating new config")

	# Create database
	#db = dbconfig()
	#cursor = db.cursor()
	try:
		#cursor.execute("CREATE DATABASE pm")
		cursor = sqlite3.connect('test.db')
	except Exception as e:
		printc("An error occurred while trying to create db. Check if database with name 'pm' already exists - if it does, delete it and try again.")
		sys.exit(0)

	print("Database created")

	# Create tables
	query = "CREATE TABLE secrets (masterkey_hash TEXT NOT NULL, device_secret TEXT NOT NULL);"
	res = cursor.execute(query)
	print("[green][+][/green] Table 'secrets' created ")

	query = "CREATE TABLE entries (username TEXT, password TEXT NOT NULL);"
	res = cursor.execute(query)
	print("[green][+][/green] Table 'entries' created ")


	print("[green][+] A [bold]MASTER PASSWORD[/bold] is the only password you will need to remember in-order to access all your other passwords. Choosing a strong [bold]MASTER PASSWORD[/bold] is essential because all your other passwords will be [bold]encrypted[/bold] with a key that is derived from your [bold]MASTER PASSWORD[/bold]. Therefore, please choose a strong one that has upper and lower case characters, numbers and also special characters. Remember your [bold]MASTER PASSWORD[/bold] because it won't be stored anywhere by this program, and you also cannot change it once chosen. [/green]\n")

	

	# Hash the MASTER PASSWORD
	hashed_mp = hashlib.sha256(mp.encode()).hexdigest()
	print("[green][+][/green] Generated hash of MASTER PASSWORD")


	# Generate a device secret
	ds = generateDeviceSecret()
	print("[green][+][/green] Device Secret generated")

	# Add them to db
	query = "INSERT INTO secrets (masterkey_hash, device_secret) values ('{}', '{}')".format(str(hashed_mp), str(ds))
	cursor.execute(query)
	cursor.commit()

	print("[green][+][/green] Added to the database")

	print("[green][+] Configuration done![/green]")

	cursor.close()



