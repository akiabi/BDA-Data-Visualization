import csv
import math



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
for i in range(1048575):
    if(dataset[i][7] != com and dataset[i][8]=='NSE'):
            com=dataset[i][7]
            n=n+1
    elif(dataset[i][7] != com and dataset[i][8]=='BSE'):
        com=dataset[i][7]
        b=b+1
    elif(dataset[i][7] != com and dataset[i][8]=='NASDAQ'):
        com=dataset[i][7]
        nd=nd+1
    else:
        continue
print("NSE= ",n)
print("BSE= ",b)
print("NASDAQ= ",nd)
from matplotlib import pyplot as plt
import numpy as np
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
langs = ['NSE', 'BSE', 'NASDAQ']
students = [n,b,nd]
colors = ['blue', 'orange', 'green']
patches, texts = plt.pie(students, colors=colors, startangle=90)
plt.legend(patches, langs, loc="best")
ax.pie(students, labels = langs,autopct='%1.2f%%')
ax.set_title("Percentage of companies in Stock Exchanges")
plt.show()
  







    
    

