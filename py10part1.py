file=open("mydoc.txt","r")
count=0
for line in file:
    words=line.split("")
    count+=len(words)
    file.close()
print("number of words in a mydoc:",count)


f=open()
name=input("enter the name")
qualification=input("enter the qualification")
passedout=input("enter the passedout")
f.write("Name:"+name+"\n")
f.write("Qualification:"+qualification+"\n")
f.write("passedout:"+passedout+"\n")
f.close()
f=open("username.txt","r")
ans=f.read()
print(ans)

class Reverse:
    def __init__(self, filename):
file = open(filename,"r" )
self.file_text = file.read()
file.close()

def get_reverse(self):
rev_file_text = .join(reversed(self.file_text))
return rev_file_text

def main():
filename = input("Enter filename:")
obj = Reverse(filename)
rev_contents = obj.get_reverse()
print(rev_contents)

if __name__ =="__main__":
main()