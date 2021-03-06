import Extract_Data
import string
import itertools

LOWERCASE_ALPHA = "abcdefghijklmnopqrstuvwxyz"

def main():
	Accounts_Pass_Pairs = Extract_Data.getAccountsAndPassHashes()
	target = 'j_snow'
	password_hash = Accounts_Pass_Pairs[target]
	salt = Extract_Data.getSalt(password_hash)
	for i in range(6,9):
		allCombos = itertools.product(LOWERCASE_ALPHA, repeat=i)
		for combo in allCombos:
			password = ""
			for each_word in combo:
				password = password + each_word
			hash_res = Extract_Data.Crypt(password, salt)
			if(hash_res == password_hash):
				print "{}:{}".format(target, password)
				return

if __name__ == '__main__':
	main()