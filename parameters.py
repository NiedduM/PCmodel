# parameters.py
from Tools import *
import commonVar as common
import networkx as nx

def loadParameters(self):

    # Projct version
    try:
        projectVersion = str(common.projectVersion)
    except BaseException:
        projectVersion = "Unknown"
    print("\nProject version " + projectVersion)

    #seed of random
    mySeed = 2#eval(input("random number seed (1 to get it from the clock) "))
    if mySeed == 1:
        random.seed()
    else:
        random.seed(mySeed)

    #other instruction necessary to SLAPP
    self.nAgents = 0 
    self.worldXSize = 50
    self.worldYSize = 50


    #simulation data
    common.numberOfPeriods = eval(input('How many reference period?'))
    common.periodLength = eval(input('How many iteration for period?'))
    self.nCycles = common.numberOfPeriods*common.periodLength


    writeSchedule()

    common.numberOfAgent = eval(input('How many agents?'))
    writeAgentsFile()
    common.heterogeneity = eval(input('Heterogeneity? (default = False)'))
    if(common.heterogeneity):
        common.noise = eval(input('Noise level?'))

    N = common.numberOfAgent
    p = 2/N
    ps = 0.2

    caso = eval(input('Which graphs for working relation? (1. Complete, 2. Erdos-Renyi, 3. Barabasi-Albert)'))
    if(caso ==3):
        common.workersGraph = nx.barabasi_albert_graph(N, 5, seed=None)
        common.wGlabel = 'BA'
    if(caso ==2):
        common.workersGraph = nx.erdos_renyi_graph(N, p, directed= True)
        common.wGlabel = 'erdos'
    if(caso == 1):
        common.workersGraph = nx.complete_graph(N)
        common.wGlabel = 'complete'
    if(caso != 1 and caso != 2 and caso != 3):
        print('case not valid')
        

    common.sellersGraph = nx.complete_graph(N) #erdos_renyi_graph(N,ps, directed = True)
    common.sGlabel = 'complete'
    print(common.workersGraph.nodes())


def writeAgentsFile():

    agentsFile = open('SIMmodel/tasteA.txt', 'w')
    for i in range(common.numberOfAgent):

        #initial instructions
        agentsFile.write(str(i) + "\n")
    agentsFile.close()
    
    govFile = open('SIMmodel/tasteB.txt','w')
    govFile.write(str(common.numberOfAgent))



def writeSchedule():


    first = ['tasteB consume', 'tasteA payWages','tasteA payTaxes', 'tasteA consumeFromCash']
    normal = ['tasteA consume','tasteA deposit','tasteA payWages','tasteA payTaxes']
    end = ['tasteA deposit', 'all write_on_DB', 'WorldState computationalUse updatePeriod','all resetTFM']
    
    myfile = open('SIMmodel/schedule.txt', 'w')
    
    for period in range(common.numberOfPeriods):

        #initial instructions
        myfile.write('# '+ str(period*common.periodLength+1) + "\n")
        if(period == 0):
            myfile.write('all createList'+ "\n")
        for instruction in first:
            myfile.write(instruction + "\n")
        for instruction in normal:
            myfile.write(instruction + "\n")

        for t in range(1,common.periodLength):
            myfile.write('# '+ str(period*common.periodLength + 1 + t) + "\n")
            for instruction in normal:
                myfile.write(instruction + "\n")

        #end of period instructions
        for instruction in end:
            myfile.write(instruction + "\n") 









