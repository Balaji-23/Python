list=[]
n=int(input("Enter the number:"))
for i in range(0,n):
    elemt=int(input())
    list.append(elemt)
print(list)
print(5 in list)
print(6 in list)
print(4 not in list)












    
    
   







   
    
    
'''   



a=[1,2,3,4,5,6,0,8,6,5,4,3,2]
print(list(set(a)))
print(type(a))




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
if(number %2==0):                          #1.check number is even or odd
   print("Number is even")
else:
    print("Number is odd") 
    
tuple=(1,2,3,4,5,6,78)
print(tuple[0:3])
    
    
    letter=input("Enter the letter:")  #check vowel or consonant
if(letter=='a'):
               print("a is a vowel")
elif(letter=='e'):
                 print("e is  a vowel")
elif(letter=='i'):
                 print("i is  a vowel")
elif(letter=='o'):
                 print("o is  a vowel")
elif(letter=='e'):
                 print("u is  a vowel")
else:
    print("The given letter is consonant")
    
    
    

dict={"name":"balaji", "sciencemark":23,
"stdnames":"sundar", "socialmark":22,
"stdntnames":"hari", "mathsmark":24
} 
print(dict)

    
    
    tamil=int(input("Enter the tamil marks:")) #total average pass or fail
english=int(input("Enter the english marks:"))
totalsum=tamil+english
average=totalsum/2
print("Total sum is:" ,totalsum)
print("Average is:" ,average)
if(average>=90):
               print("first class ")
elif(average>=80):
                 print("second class")
elif(average>=70):
                 print("third class")
elif(average>=60):
                 print("fourth class")
else:
    print("fail")
    
    yourname=input("Enter the name:")       #print all the details
mobno=int(input("Enter the mobile number:"))
gender=input("Enter the gender:")
qualification=input("Enter the qualification:")
passedout=int(input("Enter the year passed out:"))
percentage=int(input("Enter the percentage:"))
degreecompleted=int(input("Enter the completed degree or not:"))
print(yourname,mobno,gender,qualification,passedout,percentage,bool(degreecompleted))  

'''