"""
    contain all the functions
"""
from os import times
import ParaScript as ps
import MyClass as mc

def get_x(_p:ps.ParaClass,_op1:mc.OperatorClass,_op2:mc.OperatorClass,_op3:mc.OperatorClass):
    first_bracket = 1/(_p.g**2-_p.m**2)
    second_bracket = _p.m*(_op1.price+_p.b*_op1.dist+_op1.time-1+_op3.timecost)
    third_bracket = _p.g*(_op2.price+_p.b*_op2.dist+_op2.time-1-_p.la*_op2.discount_H)
    x1 = first_bracket*(second_bracket-third_bracket)
    second_bracket = _p.m*(_op2.price+_p.b*_op2.dist+_op2.time-1-_p.la*_op2.discount_H)
    third_bracket = _p.g*(_op1.price+_p.b*_op1.dist+_op1.time-1+_op3.timecost)
    x2 = first_bracket*(second_bracket - third_bracket)
    print("x1={0},x2={1}".format(x1,x2))
    _op1.numpas = x1
    _op2.numpas = x2

def _update_profitAndCost(_p:ps.ParaClass,_op1:mc.OperatorClass,_op2:mc.OperatorClass):
    _op2.cal_opcost(_p)
    _op1.cal_opcost(_p)
    _op1.cal_profit(_p)
    _op2.cal_profit(_p)




