"""
    class
"""
import ParaScript as ps
class OperatorClass(object):
    """
    operator
    """
    def __init__(self,_id):
        self.id = _id
        self.price = 0.0
        self.discount_H = 0.0
        self.time = 0.0
        self.opcost = 0.0
        self.profit = 0.0
        self.fxcost = 0.0
        self.numpas = 0.0
    def set_price(self,_val):
        self.price = _val
    def set_discout(self,_val):
        self.discount = _val
    def cal_opcost(self,_para:ps.ParaClass):
        self.opcost = self.fxcost+_para.opCostPerPas*self.numpas
    def cal_profit(self, _p:ps.ParaClass):
        if self.id ==1:
            self.profit = self.price*self.numpas-self.opcost
        if self.id ==2:
            self.profit = (self.price-_p.la*self.discount_H)*self.numpas-self.opcost
    def set_x(self, _x):
        self.numpas = _x

class UserClass(object):
    """
    class id
    1: use company 1 + 3(without discount)
    2: use company 1 + 2(with discount)
    """  
    def __init__(self,_id):
        self.id = _id
        self.price = 0.0
        self.time = 0.0
        self.cost = 0.0
    def set_price(self,_val):
        self.price = _val
    # def set_dist(self, _val):
    #     self.dist = _val
    def set_time(self, _val):
        self.time = _val
    def cal_cost(self,_para:ps.ParaClass,_op1:OperatorClass,_op2:OperatorClass,_op3:OperatorClass):
        if self.id == 1:
            # self.cost = _op1.price+_op1.time+_para.b*_op1.dist+_op3.cost
            self.cost = _op1.price+_para.vot*_op1.time+_para.vot*_op3.time
        elif self.id == 2:
            # self.cost = _op2.price+_op2.time+_para.b*_op2.dist-_para.la*_op2.discount_H
            self.cost = _op2.price+_para.vot*_op2.time-_para.la*_op2.discount_H
        else:
            print("err in computing generalised cost")

        
  