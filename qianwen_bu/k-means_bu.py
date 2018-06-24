# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 10:24:53 2018

@author: qianwen Bu
"""
import matplotlib.pyplot as plt
import numpy as np

def dis(a,b):
    return np.sqrt(sum(np.square(np.array(a)-np.array(b))))

def mean(lists):
    return sum(np.array(lists)) / len(lists)
        
x = [2.273, 27.89, 30.519, 62.049, 29.263, 62.657, 75.735, 24.344, 17.667, 68.816, 69.076, 85.691]
y = [68.367, 83.127, 61.07, 69.343, 68.748, 90.094, 62.761, 43.816, 86.765, 76.874, 57.829, 88.114]
plt.plot(x,y,'b.')
plt.show()
point = [[i,j] for i,j in zip(x,y)]
print(point)

a = [20, 60]
b = [80, 80]
a = np.array(a)
b = np.array(b)
def kmeans(a,b,point):  
    a_list = []
    b_list = []
    for i in range(len(point)):
        if dis(a,point[i]) < dis(b,point[i]):
            a_list.append(point[i])
        else:
            b_list.append(point[i])
    print('A组：', a_list)
    print('B组：', b_list)
    aa = mean(a_list)
    bb = mean(b_list)
    if (aa == a).all() and (bb == b).all():
        print('结束')
        print('A点：', aa, 'B点：', bb)
        plt.plot([i[0] for i in a_list], [i[1] for i in a_list], 'r.')
        plt.plot([i[0] for i in b_list], [i[1] for i in b_list], 'b.')
        plt.grid()
        plt.show()
        return
    else:
        a = aa
        b = bb
        point = a_list+b_list
        kmeans(a,b,point)

kmeans(a,b,point)