# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 16:12:17 2021

@author: jjosh
"""

import csv
import math
import numpy as np

lines = csv.reader(open('outputnb.csv'))
dataset = list(lines)
n=0
b=0
nd=0
for i in range(len(dataset)):
	dataset[i] = [(x) for x in dataset[i]]
print(i)
#if(dataset[1][7])
com=dataset[0][7]
clo1=float(dataset[0][4])
clo2=0
w, h = 2,2717 ;
array = [[0 for x in range(w)] for y in range(h)] 
sum=0
k=0
for i in range(1048575):
    if(dataset[i][7] != com and dataset[i][8]=='BSE'):
        com=dataset[i][7]
        clo2=float(dataset[i-1][4])
        sum=clo2-clo1;
        array[k][0]=dataset[i-1][7]
        array[k][1]=sum
        k=k+1
    else:
        continue
print("NSE= ",n)
print("BSE= ",b)
#print(array)

N = 2
  
# Max value in Nth Column in Matrix
# using max() + zip()
res = [max(i) for i in zip(*array)][1] 
print(res)
from operator import itemgetter
res1=sorted(array,key=itemgetter(1))
#print(res1)
nse1=res1[-11:-1]

import matplotlib.pyplot as plt
import pandas as pd

#clean_data = [[(str(item).split()[0]) for item in row] for row in nse1]

    
#data=(pd.DataFrame(clean_data, columns=list('xy')))
import numpy as np
import matplotlib.pyplot as plt
     
import random
random.shuffle(nse1)
d = {}
for elem in nse1:
    d[elem[1]] = elem[0]
print(d)


#import pandas as pdimport 
import matplotlib.pyplot as plt
     
#data = {'NB':accuracy_n,'DT':accuracy_d,'LGR':accuracy_L}
import numpy as np
import matplotlib.pyplot as plt
courses = list(d.keys())
values = list(d.values())

  
fig = plt.figure(figsize = (20, 5))
 
# creating the bar plot
plt.bar(values, courses)
 
plt.xlabel("Companies")
plt.ylabel("Profit")
plt.show()


