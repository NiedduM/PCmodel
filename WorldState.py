# WorldState.py
from Tools import *
from TFmatrix import *
import numpy as np
import pandas as pd
from Eagent import *
from Govern import *
from WorldState import *

class WorldState(object):
	def __init__(self):

		self.db = pd.DataFrame()
		self.period = 0


	def updatePeriod(self):

		self.period+= 1


	def insertNewEntry(self,lista):

		self.db = self.db.append([lista], ignore_index= True)



			
