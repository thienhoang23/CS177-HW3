import Extract_Data

Accounts_Pass_Pairs = Extract_Data.getAccountsAndPassHashes()

for acc in Accounts_Pass_Pairs:
	expect_hash_res = Accounts_Pass_Pairs[acc]
	salt = Extract_Data.getSalt(expect_hash_res)
	file = open("wordsEn.txt","r")
	for password in file:
		password = password[:-2]
		first_letter = password[0:1]
		capitalized_first_letter_pass = first_letter.upper() + password[1:]
		hash_res1 = Extract_Data.Crypt(capitalized_first_letter_pass, salt)
		if(hash_res1 == expect_hash_res):
			print "{}:{}".format(acc, capitalized_first_letter_pass)
			break
		capitalized_pass = password.upper()
		hash_res2 = Extract_Data.Crypt(capitalized_pass, salt)
		if(hash_res2 == expect_hash_res):
			print "{}:{}".format(acc, capitalized_pass)
			break
	file.close()