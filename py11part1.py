import re
test_str = "Balaji, is best : for ! Balaji ;"
print("The original string is : " + test_str)
res = re.sub(r'[^\w\s]', '', test_str)
print("The string after punctuation filter : " + res)

import re
def isAllPresent(str):

	regex = ("^(?=.*[a-z])(?=." +
			"*[A-Z])(?=.*\\d)" +
			"(?=.*[-+_!@#$%^&*., ?]).+$")

	p = re.compile(regex)
	if (str == None):
		print("No")
		return
    
	if(re.search(p, str)):
		print("Yes")
	else:
		print("No")

str = "#Balaji123@"

isAllPresent(str)

import re
def Check_Vow(string, vowels):
	
	str_list = re.findall(f'[{vowels}]', string, re.I)
	
	print(len(str_list))
	
	return str_list
	
vowels = 'aeiou'
string = "Geeks for Geeks"
print (Check_Vow(string, vowels))


import re

regex = '^[aeiouAEIOU][A-Za-z0-9_]*'
	

def check(string):

	if(re.search(regex, string)):
		print("Valid")
		
	else:
		print("Invalid")
	


if __name__ == '__main__' :
	
	string = "ankit"
	
	check(string)

	string = "geeks"
	check(string)

	string = "sandeep"
	check(string)


