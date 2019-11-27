from Agent import *
from Govern import *
from TFmatrix import *

class Eagent(Agent):

	def __init__(self,number, myWorldState, cash, alpha1, alpha2, workerList, sellerList, agType ,lX=-20, rX=19, bY=-20, tY=19, income = 0, sold=0):

		Agent.__init__(self,number, myWorldState, agType, lX=-20, rX=19, bY=-20, tY=19)

		self.cash = cash
		self.alpha1 = alpha1
		self.alpha2 = alpha2
		self.workersList = workerList
		self.sellerList = sellerList
		self.income = 0
		self.sold = 0
		self.consumed = 0
		self.householdTFM = TFmatrix()
		self.producerTFM = TFmatrix()

	def createList(self):
		#print('createList method of n.', self.number)

		for ag in self.agentList:
			if(ag.agType == 'tasteB'):
				self.govern = ag
				break

		wkProvv = []
		slProvv = []
		# when Eagent is created, worker and sellers lists are lists of number. Here the lists are converted in lists of agent
		for ag in self.agentList:
			if(ag.number in self.workersList):
				wkProvv.append(ag)
			if(ag.number in self.sellerList):
				slProvv.append(ag)

		self.workersList = wkProvv
		self.sellerList = slProvv
		#print(self.workersList)
		if(len(self.workersList) == 0):
			print('Workers list is empty, I am choosing at random')
			ag = self.agentList[0]
			while(ag.agType == 'tasteB'):
				ag = self.agentList[0]  #SLAPP reshuffle agent list every time it is acessed
			self.workersList.append(ag)


		if(len(self.sellerList) == 0):
			print('Sellers list is empty, I am choosing at random')
			ag = self.agentList[0]
			while(ag.agType == 'tasteB'):
				ag = self.agentList[0]  #SLAPP reshuffle agent list every time it is acessed
			self.sellerList.append(ag)



	# as household
	def reciveWage(self,wage):

		self.income += wage
		#print('n. ', self.number ,'wage received ', self.income)
		self.householdTFM.updateWages(wage)

	def payTaxes(self):
		T = self.govern.taxRate*self.income
		self.govern.receiveTaxes(T)			
		self.income -= T
		self.householdTFM.updateTaxes(-T)

	def consume(self):
		#print('n.', self.number, 'I am consuming')
		if(self.income > 0.00001):	#
			c = self.alpha1*self.income
			self.income -= c
			self.consumed += c
			self.householdTFM.updateConsumption(-c)
			#select a seller at random
			i = random.randint(0,len(self.sellerList)-1)
			self.sellerList[i].sell(c, gov = False)
		 

	def consumeFromCash(self):
		if(self.cash >0):
			c = self.alpha2*self.cash
			self.cash -= c
			self.consumed += c
			i = random.randint(0,len(self.sellerList)-1)
			self.sellerList[i].sell(c, gov = False)
			self.householdTFM.updateConsumption(-c)
			self.householdTFM.updateMoneyDep(-c)

	def deposit(self):
		self.cash += self.income
		self.householdTFM.updateMoneyDep(self.income)
		self.income = 0

	# as producer
	def sell(self, demanded,gov):
		self.sold += demanded
		#print('I, n.', self.number, 'am reciving ', demanded)
		if(gov):
			self.producerTFM.updateGovernmentExpenditures(demanded)
		else:
			self.producerTFM.updateConsumption(demanded)



	def payWages(self):
#		if(self.workersList == []):
#			self.workersList.append(self)
		self.producerTFM.updateWages(-self.sold)
		wage = self.sold/len(self.workersList)
		#print(wage)
		for ag in self.workersList:
			ag.reciveWage(wage)
		self.sold = 0



	def showTFM(self):

		print('My household matrix')
		self.householdTFM.show()
		print('My producer matrix')
		self.producerTFM.show()



	def resetTFM(self):

		self.householdTFM = TFmatrix()
		self.producerTFM = TFmatrix()



	def write_on_DB(self):

		lista = [self.number, 'Household', self.myWorldState.period]
		lista += self.householdTFM.listify()
		self.myWorldState.insertNewEntry(lista)

		lista2 = [self.number, 'Producer', self.myWorldState.period]
		lista2 += self.producerTFM.listify()
		self.myWorldState.insertNewEntry(lista2)


