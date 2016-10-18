import crypt

def getAccountsAndPassHashes():
	Accounts_Pass_Pairs = {}
	file = open("shadow","r")
	for line in file:
		line = line[:-1]
		stored_data_components = line.split(":")
		account = stored_data_components[0]
		password_hash = stored_data_components[1] 
		Accounts_Pass_Pairs[account] = password_hash
	file.close()
	return Accounts_Pass_Pairs

def getSalt(expect_hash_res):
	if ('$' in expect_hash_res) == False:
		return expect_hash_res[0:2]
	index_of_last_delimiter = expect_hash_res.rfind('$')
	return expect_hash_res[0:index_of_last_delimiter]

def Crypt(password, salt):
	e_pass = crypt.crypt(password, salt)
	return e_pass