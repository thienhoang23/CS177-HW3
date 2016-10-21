import Extract_Data
import string
import sys

Accounts_Pass_Pairs = Extract_Data.getAccountsAndPassHashes()
def main():
	acc = sys.argv[1]
	expect_hash_res = Accounts_Pass_Pairs[acc]
	salt = Extract_Data.getSalt(expect_hash_res)
	file = open("wordsEn.txt","r")
	for password in file:
		password = password[:-2]
		if len(password) < 6:
			continue
		continual_cap_pass = password
		for i in range(0, len(password)):
			capitalized_letter = password[i:i+1]
			capitalized_letter = capitalized_letter.upper()
			capitalized_i_letter_pass = password[:i] + capitalized_letter + password[i+1:]
			hash_res1 = Extract_Data.Crypt(capitalized_i_letter_pass, salt)
			if(hash_res1 == expect_hash_res):
				print "{}:{}".format(acc, capitalized_i_letter_pass)
				return
			continual_cap_pass = continual_cap_pass[:i] + capitalized_letter + continual_cap_pass[i+1:]
			hash_res2 = Extract_Data.Crypt(continual_cap_pass, salt)
			if(hash_res2 == expect_hash_res):
				print "{}:{}".format(acc, continual_cap_pass)
				return
	file.close()

if __name__ == '__main__':
	main()