def calc(name, *marks):
	print("name is:",name)
	print("marks is:",marks)
	print("total is:",sum(marks))
	print("average is:",sum(marks)/len(marks))
calc("balaji",23,4,5,889,6,7)

def fact(number):
    if number==0 or number==1:
        return 1
    else:
        return (number*fact(number-1))

print("Factorial value is:",fact(5))

def sum(n):
    if n<10:
        return n
    else:
        return n%10 +sum(n/10)
number=int(input("Enter the number:"))
total=sum(number)
print(number,total)