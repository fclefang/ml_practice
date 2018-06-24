'''
某空调厂2000年－2002年空调器销售量如下表所示。预计2003年的销售量比2002年递增3%，请用季节指数法预测2003年各季度销售量。

'''

import matplotlib.pyplot as plt
import numpy as np
import math


def yuce6(data,rate):
    n = len(data)
    #计算历年同季的销售平均数 
    A = []
    for i in range(4):
        A.append(int(sum(data[:,i])/n*10)/10)
    print(A)
    #计算历年季度总平均数
    B =int((sum(data[:,4])/12)*10)/10
    print(B)
    #计算季节指数
    S = []
    for i in range(4):
        S.append(round(A[i]/B,3))
    print(S)
    #下一年销售预测值
    Y_nextyear = round(data[-1,4]*(1+rate),1)
    print(Y_nextyear)
    #第n季度预测值
    Y_season = []
    for i in range(4):
        Y_season.append(round(Y_nextyear/4*S[i],2))
    print(Y_season)


x = np.array([
    [5.7,22.6,28.0,6.2,62.5,15.6],
    [6.0,22.8,30.2,5.9,64.9,16.2],
    [6.1,23.1,30.8,6.2,66.2,16.6]
])
rate = 0.03
# print(x[-1,4])
yuce6(x,rate)