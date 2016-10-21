import Extract_Data
import string
import itertools

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

NUMBERS = "0123456789"

Accounts_Pass_Pairs = Extract_Data.getAccountsAndPassHashes()

def main():
	acc = 'j_snow'
	expect_hash_res = Accounts_Pass_Pairs[acc]
	salt = Extract_Data.getSalt(expect_hash_res)

	file = open("wordsEn.txt","r")
	for password in file:
		password = password[:-2]
		if len(password) > 8:
			continue
		for char in Substitutions:
			password = password.replace(char,Substitutions[char])
		if len(password) < 8:
			diff = 8 - len(password)
			for i in range(1,diff+1):
				allCombos = itertools.product(NUMBERS, repeat=i)
				for combo in allCombos:
					appending = ""
					for each_word in combo:
						appending = appending + each_word
					mod_password = password + appending
					hash_res = Extract_Data.Crypt(mod_password, salt)
					if(hash_res == expect_hash_res):
						print "{}:{}".format(acc, mod_password)
						return
	file.close()

if __name__ == '__main__':
	main()