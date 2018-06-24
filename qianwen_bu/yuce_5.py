'''
某地区最近几年自行车的销售量资料如下，试用指数曲线方程预测下一年的销售量。
https://baike.baidu.com/item/%E6%8C%87%E6%95%B0%E6%9B%B2%E7%BA%BF%E9%A2%84%E6%B5%8B%E6%B3%95/3155764?fr=aladdin
'''

import matplotlib.pyplot as plt
import numpy as np
import math



def yuce5(data,time):
    u_t = []
    log_Yt = []
    log_Yt2 = []
    tY = []
    num = len(data)
    t = []
    t2 = []
    for i in range(1,num):
        u_t.append((data[i]-data[i-1])/data[i])
    for i in range(num):
        log_Yt.append(round(math.log(data[i]),4))
        log_Yt2.append(round(math.log(data[i])**2,4))
        t.append(i+1)
        t2.append((i+1)*(i+1))
        tY.append(t[i]*log_Yt[i])
    t_sum = sum(t)
    t2_sum = sum(t2)
    Y_sum = sum(log_Yt)
    Y2_sum = sum(log_Yt2)
    tY_sum = sum(tY)
    t_mean = t_sum/num
    Y_mean = Y_sum/num
    b = (tY_sum-num*t_mean*Y_mean)/(t2_sum-num*(t_mean**2))
    A = Y_mean-b*t_mean
    a = math.e**A
    return a*((math.e)**(b*time))


x = [8.7,10.6,13.3,16.5,20.6,26]
# plt.plot(x)
# plt.show()
re = yuce5(x,7)
print(re)