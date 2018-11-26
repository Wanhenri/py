import itertools
import string

a = ['VTMP-925','VTMP-850','VTMP-500','VTMP']
b = ['TEMP-250','TEMP-500','TEMP-850','TEMP']
c = ['UMES-500','UMES-850','UMES-925','UMES']
d = ['ZGEO-250','ZGEO-500','ZGEO-850','ZGEO']
e = ['UVEL-250','UVEL-500','UVEL-850','UVEL']
f = ['VVEL-250','VVEL-500','VVEL-850','VVEL']

g = ['6' , '10', '14', '18', '22', '26']
h = ['ACOR', 'RMS', 'VIEW']

#for char in "cdefg":

#for ll1, ll, i in itertools.product(h, range(0,1), range(1,13,2)):
for ll, ll1, i in itertools.product(range(0,2), h, range(1,13,2)): 
    k = str(i)
    x = g[ll]
    print("plt.subplot(6, 2,"+ k +" )")
    print("plot_ROC('" + "','".join(a) + "','" + x + "','" + ll1 + "')")
