
num=int(input("Enter the num value:"))
stop=int(input("Enter the stop value:"))
for i in range(num,stop,-1):
	print(i)
	
dictvalues={"name":"Balaji","age":23,"number":98765543}
print(dictvalues)
print(dict(sorted(dictvalues.items())))
print(sorted(dictvalues.keys()))

val={"name":"livaiz","age":24}
print(list(val.items()))

val={23445:"balaji",87665:"arun",6364335:"livaiz",4523847:"maha",98798:"hari"}
print(val.values())
print(val.clear())