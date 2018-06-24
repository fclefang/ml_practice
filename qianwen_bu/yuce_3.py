'''
例3：某企业要进行食盐销售量预测，现在有最近连续30个月的历史资料试用一次指数平滑法预测以后月份的销售量。
'''
import matplotlib.pyplot as plt
import numpy as np

def yuce3(data,a):
    S = []
    s_pre = 0
    num = len(data)
    s1 = a*data[0]+(1-a)*(sum(sale[0:3])/3)
    S.append(round(s1,1))
    print(s1)
    for i in range(num):
        s_pre = S[-1]
        S.append(round(a*data[i]+(1-a)*s_pre,1))
    print(S)        
    # print(len(S))


sale = [26.7,29.5,29.0,29.9,32.2,31.4,25.7,32.1,29.1,30.8,25.7,30.9,31.5,28.1,30.8,29.5,29.8,30.0,29.9,31.5,27.6,29.9,30.2,30.3,30.8,28.8,30.8,32.2,31.2,25.4]
# print(sale)
# plt.plot(sale)
# plt.show()
yuce3(sale,0.3)
print(sum(sale[0:3])/3)