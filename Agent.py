from Tools import *
from agTools import *

class Agent(SuperAgent):

	def __init__(self,number, myWorldState,  agType, lX=-20, rX=19, bY=-20, tY=19):
        # the environment
		self.number = number
		self.lX = lX
		self.rX = rX
		self.bY = bY
		self.tY = tY
		if myWorldState != 0:
		    self.myWorldState = myWorldState
		self.agType = agType
		self.agOperatingSets = []
		
