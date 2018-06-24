'''
某市2001—2009年化纤零售量如表所示，试预测2010年化纤零售量
'''
import matplotlib.pyplot as plt
import numpy as np


def yuce2(data):
    t = []
    y_ = []
    t2_sum = 0
    tY_sum = 0
    num = len(data)
    if num%2==0:
        for i in range(num):
            t.append(-1-((num/2)-1)+i)
    else:
        for i in range(num):
            t.append(-1*((num-1)/2)+i)
    print(t)
    Y_sum = sum(data)
    t_sum = sum(t)
    for i in range(num):
        t2_sum += t[i]*t[i]
    for i in range(num):
        tY_sum += t[i]*data[i]
    print(Y_sum,t_sum,t2_sum,tY_sum)
    a = Y_sum/float(num)
    b = tY_sum/float(t2_sum)

    for i in range(num):
        y_.append(a+b*(t[i]))
    print(sum(y_))
    a_new = sum(y_)/float(num)
    b_new = tY_sum/float(t2_sum)
    print(a_new,b_new)
    return a_new+b_new*(t[-1]+1)

sale = [265,297,333,370,405,443,474,508,541]
difference_1 = [32,36,37,35,38,31,34,33]
# plt.plot(sale)
# plt.show()
re = yuce2(sale)
print(re)
