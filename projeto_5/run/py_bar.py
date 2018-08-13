
import csv
from matplotlib import pyplot as plt
import numpy as np

# obs.: verificar quais bibliotecas são necessárias ou não.

# Realizando o teste usando somente la_plata ##
# d1 - imerg la_plata
# d2 - 24Z NCEP la_plata
# d3 - 24 SMG la_plata 

x = []
y = []
z = []
p = []
with open('data/d1.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))

with open('data/d2.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
      
        z.append(float(row[1]))

with open('data/d3.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
       
        p.append(float(row[6]))

n_groups = 25
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.25
opacity = 0.8
 
rects1 = plt.bar(index, y, bar_width,
                 alpha=opacity,
                 color='b',
                 label='IMERG')
 
rects2 = plt.bar(index + bar_width, z, bar_width,
                 alpha=opacity,
                 color='y',
                 label='BAM-NCEP')

rects3 = plt.bar(index + bar_width + bar_width, p, bar_width,
                 alpha=opacity,
                 color='r',
                 label='BAM-DAS')

plt.xlabel('DIAS')
plt.ylabel('Scores')
plt.title('24h 12Z La_Plata')

# para gerar a figura graphic3_1
plt.plot(index, y, color='b', marker='s', label='Imerge-line')

plt.legend()

plt.ylim(ymin=0, ymax=20)


plt.tight_layout()
plt.show()
plt.savefig('graph3.png')
