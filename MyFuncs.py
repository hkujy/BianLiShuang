"""
    contain all the functions
"""
from os import times
import ParaScript as ps
import MyClass as mc

def get_x(_para:ps.ParaClass,_op1:mc.OperatorClass,_op2:mc.OperatorClass,_op3:mc.OperatorClass):
    first_bracket = 1/(_para.g**2-_para.m**2)
    second_bracket = _para.m*(_op1.price+_para.vot*_op1.time-_para.a1+_para.vot*_op3.time)
    third_bracket = _para.g*(_op2.price+_para.vot*_op2.time-_para.a2-_para.la*_op2.discount_H)
    x1 = first_bracket*(second_bracket-third_bracket)
    second_bracket = _para.m*(_op2.price+_para.vot*_op2.time-_para.a2-_para.la*_op2.discount_H)
    third_bracket = _para.g*(_op1.price+_para.vot*_op1.time-_para.a1+_para.vot*_op3.time)
    x2 = first_bracket*(second_bracket - third_bracket)
    print("x1={0},x2={1}".format(x1,x2))
    _op1.numpas = x1
    _op2.numpas = x2

def _update_profitAndCost(_p:ps.ParaClass,_op1:mc.OperatorClass,_op2:mc.OperatorClass):
    _op2.cal_opcost(_p)
    _op1.cal_opcost(_p)
    _op1.cal_profit(_p)
    _op2.cal_profit(_p)




