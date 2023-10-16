ans=lambda a,b,c:(a+b)*c
print(ans(1,2,3))

check=lambda a,b:"a is big" if(a>b) else "b is big"
print(check (2,3))

mylist=[1,2,3,4,5,6,7,8,9,10]
ans=list(map(lambda x:x*5,mylist))
print(ans)