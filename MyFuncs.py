"""
    contain all the functions
"""
from os import times
import ParaScript as ps
import matplotlib.pyplot as plt

#TODO:
# 1. add fixed operation cost 
# 2. add the effect of freqeuncy 



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
        # self.distance = 0.0
        
    def set_price(self, _val):
        self.price = _val

    def cal_opcost(self, _para: ps.ParaClass()):
        self.opcost = self.fxcost+_para.opCostPerPas*self.numpas

    # def cal_profit(self, _para: ps.ParaClass()):
    #     if self.id == 1:
    #         self.profit = self.price*self.numpas-self.opcost
    #     if self.id == 2:
    #         self.profit = (self.price-self.discount)*self.numpas-self.opcost

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
    third_bracket = _para.g * (_op[0].price+_para.val_of_time*_op[0].time + _op[1].price+_para.val_of_time*_op[1].time-_para.a2-_op[1].discount)
    x1 = first_bracket*(second_bracket-third_bracket)

    second_bracket = _para.m * (_op[1].price+_op[0].price+_para.val_of_time*_op[1].time + _para.val_of_time*_op[0].time- _para.a2-_op[1].discount)
    third_bracket = _para.g * (_op[0].price+_para.val_of_time*_op[0].time - _para.a1+_para.val_of_time*_op[2].time)
    x2 = first_bracket*(second_bracket - third_bracket)
    _op[0].numpas = x1
    _op[1].numpas = x2
    

#    fourth_bracket=1/2*(_para.g**2-_para.m**2)
#    fifth_bracket =  (_para.μ*_op[4].distance+_para.val_of_time*_op[4].time - _para.a2-_op[4].discount*abs(_op[4].time -_op[3].time ))
#   sixth_bracket =  (_para.μ*_op[3].distance+_para.val_of_time*_op[3].time+_op[2].time)
#    x4=fourth_bracket*( _para.m*fifth_bracket-_para.g *sixth_bracket)
#    x5=fourth_bracket*(_para.m *sixth_bracket-_para.g*fifth_bracket)
#    #_op[3].numpas = x4
#    #_op[4].numpas = x5
#   seventh_bracket=1/(_para.g**2-4*_para.m**2)*(_para.g**2-_para.m**2)
#    eighth_bracket =(_para.a1-_para.val_of_time*_op[5].time-_para.μ*_op[5].distance-_op[2].time)
#    ninth_bracket=(_para.a2-_para.val_of_time*_op[6].time-_para.μ*_op[6].distance+_op[6].discount*abs(_op[5].time -_op[6].time))
#   tenth_bracket=(_para.a1-_para.μ*_op[5].distance-_para.val_of_time*_op[5].time)
#   x6=seventh_bracket*(2*_para.m**3*eighth_bracket-_para.g*_para.m**2*ninth_bracket-_para.m*_para.g**2*tenth_bracket)
#    x7=seventh_bracket*(2*_para.m**3*(ninth_bracket+_para.val_of_time*_op[5].time)-_para.g*_para.m**2*(tenth_bracket-_op[2].time)-_para.m*_para.g**2* ninth_bracket)
#    _op[5].numpas = x6
#    _op[6].numpas = x7
    
def cal_profit(_p:ps.ParaClass,_op):
    """
        compute profit for the two operators
    """
    _op[1].profit = (_op[1].price -_op[1].discount)*_op[1].numpas - _op[1].opcost
    _op[0].profit = _op[0].price*(_op[1].numpas + _op[0].numpas) - _op[1].opcost

def update_costAndProfit(_p: ps.ParaClass, _op):
    # step 1: compute the operation cost
    _op[0].opcost = _op[0].fxcost + _p.opCostPerPas*_op[0].numpas
    _op[1].opcost = _op[1].fxcost + _p.opCostPerPas*_op[1].numpas
  
    # step 1: compute the profit
    cal_profit(_p,_op)


