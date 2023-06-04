import utils.aesutil
from getpass import getpass

from Cryptodome.Protocol.KDF import PBKDF2
from Cryptodome.Hash import SHA512
from Cryptodome.Random import get_random_bytes
import base64
import sqlite3
from utils.dbconfig import dbconfig
def get_secret_creds():

    
    db = dbconfig()
    cursor = db.cursor()
    query = "SELECT * FROM secrets"
    cursor.execute(query)
    result = cursor.fetchall()[0]
    return result
    

def computeMasterKey(mp,ds):
	password = mp.encode()
	salt = ds.encode()
	key = PBKDF2(password, salt, 32, count=1000000, hmac_hash_module=SHA512)
	return key


def checkEntry(username):
	db = dbconfig()
	cursor = db.cursor()
	query = "SELECT * FROM entries WHERE username = '{}'".format(username)
	cursor.execute(query)
	


	if len(cursor.execute(query).fetchall()) == 1:
		db.close()
		return True
	else:
		db.close()
		return False


def addEntry(username, password):
	# Check if the entry already exists
	if checkEntry(username):
		
		return False

	
	creds = get_secret_creds()
	mp = creds[0]
	ds = creds[1]

	# compute master key
	mk = computeMasterKey(mp,ds)

	# encrypt password with mk
	encrypted = utils.aesutil.encrypt(key=mk, source=password, keyType="bytes")

	# Add to db
	db = dbconfig()
	cursor = db.cursor()
	query = "INSERT INTO entries (username, password) values ('{}', '{}')".format(username, encrypted)
	cursor.execute(query)
	db.commit()
	db.close()


	return True
#print(checkEntry("1234567"))
