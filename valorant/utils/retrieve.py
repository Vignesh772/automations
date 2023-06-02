import utils.aesutil

from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes
import base64
import sqlite3


def computeMasterKey(db):
	#db = sqlite3.connect('C:\\Users\\V Vignesh\\Documents\\GitHub\\automations\\valorant\\test.db')
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
	db = sqlite3.connect('C:\\Users\\V Vignesh\\Documents\\GitHub\\automations\\valorant\\test.db')
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