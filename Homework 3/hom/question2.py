import numpy as np
import matplotlib.pyplot as plt
from Question1_3 import a1, b1, c1, computer

column =  ['data1', 'data2', 'data3']

max = [(np.max(a1)), (np.max(b1)), (np.max(c1))]
min = [(np.min(a1)), (np.max(b1)), (np.max(c1))]
mean = [(np.mean(a1)), (np.mean(b1)), (np.mean(c1))]
median = [(np.median(a1)), (np.median(b1), (np.median(c1)))]
mean_std = [(np.std(a1)), (np.std(b1)), (np.std(c1))] 
meanaddstd = mean + mean_std
p25 = [(np.percentile(a1, 25)),(np.percentile(b1, 25)),(np.percentile(c1, 25))]
p75 = [(np.percentile(a1, 75)),(np.percentile(b1, 75)),(np.percentile(c1, 75))]


plt.scatter(column,max,marker='x',color='m',label='max')
plt.scatter(column,min,marker='o',color='b',label='max')
plt.scatter(column,mean,marker='+',color='y',label='max')
#plt.scatter(column,median,marker='1',color='r',label='max')
#plt.scatter(column,mean_std,marker='2',color='g',label='max')
#plt.scatter(column,meanaddstd,marker='3',color='m',label='max')
#plt.scatter(column,p25,marker='>',color='y',label='max')
#plt.scatter(column,p75,marker='<',color='r',label='max')
#plt.legend(['max','min','mean','median','mean_std','meanaddstd','p25','p75'])
plt.show()
print()