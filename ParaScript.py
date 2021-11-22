"""
    Define the parameters
"""

class ParaClass(object):
    def __init__(self):
        self.opCostPerPas = 0.0
        self.val_of_time = 0.02 # value of travel time
        self.discount_ratio= 0.1
        self.m = 0.5
        # self.g = -0.5
        self.g = -0.2
        self.a1 = 120
        self.a2  = 100
        self.price = []
        self.travel_time = []
        self.distance=[]
        self.fxcost=[]
        pass