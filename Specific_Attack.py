import Extract_Data
import sys
import crypt

Accounts_Pass_Pairs = Extract_Data.getAccountsAndPassHashes()

account = sys.argv[1]
password = sys.argv[2]
salt = sys.argv[3]
e_pass = crypt.crypt(password, salt)
print e_pass == Accounts_Pass_Pairs[account]