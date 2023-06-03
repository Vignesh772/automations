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
		cursor = dbconfig()
	except Exception as e:
		printc("An error occurred while trying to create db. Check if database with name 'pm' already exists - if it does, delete it and try again.")
		sys.exit(0)


	# Create tables
	query = "CREATE TABLE secrets (masterkey_hash TEXT NOT NULL, device_secret TEXT NOT NULL);"
	res = cursor.execute(query)

	query = "CREATE TABLE entries (username TEXT, password TEXT NOT NULL);"
	res = cursor.execute(query)



	

	# Hash the MASTER PASSWORD
	hashed_mp = hashlib.sha256(mp.encode()).hexdigest()


	# Generate a device secret
	ds = generateDeviceSecret()

	# Add them to db
	query = "INSERT INTO secrets (masterkey_hash, device_secret) values ('{}', '{}')".format(str(hashed_mp), str(ds))
	cursor.execute(query)
	cursor.commit()



	cursor.close()