def find_optimal_discount(dc,pf):
    """
        find the optimal discount value
        dc: discount list
        pf: profit lst
    """
    if len(dc) != len(pf):
        print("Warning: the length of the input list do not equal")
        input("--------need to debug----------------")

    max_prof = -9999
    max_prof_index = -1
    for i in range(0,len(dc)):
        if pf[i]>max_prof:
            max_prof_index = i
            max_prof = pf[i]
    return dc[max_prof_index],pf[max_prof_index]


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
    #operators[3].time = _para.travel_time[3]
    # operators[4].time = _para.travel_time[4]
    #operators[5].time = _para.travel_time[5]
    operators[0].fxcost = _para.fxcost[0]
    operators[1].fxcost = _para.fxcost[1]

    for i in range(0, 10):
        _para.discount_ratio = 0.05*(i+1)
        operators[1].discount = get_discont_val(
            operators[0].time, operators[1].time, _para)
        discount_val= get_discont_val(
            operators[0].time, operators[1].time, _para)
        discount.append(discount_val)
        if operators[1].price - operators[1].discount < 0:
            print("error: the op2 price after discout is negative")
            input()
        get_x(_para, operators)
        # print("{0},{1}".format(operators[0].numpas,operators[1].numpas))
        update_costAndProfit(_para, operators)
        x1_list.append(operators[0].numpas)
        x2_list.append(operators[1].numpas)
        total_demand.append(operators[0].numpas + operators[1].numpas)
        op1_profit.append(operators[0].profit)
        op2_profit.append(operators[1].profit)
        op1_cost.append(operators[0].opcost)
        op2_cost.append(operators[1].opcost)

    for i in range(0,len(x1_list)):
        with open('TestResults.csv', 'a') as f:
        # print("TestId,Price1,Price2,Time1,Time2,Time3,DiscountRatio,m,g,x1,x2,profit1,profit2,opCost1,opCost2",file=f)
            print("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14}".format
            (case_id,_para.price[0],_para.price[1],_para.travel_time[0],_para.travel_time[1],_para.travel_time[2],
            discount[i],_para.m,_para.g,x1_list[i],x2_list[i],op1_profit[i],op2_profit[i],
            op1_cost[i],op2_cost[i]),file=f)
    opt_disc, opt_profit = find_optimal_discount(discount,op2_profit) 
    print("Optimal Discount = {0}, Optimal Profit = {1}".format(opt_disc, opt_profit))
 
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
    # plt.plot(total_demand, label="total")
    # plt.title("Demand")
    xtick = plt.gca().get_xticks()
    ytick = plt.gca().get_yticks()
    xtick = discount
    plt.gca().set_xticklabels(xtick, fontsize=10,fontname='Times New Roman')
    plt.gca().set_yticklabels(ytick, fontsize=10,fontname='Times New Roman')
    xmajorFormatter = plt.FormatStrFormatter('%.1f')
    plt.gca().xaxis.set_major_formatter(xmajorFormatter)
    plt.gca().set_xlabel("Discount Value",fontsize=12,fontname='Times New Roman')
    plt.legend()
    plt.ion()
    plt.pause(1)
    plt.tight_layout()
    plt.savefig("Base_Demand_Case_"+str(case_id)+".png",bbox_inches='tight',dpi=600) 
    plt.close()

    plt.plot(op1_profit, label='op1')
    plt.plot(op2_profit, label='op2')
    plt.title("profit", fontsize = 12, fontname ='Times New Roman')
    xtick = plt.gca().get_xticks()
    ytick = plt.gca().get_yticks()
    xtick = discount
    plt.gca().set_xticklabels(xtick, fontsize=10,fontname='Times New Roman')
    plt.gca().set_yticklabels(ytick, fontsize=10,fontname='Times New Roman')
    xmajorFormatter = plt.FormatStrFormatter('%.1f')
    plt.gca().xaxis.set_major_formatter(xmajorFormatter)
    plt.gca().set_xlabel("Discount Value",fontsize=12,fontname='Times New Roman')
  
    plt.legend()
    plt.ion()
    plt.pause(1)
    plt.tight_layout()
    plt.savefig("Base_Profit_Case_"+str(case_id)+".png",bbox_inches='tight',dpi=600) 
    plt.close()
    
   # plot op 2 
    plt.plot(op2_profit)
    plt.title("Operator 2 Profit",fontsize=12, fontname='Times New Roman')
    xtick = plt.gca().get_xticks()
    ytick = plt.gca().get_yticks()
    xtick = discount
    plt.gca().set_xticklabels(xtick, fontsize=10,fontname='Times New Roman')
    plt.gca().set_yticklabels(ytick, fontsize=10,fontname='Times New Roman')
    xmajorFormatter = plt.FormatStrFormatter('%.1f')
    plt.gca().xaxis.set_major_formatter(xmajorFormatter)
    plt.gca().set_xlabel("Discount Value",fontsize=12,fontname='Times New Roman')
    plt.gca().set_ylabel("Profit",fontsize=12,fontname='Times New Roman')
    plt.ion()
    plt.pause(1)
    plt.savefig("Base_Profit_Op2_Case_"+str(case_id)+".png",bbox_inches='tight',dpi=600) 
    plt.close()
    # plot op1 
    plt.plot(op1_profit)
    xtick = plt.gca().get_xticks()
    ytick = plt.gca().get_yticks()
    xtick = discount
    plt.gca().set_xticklabels(xtick, fontsize=10,fontname='Times New Roman')
    plt.gca().set_yticklabels(ytick, fontsize=10,fontname='Times New Roman')
    xmajorFormatter = plt.FormatStrFormatter('%.1f')
    plt.gca().xaxis.set_major_formatter(xmajorFormatter)
    plt.gca().set_xlabel("Discount Value",fontsize=12,fontname='Times New Roman')
    plt.gca().set_ylabel("Profit",fontsize=12,fontname='Times New Roman')
 
    plt.title("Operator 1 Profit",fontsize =12, fontname ='Times New Roman')
    plt.ion()
    plt.pause(1)
    plt.savefig("Base_Profit_Op1_Case_"+str(case_id)+".png",bbox_inches='tight',dpi=600) 
    plt.close()
    # step 3: plot


