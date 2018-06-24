'''
某商店1990—2001年销售额如下，请运用指数平滑法预测2002年、2003年、2004年、2005年、2006年的销售额。（α＝0.9）（设初始值为前三期的移动平均值
'''

import matplotlib.pyplot as plt
import numpy as np


def yuce3(data,a):
    S = []
    s_pre = 0
    num = len(data)
    s1 = sum(data[0:3])/3
    S.append(round(s1,1))
    print(s1)
    for i in range(1,num):
        s_pre = S[-1]
        S.append(round(a*data[i]+(1-a)*s_pre,1))
    print(S)        
    return S
def yuce4(data,a,t):
    S_1 = yuce3(data,a)
    S_2 = yuce3(S_1,a)
    a_t = 2*S_1[-1]-S_2[-1]
    b_t = a/(1-a) *(S_1[-1]-S_2[-1])
    Y_T = a_t + b_t*(t-len(data))
    return Y_T


x = [440,481,513,510,536,575,620,660,711,736,791,825]
a = 0.9
re = yuce4(x,a,14)
print(re)