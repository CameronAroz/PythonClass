from hashlib import md5
from hashlib import sha256
from base64 import standard_b64encode

solution_file = "unlocked.txt"
dictionary_file = "british-english.txt"
encrypted_dictionary = "encrypted_possibilities.txt"

#Creating a File With The Passwords
dictionary = open(dictionary_file, "r")
encrypted_d = open(encrypted_dictionary, "w")
salt = "saltysaltgoodness"

for line in dictionary:
	word = line.rstrip()
	encrypted1 = md5(word+salt).hexdigest()
	encrypted2 = sha256(word+salt).hexdigest()
	encrypted3 = standard_b64encode(sha256(word+salt).hexdigest())
	encrypted_d.write("{}:{}\n".format(word,encrypted1))
	encrypted_d.write("{}:{}\n".format(word,encrypted2))
	encrypted_d.write("{}:{}\n".format(word,encrypted3))
	
#Always close the files
dictionary.close()
encrypted_d.close()


	
	
	
