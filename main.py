"""
    main func
"""

from numpy.lib.shape_base import tile
import ParaScript as ps
import MyClass as mc
import MyFuncs as mf
import matplotlib.pyplot as plt


if __name__ == '__main__':
    """
    main
    """
    # step 1: set the unchanged parametersa
    x1_list = []
    x2_list = []
    op1_profit = []
    op2_profit = []
    op1_cost = []
    op2_cost = []

    para = ps.ParaClass()
    op1 = mc.OperatorClass(_id = 1)
    op2 = mc.OperatorClass(_id = 2)
    op3 = mc.OperatorClass(_id = 3)

    # price of the two company 
    op1.price = 0.5
    op2.price = 0.5
    # distance of the two company 
    op1.dist = 0.2
    op2.dist = 0.1
    # travel time of the two companies
    op1.time = 0.0
    op2.time = 0.0
    # travel timecos of the third company 
    op3.timecost = 0.1
    op2.discount_H = op1.dist-op2.dist

    for i in range(0,20):
        para.la = 0.05*(i+1)
        if op2.price-para.la*op2.discount_H<0:
            print("error: the op2 price after discout is negative")
            input()
        mf.get_x(para,op1,op2,op3)
        mf._update_profitAndCost(para,op1,op2)
        x1_list.append(op1.numpas) 
        x2_list.append(op2.numpas)
        op1_profit.append(op1.profit)
        op2_profit.append(op2.profit)
        op1_cost.append(op1.opcost)
        op2_cost.append(op2.opcost)
        print("p1={0},p2={1}".format(op1_profit,op2_profit))
    # plt.plot(op2_profit)
    # plt.ion()
    # plt.pause(2)
    # plt.close()
    # plt.plot(op1_profit)
    # plt.ion()
    # plt.pause(2)
    # plt.close()
    plt.plot(x1_list)
    plt.title("x1")
    plt.ion()
    plt.pause(2)
    plt.close()
    plt.plot(x2_list)
    plt.title("x2")
    plt.ion()
    plt.pause(2)
    plt.close()
    # step 3: plot
