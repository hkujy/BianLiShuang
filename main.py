
import ParaScript as ps
import MyFuncs as mf
import matplotlib.pyplot as plt


if __name__ == '__main__':
    """
    main
    """
    para = ps.ParaClass()
    para.price = [20, 20]
    para.travel_time = [20, 10, 20]
    para.m = 1
    para.g = 0.25
    para.fxcost= [50, 50]
    para.val_of_time = 1.0
    para.opCostPerPas = 1.0
    with open('TestResults.csv', 'w+') as f:
        print("TestId,Price1,Price2,Time1,Time2,Time3,DiscountRatio,m,g,x1,x2,profit1,profit2,opCost1,opCost2", file=f)
    
    mf.test_one_ParaSet(case_id=1, _para=para)
    # mf.test_one_share(case_id=2, _para=para)
    # mf.test_one_Bertand(case_id=3, _para=para)

