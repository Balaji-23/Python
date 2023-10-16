'''
numbers=int(input("Enter the numbers:"))
for num in range(1,51):
    if num%3==0 and num%5==0:
        print(num,"Accord Matrix")
    elif(num%3==0):
        print(num,"Accord")
    elif(num%5==0):
        print(num,"Matrix")
    else:
        print("wrong")

 break          
divisor:
dividend=int(input("Enter the num:"))
divisor=int(input("Enter the divisor:"))
num=dividend/divisor
print("divisor is:",divisor)
print("dividend is:",dividend)
print("quotient is:",num)

  
mul=int(input("Enter the multiplication table:"))
for multiply in range(1,11,1):
    print(multiply,"*",mul,"=",multiply*mul)
  
  
  
num=str(input("Enter the num:"))
for number in num:
    print(int(number))
       
num=int(input("Enter the number:"))
stop=int(input("Enter the stop value:"))
for number in range(num,stop,-1):
    if(number%2!=0):
        print(number,"the given value is odd")
   
   
count=0
num=[1,2,3,4,5]
for x in num:
    if(x==5):
        count+=1
print("number of occurences for the given number is:",count)

li=[12,3,4,5,6,7]
li[1]="##"
print(li)
    
li=[1,2,3,4,5,6,7]
print(li)
li.append(8)
print(li)
li.remove(7)
print(li)

tuple=(1,2,3,4,6,7)
tu=tuple.count(7)
print(tu)


list=[]
d=(int(input("Enter the d value:")))
for li in range(0,d):
    ele=int(input())
    list.append(ele)
    print(list)
l=list[::-1]
print(l)
'''

li=[23,45,6,7,8,9]
del li
print(li)