def get_x_share_mon(_para: ps.ParaClass, _op):
    """
    """
    first_denominator= 1/(2*(_para.g**2-_para.m**2))
    first_brack_x1 =  (_para.val_of_time*_op[0].time - _para.a1-_op[2].time )
    second_brack_x1 = (_para.val_of_time*_op[1].time -_para.a2-_op[1].discount)
    x1 = first_denominator*(_para.m*first_brack_x1-_para.g*second_brack_x1)
    x2 = first_denominator*(_para.m*second_brack_x1-_para.g*first_brack_x1)
    _op[0].numpas = x1
    _op[1].numpas = x2
  
def get_price_share_mon(_para: ps.ParaClass, _op):
    """
    """
    _op[0].price = 0.5*(_para.a1-_para.val_of_time*_op[0].time-_op[2].time)
    _op[1].price = 0.5*(_para.a2-_para.val_of_time*_op[1].time+_op[1].discount)

    
def test_one_share(case_id: int, _para: ps.ParaClass()):
    
    x1_list = []
    x2_list = []
    
    total_demand = []
    discount = []
    op1_profit = []
    op2_profit = []
    total_profit = []
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
    #operators[3].time = _para.travel_time[3]
    # operators[4].time = _para.travel_time[4]
    #operators[5].time = _para.travel_time[5]
    operators[0].fxcost = _para.fxcost[0]
    operators[1].fxcost = _para.fxcost[1]

    

    for i in range(0, 15):
        _para.discount_ratio = 0.05*(i+1)
        operators[1].discount = get_discont_val(
            operators[0].time, operators[1].time, _para)
        discount_val= get_discont_val(
            operators[0].time, operators[1].time, _para)
        discount.append(discount_val)
        if operators[1].price - operators[1].discount < 0:
            print("error: the op2 price after discout is negative")
            input()
        # get_x(_para, operators)
        get_x_share_mon(_para, operators)
        # print("price {0},{1}".format(operators[0].price,operators[1].price))
        get_price_share_mon(_para, operators)
        # print("price {0},{1}".format(operators[0].price,operators[1].price))
        update_costAndProfit(_para, operators)
        # print("{0},{1}".format(operators[0].numpas,operators[1].numpas))
        # update_costAndProfit(_para, operators)
        x1_list.append(operators[0].numpas)
        x2_list.append(operators[1].numpas)
        # total_demand.append(operators[0].numpas + operators[1].numpas)
        op1_profit.append(operators[0].profit)
        op2_profit.append(operators[1].profit)
        total_profit.append(operators[0].profit+operators[1].profit)
        op1_cost.append(operators[0].opcost)
        op2_cost.append(operators[1].opcost)

    plt.plot(x1_list, label="x1")
    plt.plot(x2_list, label="x2")
    # plt.plot(total_demand, label="total")
    plt.title("Demand")
    plt.legend()
    plt.ion()
    plt.pause(1)
    plt.tight_layout()
    plt.savefig("ShareMono_Demand_Case_"+str(case_id)+".png",bbox_inches='tight',dpi=600) 
    plt.close()

    plt.plot(op2_profit)
    plt.title("Op2 Profit")
    plt.ion()
    plt.pause(1)
    plt.savefig("ShareMono_Profit_Op2_Case_"+str(case_id)+".png",bbox_inches='tight',dpi=600) 
    plt.close()
    
    plt.plot(op1_profit)
    plt.title("Op1 Profit")
    plt.ion()
    plt.pause(1)
    plt.savefig("ShareMono_Profit_Op1_Case_"+str(case_id)+".png",bbox_inches='tight',dpi=600) 
    plt.close()
    
    plt.plot(total_profit)
    plt.title("TotalProfit")
    plt.ion()
    plt.pause(1)
    plt.savefig("ShareMono_Profit_Total_Case_"+str(case_id)+".png",bbox_inches='tight',dpi=600) 
    plt.close()
    for i in range(0,len(x1_list)):
        with open('TestResults.csv', 'a+') as f:
            print("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14}".format
            (case_id,_para.price[0],_para.price[1],_para.travel_time[0],_para.travel_time[1],_para.travel_time[2],
            _para.discount_ratio,_para.m,_para.g,x1_list[i],x2_list[i],op1_profit[i],op2_profit[i],
            op1_cost[i],op2_cost[i]),file=f)
    opt_disc, opt_profit = find_optimal_discount(discount,total_profit) 
    print("Optimal Discount = {0}, Optimal Profit = {1}".format(opt_disc, opt_profit))
 
 
  
  #######################################################################
  
 
