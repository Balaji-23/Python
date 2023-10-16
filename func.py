#function without arguments without return type
def fun():
    a=10
    b=20
    d=a+b
    print(d)
fun()
fun()

#function with arguments without return type
def fun(a,b):
	c=a+b
	print(c)
fun(2,3)
fun(5,5)

#function with arguments with return type
def add(c,e):
    total=c+e
    average=total/2
    return average
name,v=add(2,3)
print("name is:",name)
print("value is:",v)