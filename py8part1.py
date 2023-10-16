num=int(input("Enter the fact number:"))
fact=1
for i in range(1,num+1):
        fact=fact*i
print("the factorial of",num,"is",fact)

n=int(input("Enter the number:"))
ans=n
sum1=count=0
while(n>0):
    rem=n%10
    sum1=sum1+rem
    n=n//10
    count=count+1
print("sum of the digits",sum1)
if(ans%sum1==0):
    print("Niven number")
else:
    print("not a niven number")
    
def ispower(x,y):
    count=0
    while(x%y==0):
        x=x//y
        count=count+1
        print(y,"^",count)
    return x==1
print(ispower(64,2))
print(ispower(11,2))

n=int(input("Enter the n value:"))
num=0
number=1
print(num)
print(number)
for i in range(num,n):
    n=num+number
    num=number
    number=n
    print(n)

numberList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ansList = []
for num in numberList :
    if num == 0 or num == 1 :
        continue
    for i in range(2, num // 2 + 1) :
        if num % i == 0 :
            break
    else :
        ansList.append(num)
if len(ansList) :
    print("Prime Number : ",end = "-> ")
    for ans in ansList :
        print(ans, end = ", ")  
else :
    print("No any number from the given list is Prime")