from Agent import*
from Eagent import*
from TFmatrix import*

class Govern(Agent):

	def __init__(self,number, myWorldState,cash, consumption, taxRate, agType , lX=-20, rX=19, bY=-20, tY=19):
	
		Agent.__init__(self,number, myWorldState, agType, lX=-20, rX=19, bY=-20, tY=19)

		self.cash = cash
		self.consumption = consumption
		self.taxRate = taxRate

		self.TFM = TFmatrix()


	def createList(self):
		self.eagentList = []
		#print('createList method of gov', self.number)
		for ag in self.agentList:
			if(ag.agType == 'tasteA'):
				self.eagentList.append(ag)
		#print(len(self.eagentList))


	def consume(self):
		demanded = self.consumption/len(self.eagentList)
		#print('gov consumption', demanded)
		for ag in self.eagentList:
			ag.sell(demanded, True)
		self.cash -= self.consumption
		self.TFM.updateGovernmentExpenditures(-self.consumption)
		self.TFM.updateMoneyDep(-self.consumption)

	def receiveTaxes(self, T):
		self.cash += T
		self.TFM.updateTaxes(T)
		self.TFM.updateMoneyDep(T)
		#aggiorna T in matrice TF


	def write_on_DB(self):

		lista = [self.number, 'Government', self.myWorldState.period]
		lista += self.TFM.listify()
		self.myWorldState.insertNewEntry(lista)

	def resetTFM(self):

		self.TFM = TFmatrix()
