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
		password_hash = Accounts_Pass_Pairs[target]
		salt = Extract_Data.getSalt(password_hash)
		file = open('wordsEn.txt','r')
		for password in file:
		password = password[:-2]
		if(len(password) < 6 or len(password) > 8):
			continue
		hash_res = Extract_Data.Crypt(password, salt)
		if(hash_res == password_hash):
			print "{}:{}".format(target,password)
			return
		for char in Substitutions:
			mod_pass = password.replace(char,Substitutions[char])
			print mod_pass
			hash_res = Extract_Data.Crypt(password, salt)
			if(hash_res == password_hash):
				print "{}:{}".format(target,mod_password)
				return
	file.close()


if __name__ == '__main__':
	main()