def get_price_Betran(_para: ps.ParaClass, _op):
    """
    price formula
    """
  
def get_x_Betran(_para: ps.ParaClass, _op):
    """
        x formula
    """
def test_one_Bertand(case_id: int, _para: ps.ParaClass()):
    """

    """
    x1_list = []
    x2_list = []
    
    total_demand = []
    discount = []
    op1_profit = []
    op2_profit = []
    total_profit = []
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
    #operators[3].time = _para.travel_time[3]
    # operators[4].time = _para.travel_time[4]
    #operators[5].time = _para.travel_time[5]
    operators[0].fxcost = _para.fxcost[0]
    operators[1].fxcost = _para.fxcost[1]

    
    for i in range(0, 15):
        _para.discount_ratio = 0.05*(i+1)
        operators[1].discount = get_discont_val(
            operators[0].time, operators[1].time, _para)
        discount_val= get_discont_val(
            operators[0].time, operators[1].time, _para)
        discount.append(discount_val)
        if operators[1].price - operators[1].discount < 0:
            print("error: the op2 price after discout is negative")
            input()

        get_price_Betran(_para, operators)
        get_x_Betran(_para, operators)

        update_costAndProfit(_para, operators)
        # print("{0},{1}".format(operators[0].numpas,operators[1].numpas))
        # update_costAndProfit(_para, operators)
        x1_list.append(operators[0].numpas)
        x2_list.append(operators[1].numpas)
        # total_demand.append(operators[0].numpas + operators[1].numpas)
        op1_profit.append(operators[0].profit)
        op2_profit.append(operators[1].profit)
        total_profit.append(operators[0].profit+operators[1].profit)
        # op1_cost.append(operators[0].opcost)
        # op2_cost.append(operators[1].opcost)

    plt.plot(x1_list, label="x1")
    plt.plot(x2_list, label="x2")
    # plt.plot(total_demand, label="total")
    plt.title("Demand")
    plt.legend()
    plt.ion()
    plt.pause(1)
    plt.tight_layout()
    plt.savefig("Bert_Demand_Case_"+str(case_id)+".png",bbox_inches='tight',dpi=600) 
    plt.close()

    plt.plot(op2_profit)
    plt.title("Op2 Profit")
    plt.ion()
    plt.pause(1)
    plt.savefig("Bert_Profit_Op2_Case_"+str(case_id)+".png",bbox_inches='tight',dpi=600) 
    plt.close()
    
    plt.plot(op1_profit)
    plt.title("Op1 Profit")
    plt.ion()
    plt.pause(1)
    plt.savefig("Bert_Profit_Op1_Case_"+str(case_id)+".png",bbox_inches='tight',dpi=600) 
    plt.close()
    
    plt.plot(total_profit)
    plt.title("TotalProfit")
    plt.ion()
    plt.pause(1)
    plt.savefig("Bert_Profit_Total_Case_"+str(case_id)+".png",bbox_inches='tight',dpi=600) 
    plt.close()
 
    for i in range(0,len(x1_list)):
        with open('TestResults.csv', 'a+') as f:
        # print("TestId,Price1,Price2,Time1,Time2,Time3,DiscountRatio,m,g,x1,x2,profit1,profit2,opCost1,opCost2",file=f)
            print("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14}".format
            (case_id,_para.price[0],_para.price[1],_para.travel_time[0],_para.travel_time[1],_para.travel_time[2],
            _para.discount_ratio,_para.m,_para.g,x1_list[i],x2_list[i],op1_profit[i],op2_profit[i],
            op1_cost[i],op2_cost[i]),file=f)
    # opt_disc, opt_profit = find_optimal_discount(discount,op2_profit) 
    # print("Optimal Discount = {0}, Optimal Profit = {1}".format(opt_disc, opt_profit))
 