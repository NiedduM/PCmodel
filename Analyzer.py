import matplotlib.pyplot as plt
import numpy as np
import pickle as pk
import pandas as pd
from IPython.display import display

class Analyzer():

    def __init__(self):
        
        self.simulations = pk.load(open('6 objectSwarmObserverAgents_AESOP_turtleLib_NetworkX/SIMmodel/simulation_data/dbSimulation', 'rb'))
        display(self.simulations)
        
    def loadSimulation(self, fileName):
        
        name = '6 objectSwarmObserverAgents_AESOP_turtleLib_NetworkX/SIMmodel/simulation_data/' + fileName
        self.db = pk.load(open(name, 'rb')  )
        self.db.columns = ['Id', 'Sector', 'Period', 'C', 'G','WB','T','H' ]
        
        
    def showTFmatrixComplete(self):
        
        display(self.db.groupby(['Period' ,'Sector' ]).sum()[ ['C', 'G','WB','T','H']].transpose())

        
    def showTFmatrix(self, period = 0):
        
        display(self.db[self.db.Period == period].groupby([ 'Sector' ]).sum()[ ['C', 'G','WB','T','H']].transpose())
        
    def printTable(self):
        
        self.table = self.db[self.db.Sector == 'Household'].groupby(['Period'])[['WB','C','H', 'T']].sum()
        display(self.table.abs().transpose())
        
    
    
    def wealthDistribution(self, period = 0):
        
        dbNew = self.db[self.db.Period == period]
        distributionH = np.array(dbNew[dbNew.Sector == 'Household'].H)
        plt.hist(distributionH)
        plt.show()
        print('H mean = ', distributionH.mean())
        print('dev std = ', distributionH.std())
