import Extract_Data
import string
import itertools

NUMBERS = "0123456789"

def main():
	Accounts_Pass_Pairs = Extract_Data.getAccountsAndPassHashes()
	acc = 'targaryend'
	password_hash = Accounts_Pass_Pairs[acc]
	salt = Extract_Data.getSalt(password_hash)
	i = 5
	while True:
		allCombos = itertools.product(NUMBERS, repeat=i+1)
		for combo in allCombos:
			password = ""
			for each_word in combo:
				password = password + each_word
			hash_res = Extract_Data.Crypt(password, salt)
			if(hash_res == password_hash):
				print "{}:{}".format(acc, password)
				return
if __name__ == '__main__':
	main()