'''tamil=int(input("Enter the tamil mark:"))
english=int(input("Enter the english mark:"))
maths=int(input("Enter the maths mark:"))
science=int(input("Enter the science mark:"))
social=int(input("Enter the social mark:"))
total=tamil+english+maths+science+social
average=total/5
print("Total is:",total)
print("Average is:",average)
if(average>=75):
    print("Distinction")
elif(average>=60):
    print("First class")
elif(average>=50):
    print("second class")
elif(average<50):
    print("fail")
    
num=int(input("Enter the num:"))
if(num>0):
    print("Number is positive")
elif(num==0):
    print("number is neither positive nor negative")
else:
    print("Number is Negative")
    



number=int(input("Enter the number:"))
if number%2==0 and number%4!=0:
   print("first condition true ")
elif():
    print("second condition is true")
else:
    print("one is true and another one is false")
    
    #or- t t t  f t t  t f t  f f f
    #And-t f f  f t f  t t t  f f f
    '''
a=int(input("Enter the a value:"))
if(a<=100):
	print("Free")
elif(a>101 and a<=200):
	val=0.80*a
elif(a>201and a<=300):
	val=1*a
elif(a>301 and a<=400):
	val=1.20*a
elif(a>400):
	val=2*a
print("a value is:",a)
print("val is:",val)

