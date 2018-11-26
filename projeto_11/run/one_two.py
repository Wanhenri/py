from matplotlib import pyplot as plt

x =  [0, 1, 1, 2, 3, 5, 8, 13, 21]
y1 = [1, 4, 5, 6, 7, 8, 5, 1 , 4]
y2 = [2, 6, 2, 3, 4, 9, 1, 2, 5]



plt.plot(x,y1, color="pink", marker='o')
plt.title("Two Lines on One Graph")
plt.xlabel("Amazing X-axis")
plt.ylabel("Incredible Y-axis")
plt.legend([x,y1], loc=4)
plt.show()
plt.savefig('one_line.png')

plt.plot(x,y2, color="gray", marker='o')
plt.title("Two Lines on One Graph")
plt.xlabel("Amazing X-axis")
plt.ylabel("Incredible Y-axis")
plt.legend([x,y2], loc=4)
plt.show()
plt.savefig('two_line.png')
