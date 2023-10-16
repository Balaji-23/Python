

'''
amount=int(input("Enter the amount:"))
print("product amount is:",amount)
gst=amount*4.5/100
print("gst amount is:",gst)
totalamount=amount+gst
print("total product value is:",totalamount)
userpaidamount=int(input("Enter the userpaidamount:"))
print(userpaidamount)
balanceamount=userpaidamount-totalamount
print(balanceamount)

number=int(input("Enter the number:"))
if number%2==0 and number%4!=0:
   print("Either one condition or both conditions are true ")

else:
    print("Either one condition or both conditions are false")
    
    23 f t  false
    22 t  t t 
    
    
a=int(input("Enter the a value:"))
b=int(input("Enter the b value:"))
c=int(input("Enter the c value:"))
if(a>b):
    print("the number a is a greater")
if(b<c):
    print("the number c is a greater")
else:
    print("b is greater")
 
def pairofnumbers(lst,k):
    res=[]
while lst:
    num=lst.pop()
    diff=k-num
    if diff in lst:
        res.append((diff.num))
        res.reverse()
        return res
lst=[1,5,3,7,9]
k=12
print(pairofnumbers(lst,k))
'''
name=input("Enter the name:")
n=input("Enter the nam:")
if(len(str1)==len(str2)):
	if(sorted(str1)==sorted(str2)):
		print("Both string are anagram")
    else if:
        print("Both Strings length are equal but not anagram")
else:
    print("Strings length are not equal")

import csv
def write():
    ch="y"
with open("userinfo1.csv","w")as f:
wo=csv.writer(f)
wo.writerow(["username","emailid","phone number","dob"])
while True:
user_name=input("enter the username:")
mailid=input("enter the mailid:")
phonenumber=int(input("enter the phone number:"))
dob=(input("enter the dob:"))
data=[user_name,mailid,phonenumber,dob]
wo.writerow(data)
ch=input("do you want to enter the more records(y/n)")
if ch in & 'Nn':
    break
def read():
with open("userinfo1.csv","r")as f:
ro=csv.reader(f)
for i in ro:
print(i)
write()
read()

import csv
reader = csv.reader(open("userinfo1.csv"))
for row in reader:
print(row)