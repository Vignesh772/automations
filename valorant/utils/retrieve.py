import utils.aesutil

from Cryptodome.Protocol.KDF import PBKDF2
from Cryptodome.Hash import SHA512
from Cryptodome.Random import get_random_bytes
import base64
import sqlite3
from utils.dbconfig import dbconfig

def computeMasterKey(db):
	cursor = db.cursor()
	query = "SELECT * FROM secrets"
	cursor.execute(query)
	result = cursor.fetchall()[0]

	password = result[0].encode()
	salt = result[1].encode()
	key = PBKDF2(password, salt, 32, count=1000000, hmac_hash_module=SHA512)
	return key

def retrieveEntries():
	user_pass_list = []
	db = dbconfig()
	cursor = db.cursor()

	query = "SELECT * FROM entries"
	

	cursor.execute(query)
	results = cursor.fetchall()
	
	if len(results) == 0:
		
		return user_pass_list
	mk = computeMasterKey(db)
	for i in results:
		

		# decrypt password
		decrypted = utils.aesutil.decrypt(key=mk,source=i[1],keyType="bytes")
		decrypted=decrypted.decode()
		user_pass_list.append((i[0],decrypted))




	
	
	db.close()
	return user_pass_list
#print(retrieveEntries())