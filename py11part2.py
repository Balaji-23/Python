import re
def rem_vowel(string):
    return (re.sub("[aeiouAEIOU]","",string))           

string = "Balaji"
print(rem_vowel(string))


import re
str1 = "A"
str2 = "b"

print("Checking if the string '",str1,"' is uppercased or not")
print(bool(re.match('[A-Z]', str1)))

print("Checking if the string '",str2,"' is uppercased or not")
print(bool(re.match('[A-Z]', str2)))


import re
string = 'trs'
res = re.findall(r'[a,e,i,o,u]', string)
print("the given string contains vowel")