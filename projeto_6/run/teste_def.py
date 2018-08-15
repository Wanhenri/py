#import pandas as pd
import csv
import matplotlib.pyplot as plt
#from matplotlib import style
from matplotlib import pyplot as plt


# Realizando o teste usando somente la_plata ##
# d1 - imerg la_plata
# d2 - 24Z NCEP la_plata
# d3 - 24 SMG la_plata 


x = []
y = []

with open('data/d1.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))

z=[]

with open('data/d2.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
      
        z.append(float(row[6]))

p=[]

with open('data/d3.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
       
        p.append(float(row[6]))

# Plot 1 figura
def plot_ROC(eixo_x, eixo_y1,label_1, eixo_y2,label_2, eixo_y3, label_3):

  t = ("This is a really long string")
  
  plt.text(12, 20, t, fontsize=12, style='oblique', va='top', wrap=True)  
    
  plt.plot(eixo_x,eixo_y1,label=label_1)
  plt.plot(eixo_x,eixo_y2,label=label_2)
  plt.plot(eixo_x,eixo_y3,label=label_3)
  plt.xlim(xmin=1, xmax=25)
  plt.ylim(ymin=-2, ymax=20)
  plt.xlabel('Dias')
  plt.ylabel('')
  plt.title('Serie temporal da Area La_Plata')
	
  plt.legend()
	
  plt.grid()
	
  plt.show()
	
  plt.savefig('teste_def.png')
	
  plt.clf()
    

plot_ROC(x,y,'IMERGE - La_plata',z,'24h 12Z NCEP la_plata', p,'24h 12Z SMG la_plata') 
