import Extract_Data

Accounts_Pass_Pairs = Extract_Data.getAccountsAndPassHashes()

for acc in Accounts_Pass_Pairs:
	expect_hash_res = Accounts_Pass_Pairs[acc]
	salt = Extract_Data.getSalt(expect_hash_res)

	# Dictionary Attack
	file = open("wordsEn.txt","r")
	for password in file:
		hash_res = Extract_Data.Crypt(password, salt)
		if(hash_res == expect_hash_res):
			print "{}:{}".format(acc, password)
			break
	file.close()