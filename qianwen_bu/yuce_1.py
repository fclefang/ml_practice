'''
已知某商店1991年—1998年某一种商品销售量的统计数据如表，试预测1999年该商品销售量。
'''

import matplotlib.pyplot as plt
import numpy as np

def yuce1(data):
    t = []
    t2_sum = 0
    tY_sum = 0
    num = len(data)
    if num%2==0:
        for i in range(num):
            t.append(-1-2*((num/2)-1)+i*2)
    else:
        for i in range(num):
            t.append(-2*((num-1)/2)+i*2)
    Y_sum = sum(data)
    t_sum = sum(t)
    for i in range(num):
        t2_sum += t[i]*t[i]
    for i in range(num):
        tY_sum += t[i]*data[i]
    print(Y_sum,t_sum,t2_sum,tY_sum)
    a = Y_sum/float(num)
    b = tY_sum/float(t2_sum)
    return a+b*(t[-1]+2)



x = [248,253,257,260,266,270,279,285]
# plt.plot(x)
# plt.show()
re = yuce1(x)
print(re)