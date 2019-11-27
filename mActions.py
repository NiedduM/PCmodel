from Agent import *
from Eagent import *
from Govern import *
import numpy as np
import os


def do0(address):
    self = address  # if necessary
    askEachAgentInCollection(address.agentList, Agent.setNewCycleValues)


def do1(address):
    self = address  # if necessary
    pass


def createTheAgent(self, line, num, agType):
    # explictly pass self, here we use a function

    if len(line.split()) == 1:  # weak control, can be improved
        anAgent = Agent(
            num,
            self.worldState,
            random.randint(
                self.leftX,
                self.rightX),
            random.randint(
                self.bottomY,
                self.topY),
            self.leftX,
            self.rightX,
            self.bottomY,
            self.topY,
            agType=agType)
        self.agentList.append(anAgent)

    else:
        print("Error in file " + agType + ".txt")
        os.sys.exit(1)


def createTheAgent_Class(self, line, num, agType, agClass):
    # explictly pass self, here we use a function

    # check if the file having the content of agClass and extension
    # .py exists

    common.agClassVerified = False
    if not common.agClassVerified:
        try:
            exec("import " + agClass)
            common.agClassVerified = True
        except BaseException:
            print("Missing file " + agClass + ".py")
            os.sys.exit(1)

    print(agClass)

    alpha1 = common.alpha1
    alpha2 = common.alpha2

    if(common.heterogeneity): 
        alpha1 += common.noise*np.random.uniform(-0.5,0.5)     #normal(loc=common.alpha1 ,scale=common.alpha1/10)
        alpha2 += common.noise*np.random.uniform(-0.5,0.5)

    govCons = common.G
    taxRate = common.taxRate
    workerList = []
    sellerList = []
    if(agType == 'tasteA'):
        workerList = [wk for wk in common.workersGraph.neighbors(num)]
        sellerList = [sl for sl in common.sellersGraph.neighbors(num)]
    print('wk list of agent n.', num, ' = ' , workerList)

    # first step in exec:
    # access the files of the classes to create the instances
    # N.B. to simplify the structure of SLAPP, the name of the
    # class and the name of the file containing it, have to be the same.
    if len(line.split()) >= 1:  # weak control, can be improved
        try:
            space = {
                'num': num,
                'sW': self.worldState,
                'random': random,
                'leftX': self.leftX,
                'rightX': self.rightX,
                'bottomY': self.bottomY,
                'topY': self.topY,
		'cash': 0,
		'alpha1': alpha1,
		'alpha2': alpha2,
		'workerList': workerList,
		'sellerList': sellerList,
		'consumption': govCons,
		'taxRate' : taxRate,	
                'agType': agType}

            if(agClass == 'Eagent'):
                exec("from " + agClass + " import *;" +
                 "anAgent = " + agClass + "(num, sW," +
		 "cash," +
		 "alpha1," +
		 "alpha2," +
		 "workerList," +
		 "sellerList," +
                 "agType=agType)", space)


            elif(agClass == 'Govern'):
                exec("from " + agClass + " import *;" +
                 "anAgent = " + agClass + "(num, sW," +
		 "cash," +
		 "consumption," +
		 "taxRate," +
                 "agType=agType)", space)
            anAgent = space['anAgent']
            self.agentList.append(anAgent)

        except BaseException:
            print("Argument error creating an instance of class", agClass)
            os.sys.exit(1)

def otherSubSteps(subStep, address):
    return False
