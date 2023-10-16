class Base:
	def __init__(self):
	   self.firstname="kalai"
	   self.__nickname="chittu"
	   self._lastname="selvi"
	   print("Firstname:",self.firstname)
	   print("Nickname:",self.__nickname)
	   print("Lastname:",self._lastname)
       
class Derived(Base):
	def __init__(self):
	   Base.__init__(self)
	   print("Firstname:",self.firstname)
	   print("Nickname:",self.__nickname)
	   print("Lastname:",self._lastname)

b1=Base()
print("===============")
d1=Derived()
