'''
k = 1
for i in range(0, 4):
    for j in range(0, i+1):
        print(k, end=" ")
        k = k + 1
    print()
    
    
def pattern(n):
      k = 2 * n - 2
      for i in range(0,n):
           for j in range(0,k):
               print(end=" ")
           k = k - 1
           for j in range(0, i+1):
                print("*", end=" ")
           print("\r")
 
pattern(5)

n = int(input("Enter number of lines of pattern: "))

for i in range(1,n+1):
    for j in range(1, i+1):
        print(j%2, end="")
    print()
'''    
n=int(input())
odd_even=lambda n:"Even number" if(n%2==0) else "Odd number"
print(odd_even(n))
    