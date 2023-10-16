class banking:
	def interest(self):
		balance=int(input("Enter the balance amount:"))
		if balance > 25000:
			accountbalance=balance*6.5*100
			print(accountbalance)
bank=banking()
bank.interest()