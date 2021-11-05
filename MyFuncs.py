"""
    contain all the functions
"""
from os import times
import ParaScript as ps
import matplotlib.pyplot as plt

class OperatorClass(object):
    """
    operator
    """

    def __init__(self, _id):
        self.id = _id
        self.price = 0.0
        self.discount = 0.0
        self.time = 0.0
        self.opcost = 0.0
        self.profit = 0.0
        self.fxcost = 0.0
        self.numpas = 0.0

    def set_price(self, _val):
        self.price = _val

    def cal_opcost(self, _para: ps.ParaClass()):
        self.opcost = self.fxcost+_para.opCostPerPas*self.numpas

    def cal_profit(self, _para: ps.ParaClass()):
        if self.id == 1:
            self.profit = self.price*self.numpas-self.opcost
        if self.id == 2:
            self.profit = (self.price-self.discount)*self.numpas-self.opcost

# class UserClass(object):
#     """
#     class id
#     1: use company 1 + 3(without discount)
#     2: use company 1 + 2(with discount)
#     """

#     def __init__(self, _id):
#         self.id = _id
#         self.price = 0.0
#         self.time = 0.0
#         self.cost = 0.0

#     def set_price(self, _val):
#         self.price = _val
#     # def set_dist(self, _val):
#     #     self.dist = _val

#     def set_time(self, _val):
#         self.time = _val

#     def cal_cost(self, _para: ps.ParaClass(), _op):
#         if self.id == 1:
#             # self.cost = _op1.price+_op1.time+_para.b*_op1.dist+_op3.cost
#             self.cost = _op[0].price+_para.val_of_time * _op[0].time+_para.val_of_time*_op[2].time
#         elif self.id == 2:
#             # self.cost = _op2.price+_op2.time+_para.b*_op2.dist-_para.la*_op2.discount_H
#             self.cost = _op[1].price+_para.val_of_time * _op[1].time-_op[1].discount
#         else:
#             print("err in computing generalised cost")


def get_discont_val(t1, t2, _para):
    """
        a general function to compute the discout value
        input: travel time of the two companies 
    """
    val = _para.discount_ratio*(t1 - t2)
    if val < 0:
        input(
            "The travel time of company op2 is greater than op 1, need to further examine")
    return val


def get_x(_para: ps.ParaClass, _op):
    """
        compute the value of x1 and x2 based on the formulation
    """
    first_bracket = 1/(_para.g**2-_para.m**2)
    second_bracket = _para.m * (_op[0].price+_para.val_of_time*_op[0].time - _para.a1+_para.val_of_time*_op[2].time)
    third_bracket = _para.g * (_op[1].price+_para.val_of_time*_op[1].time-_para.a2-_op[1].discount)
    x1 = first_bracket*(second_bracket-third_bracket)
    second_bracket = _para.m * (_op[1].price+_para.val_of_time*_op[1].time- _para.a2-_op[1].discount)
    third_bracket = _para.g * (_op[0].price+_para.val_of_time*_op[0].time - _para.a1+_para.val_of_time*_op[2].time)
    x2 = first_bracket*(second_bracket - third_bracket)
    _op[0].numpas = x1
    _op[1].numpas = x2


def update_ProfitAndCost(_p: ps.ParaClass, _op):
    # step 1: compute the operation cost
    _op[0].cal_opcost(_p)
    _op[1].cal_opcost(_p)
    # step 1: compute the profit
    _op[0].cal_profit(_p)
    _op[1].cal_profit(_p)


def test_one_ParaSet(case_id: int, _para: ps.ParaClass()):
    """
        calculate one combination of parameters
    """
    x1_list = []
    x2_list = []
    total_demand = []
    discount = []
    op1_profit = []
    op2_profit = []
    op1_cost = []
    op2_cost = []
    operators = []
    operators.append(OperatorClass(_id=1))
    operators.append(OperatorClass(_id=2))
    operators.append(OperatorClass(_id=3))
    # price of the two companies
    operators[0].price = _para.price[0]
    operators[1].price = _para.price[1]
    # travel time of the two companies
    operators[0].time = _para.travel_time[0]
    operators[1].time = _para.travel_time[1]
    # travel timecos of the third company
    operators[2].time = _para.travel_time[2]


    for i in range(0, 10):
        _para.discount_ratio = 0.05*(i+1)
        operators[1].discount = get_discont_val(
            operators[0].time, operators[1].time, _para)
        discount.append(operators[1].discount)
        if operators[1].price - operators[1].discount < 0:
            print("error: the op2 price after discout is negative")
            input()
        get_x(_para, operators)
        print("{0},{1}".format(operators[0].numpas,operators[1].numpas))
        update_ProfitAndCost(_para, operators)
        x1_list.append(operators[0].numpas)
        x2_list.append(operators[1].numpas)
        total_demand.append(operators[0].numpas + operators[1].numpas)
        op1_profit.append(operators[0].profit)
        op2_profit.append(operators[1].profit)
        op1_cost.append(operators[0].opcost)
        op2_cost.append(operators[1].opcost)

    for i in range(0,len(x1_list)):
        with open('TestResults.txt', 'a') as f:
        # print("TestId,Price1,Price2,Time1,Time2,Time3,DiscountRatio,m,g,x1,x2,profit1,profit2,opCost1,opCost2",file=f)
            print("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14}".format
            (case_id,_para.price[0],_para.price[1],_para.travel_time[0],_para.travel_time[1],_para.travel_time[2],
            _para.discount_ratio,_para.m,_para.g,x1_list[i],x2_list[i],op1_profit[i],op2_profit[i],
            op1_cost[i],op2_cost[i]),file=f)
 
    # plt.plot(op2_profit)
    # plt.ion()
    # plt.pause(2)
    # plt.close()
    # plt.plot(op1_profit)
    # plt.ion()
    # plt.pause(2)
    # plt.close()
    plt.plot(x1_list, label="x1")
    plt.plot(x2_list, label="x2")
    plt.plot(total_demand, label="total")
    plt.title("demand")
    plt.legend()
    plt.ion()
    plt.pause(2)
    plt.tight_layout()
    plt.savefig("demand_case_"+str(case_id)+".png",bbox_inches='tight',dpi=600) 
    plt.close()
    plt.plot(op1_profit, label='op1')
    plt.plot(op2_profit, label='op2')
    plt.title("profit")
    plt.legend()
    plt.ion()
    plt.pause(2)
    plt.tight_layout()
    plt.savefig("proft_case_"+str(case_id)+".png",bbox_inches='tight',dpi=600) 
    plt.close()
    plt.plot(op2_profit, label='op2')
    plt.title("Op2 Profit")
    plt.ion()
    plt.savefig("Op2Profit"+str(case_id)+".png",bbox_inches='tight',dpi=600) 
    plt.close()
    # step 3: plot
