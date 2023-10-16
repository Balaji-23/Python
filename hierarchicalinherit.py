class bank:
	def__init__(self,cid,cname,balance):
	   self.cid=cid
	   self.cname=cname
	   slef.balance=balance

class deposit(bank):
	def__init__(self,cid,cname,balance,depmnt):
	   bank.__init__(self,cid,cname,balance):
	   self.deamnt=deamnt
	def dep_trans(self):
		self.current_balance=self.balance+self.dpmnt
		print("After deposit:",self.current_balance)