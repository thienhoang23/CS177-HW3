import crypt

def Crypt(password, salt):
	e_pass = crypt.crypt(password, salt)
	return e_pass

def getSalt(expect_hash_res):
	if ('$' in expect_hash_res) == False:
		return expect_hash_res[0:2]
	index_of_last_delimiter = expect_hash_res.rfind('$')
	return expect_hash_res[0:index_of_last_delimiter]

Accounts_Pass_Pairs = {}

#Assigning acc_pass pair
file = open("shadow","r")
for line in file:
	line = line[:-1]
	Account_Pass_Pair = line.split(":", 1)
	Accounts_Pass_Pairs[Account_Pass_Pair[0]] = Account_Pass_Pair[1]
file.close()

for acc in Accounts_Pass_Pairs:
	found_message = False
	expect_hash_res = Accounts_Pass_Pairs[acc]
	salt = getSalt(expect_hash_res)
	# Dictionary Attack
	file = open("wordsEn.txt","r")
	for line in file:
		line = line[:-1]
		hash_res = Crypt(line, salt)
		for i in range(0,999):
			hash_res = Crypt(hash_res, salt)
		if(hash_res == expect_hash_res):
			print line
			found_message = True
			break
	file.close()
	"""
	# Common Passwords Attack
	file = open("rockyou.txt","r")
	for line in file:
		line = line[:-1]
		hash_res = Crypt(line, salt)
		if(hash_res == expect_hash_res):
			print line
			found_message = True
			break
	file.close()
	"""