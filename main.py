"""
    main func
"""
import ParaScript as ps
import MyFuncs as mf
import matplotlib.pyplot as plt


if __name__ == '__main__':
    """
    main
    """
    para = ps.ParaClass()
    para.price = [10, 10]
    para.travel_time = [30, 20, 15]
    para.m = 1
    para.g = 0.25
    with open('TestResults.txt', 'w+') as f:
        print("TestId,Price1,Price2,Time1,Time2,Time3,DiscountRatio,m,g,x1,x2,profit1,profit2,opCost1,opCost2", file=f)
    mf.test_one_ParaSet(case_id=1, _para=para)

    # para.g = -0.25
    # mf.test_one_ParaSet(case_id=2, _para=para)

    # para.price = [10, 10]
    # para.travel_time = [20, 15, 15]
    # mf.test_one_ParaSet(case_id=2, _para=para)
