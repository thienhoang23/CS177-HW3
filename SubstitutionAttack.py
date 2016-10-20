import Extract_Data
import string

Substitutions = {
	'l' : '1',
	'i' : '1',
	'e'	: '3',
	't' : '7',
	'l' : '7',
	's' : '5',
	'a' : '4',
	'h' : '4',
	'b' : '8',
	'g' : '9',
	'q'	: '9',
	'o' : '0',
}

def main():
	Accounts_Pass_Pairs = Extract_Data.getAccountsAndPassHashes()

	for acc in Accounts_Pass_Pairs:
		found = False
		password_hash = Accounts_Pass_Pairs[acc]
		salt = Extract_Data.getSalt(password_hash)
		file = open('wordsEn.txt','r')
		for password in file:
			password = password[:-2]
			if(len(password) < 6):
				continue
			continual_mod_password = password
			for char in Substitutions:
				mod_password = password.replace(char,Substitutions[char])
				continual_mod_password = continual_mod_password.replace(char,Substitutions[char])
				hash_res1 = Extract_Data.Crypt(mod_password, salt)
				hash_res2 = Extract_Data.Crypt(continual_mod_password, salt)
				if(hash_res1 == password_hash):
					print "{}:{}".format(acc, mod_password)
					found == True
					break
				if(hash_res2 == password_hash):
					print "{}:{}".format(acc, continual_mod_password)
					found == True
					break
			if found == True:
				break
	file.close()


if __name__ == '__main__':
	main()