class TFmatrix():

	def __init__(self):

		self.C = 0
		self.G = 0
		self.WB = 0
		self.T = 0
		self.H = 0

	def updateConsumption(self, x):

		self.C += x

	def updateGovernmentExpenditures(self, x):

		self.G += x

	def updateWages(self, x):

		self.WB += x

	def updateTaxes(self, x):

		self.T += x

	def updateMoneyDep(self, x):

		self.H += x

	def sumTFM(self,tfM):

		ret = TFmatrix()
		ret.C = self.C + tfM.C
		ret.G = self.G + tfM.G
		ret.WB = self.WB + tfM.WB
		ret.T = self.T + tfM.T
		ret.H = self.H + tfM.H
		return ret

	def listify(self):
		return[self.C ,self.G ,self.WB, self.T, self.H]

	def show(self):

		print('C = ', self.C)
		print('G = ', self.G)
		print('WB = ', self.WB)
		print('T = ', self.T)
		print('H = ', self.H)


