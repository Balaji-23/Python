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