import Extract_Data
import itertools
import sys


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

	if len(sys.argv) == 1 :
		for acc in Accounts_Pass_Pairs:
			
			expect_hash_res = Accounts_Pass_Pairs[acc]
			salt = Extract_Data.getSalt(expect_hash_res)
			# Dictionary Attack
			file = open("wordsEn.txt","r")
			for password in file:
				password = password[:-2]
				if (len(password) < 2):
					break
				for each_appending in append_list:
					mod_password = password + each_appending
					hash_res = Extract_Data.Crypt(mod_password, salt)
					if(hash_res == expect_hash_res):
						print "{}:{}".format(acc, mod_password)
						file.close()
						return
	else:
		acc = sys.argv[1]
		expect_hash_res = Accounts_Pass_Pairs[acc]
		salt = Extract_Data.getSalt(expect_hash_res)
		# Dictionary Attack
		file = open("wordsEn.txt","r")
		for password in file:
				password = password[:-2]
				if (len(password) < 3):
					continue
				for each_appending in append_list:
					mod_password = password + each_appending
					print mod_password
					hash_res = Extract_Data.Crypt(mod_password, salt)
					if(hash_res == expect_hash_res):
						print "{}:{}".format(acc, mod_password)
						file.close()
						return

if __name__ == '__main__':
	main()