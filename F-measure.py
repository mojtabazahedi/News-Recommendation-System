import matplotlib.pyplot as plt
# our X values:
k = list(range(5,40,5))
print(k)
# our Y values:
f1_values = [13.6, 20, 30.1, 38.6, 48.3, 54.4,50.8]
f2_values = [7.7, 14.9, 23, 36.3, 40, 44.9,43.7]
f3_values = [18.7,24.7,33.5,41.4,50.4,59.9,58.3]
explicit=plt.plot(k, f1_values,color='orange', label='explicit',linewidth=5)
implicit=plt.plot(k, f2_values,color='blue', label='implicit',linewidth=5)
hybrid=plt.plot(k, f3_values,color='green', label='hybrid',linewidth=5)
plt.xlabel('k')
plt.ylabel('F-measure-at-k')
plt.grid(True)
plt.legend(loc="lower right")
p1=plt.show(explicit)
p2=plt.show(implicit)
p3=plt.show(hybrid)

