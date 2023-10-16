'''
def number():
    list1=[]
    num=int(input("Enter the num value:"))
    for i in range(1,num+1):
        n=int(input("Enter the n value:"))
        list1.append(n)
    print("the largest number is:",max(list1))
    print("the second largest number is:",sorted(list1)[-2])
number()

def digits():
    listval=[]
    value=int(input("Enter the value:"))
    for z in range(1,value+1):
        v=int(input("Enter the val:"))
        listval.append(v)
    print(listval)
digits()        
'''
def add(a,b):
    return a+b
value=add(2,3)
print("sum is:",value)  
def sub(a,b):
    return a-b
value=sub(4,3)
print("subtract is:",value)  
def mul(a,b):
    return a*b
value=mul(24,5)
print("multiply is:",value)  
def div(a,b):
    return a/b
value=div(20,4)
print("divide is:",value)  

billamount=int(input("Enter the bill amount:"))
print("original amount is:",billamount)
gstamount=(billamount*12/100)/100
print("Gstamount is:",gstamount)
emi=30000
calcemi=emi/12
total=calcemi+billamount
print("total Emi amount the year:",emi)
print("total emi amount per month:",calcemi)
print("emi and bill total amount is:",total)



 
   
