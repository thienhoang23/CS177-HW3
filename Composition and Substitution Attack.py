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

def main():
	append_list = []

	for i in range(1,6):
		allCombos = itertools.product(NUMBERS, repeat=i)
		for combo in allCombos:
			appending = ""
			for each_word in combo:
				appending = appending + each_word
			append_list.append(appending)

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
				continual_mod_password = continual_mod_password.replace(char, Substitutions[char])
				for each_appending in append_list:
					number_padded_mod_password = continual_mod_password + each_appending
					hash_res = Extract_Data.Crypt(number_padded_mod_password, salt)
					if(hash_res == password_hash):
						print "{}:{}".format(acc, number_padded_mod_password)
						found = True
						break
				if found == True:
					break
			if found == True:
				break
	file.close()


if __name__ == '__main__':
	main()