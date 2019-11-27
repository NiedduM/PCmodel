from Tools import *
from Agent import *
from Eagent import *
from Govern import *
from WorldState import *
import commonVar as common
import pickle as pk
import datetime as dt

def do1b(address):
    pass


def do2a(address, cycle):
    pass


def do2b(address, cycle):
    pass

def otherSubSteps(subStep, address):
    return False

def showResultOLD(address):

	self = address
	Hg = 0
	T = 0
	C = 0
	for ag in address.modelSwarm.agentList:
		if(type(ag) == Govern):
			G = ag.consumption
			Hg = ag.cash
			T = ag.consumption + Hg
		else:
			C += ag.consumed

	print('Y  ', C + G)
	print('T  ', T)
	print('C  ', C)
	print('H  ', Hg)

	fi = open('SIMmodel/Pickleprove', 'wb')

	db = address.modelSwarm.worldState.db
	pk.dump(db,fi)








def showResult(address):

	self = address

	try:
		myfile = open('SIMmodel/simulation_data/dbSimulation','rb')
			
	except BaseException:

		print('dbSimulation file does not exist. Creating now...')
		DBcreation()
		print('created')
		myfile = open('SIMmodel/simulation_data/dbSimulation','rb')
			

	downloadedDB = pk.load(myfile)

	fileName = 'SIMsimulation'
		
	index = 0
	if(len(downloadedDB) > 0):
		index = downloadedDB.index[-1] + 1
		
	fileName = fileName + str(index)
	fi = open('SIMmodel/simulation_data/' + fileName, 'wb')
	db = address.modelSwarm.worldState.db
	pk.dump(db,fi)
	fi.close()

	myfile.close()

	data = str(dt.datetime.now())


	myfile = open('SIMmodel/simulation_data/dbSimulation','wb')

	downloadedDB.loc[index] = [data, fileName, common.G, common.taxRate, common.alpha1, common.alpha2, common.numberOfPeriods, common.periodLength, common.numberOfAgent, common.wGlabel, common.sGlabel, common.heterogeneity ]
	
	pk.dump(downloadedDB, myfile)

	print('Salvataggio effettuato')


def DBcreation():

	myfile = open('SIMmodel/simulation_data/dbSimulation','wb')

	DBsimulation = pd.DataFrame(columns=  ['Date', 'File name', 'G','taxRate', 'alpha1', 'alpha2', 'Periods', 'Period length',  'Number of agents', 'Workers graph', 'Sellers graph', 'Heterogeneity'])

	pk.dump(DBsimulation, myfile)

	myfile.close()

		
		


