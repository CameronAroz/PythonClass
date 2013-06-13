
attack_list = []
identified_target_list = []
combined_filename = "encrypted_possibilities.txt"
attack_filename = "big_guy.txt"
solutions = "solutions.txt"

##Reading in the Possible Encryptions
read_this_file = open(combined_filename, "r")
write_cracked_passwords = open(solutions,"w")

print "\nInitializing the attack list:"

##Array of All possible words and with their corresponding encrypted password
for line in read_this_file:
	(plaintext, encrypted) = line.split(":")
	attack_list.append((plaintext,encrypted.rstrip()))
read_this_file.close()

#Identify Targets
print "\nIdentify the targets:"

##Opening the file and read in the users we're going to attack
attack_this_file = open(attack_filename, 'r')
for line in attack_this_file:
	(user,uid,encrypted_pw) = line.rstrip().split(":")
	identified_target_list.append((user,encrypted_pw))

attack_this_file.close()

##Attack the targets
print "\nInitiate Attack Sequence"
for target in identified_target_list:
	(user,target_password) = target
	
	#Check passwords
	for word in attack_list:
		(attack_word_plaintext,attack_word_encrypted) = word
		if target_password == attack_word_encrypted:
			print "Target identified! user:{}\tpassword:{}".format(user,attack_word_plaintext)
			write_cracked_passwords.write("Target identified! user:{}\tpassword:{} \n".format(user,attack_word_plaintext))

write_cracked_passwords.close()
		
			
			
	







