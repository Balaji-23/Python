class circle:
    def perimeter(self,r):
        self.r=r
        peri=2*3.14*r
        print("perimeter of the circle:",peri)
    def area(self,rad):
        self.rad=rad
        are=3.14*rad*rad
        print("area of the circle:",are)
cir=circle()
cir.perimeter(2)
cir.area(4)  

class employee:
    def task(self,num):
        self.num=num
        print("asar task completed:",num)
        
    def remaining(self,number):
        self.number=number
        print("remaining is:",number)
        
e=employee()        
e.task(5)
e.remaining(6)


class student:
    def studentname(self):
        scimarks=int(input("Enter the science marks:"))
        socmarks=int(input("Enter the social marks:"))
        sumofmarks=scimarks+socmarks
        avgmarks=sumofmarks/2
        print("Sum of marks are:",sumofmarks)
        print("average of marks are:",avgmarks)
        
stu=student()
stu.studentname()
        
 
class temperature:
    def celtofahr(self):
        celcius=15
        farenheit=(celcius*9/5)+32
        print("celcius to farenheit is:",farenheit)
    def fahrtocel(self):
        farenheit=60
        celcius=(farenheit-32)*5/9
        print("celcius to farenheit is:",celcius)
t=temperature()
t.celtofahr()    
t.fahrtocel()
    
        
        