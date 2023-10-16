n="balaji"
for i in n:
    if n.count(i)==1:
        c=i
    break   
print("non repeating word:",c)

name=input("Enter the name:")
for i in name.split():
    print(name[::-1])
    
name="        hi this is balaji"
print(name.strip())
    
n="balaji"
print(n.upper())
print(n.lower())    
    
str=input("Enter the string:")
vowels=0
consonant=0
for i in str:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        vowels=vowels+1
    else:
        consonant=consonant+1
print("number of vowels:",vowels)
print("number of consonants :",consonant)

