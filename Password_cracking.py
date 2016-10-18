import crypt

def Crypt(password, salt):
  e_pass = crypt.crypt(password, salt)
  return e_pass

file = open("shadow","r")
Accounts_Pass_Pairs = {}

for line in file:
	line = line[:-1]
	Account_Pass_Pair = line.split(":", 1)
	Accounts_Pass_Pairs[Account_Pass_Pair[0]] = Account_Pass_Pair[1]
file.close()

target = 'j_snow'

file = open("wordsEn.txt","r")
for line in file:
	line = line[:-1]
	hash_res = Crypt(line, "aa")
	if(hash_res == Accounts_Pass_Pairs[target]):
		print line
		break
file.close()

file = open("rockyou.txt","r")
for line in file:
	line = line[:-1]
	hash_res = Crypt(line, "aa")
	if(hash_res == Accounts_Pass_Pairs[target]):
		print line
		break
file.close()