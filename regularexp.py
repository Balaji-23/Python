'''
import re

str1=input("Enter the string :")
ans=re.findall("all",str1)
print(ans)

ans=re.finditer("all",str1)
for x in ans:
	print(x)

ans=re.search("all",str1)
print(ans,ans.group())


ans=re.match("best",str1)
print(ans)

ans=re.split("\s",str1)
print(ans)

ans=re.sub("\s","*",str1)
print(ans)

ans=re.subn("/s","*",str1)
print(ans)


'''
import re
str1=input("Enter data:")
pattern1="^[A-Z]"

if(re.search(pattern1,str1)):
    print("Starts with upper case")
else:
    print("Does not starts with uppercase")
