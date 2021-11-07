import matplotlib.pyplot as plt
# our X values:
k = list(range(5,40,5))
print(k)
# our Y values:
rc1_values = [9.3, 15.3, 28, 39.3, 51, 56,54]
rc2_values = [5.1, 12.8, 23, 36.8, 40, 44,42.5]
rc3_values = [13.7,19.6,32.3,43,52.5,59.5,58]
explicit=plt.plot(k, rc1_values,color='orange', label='explicit',linewidth=5)
implicit=plt.plot(k, rc2_values,color='blue', label='implicit',linewidth=5)
hybrid=plt.plot(k, rc3_values,color='green', label='hybrid',linewidth=5)
plt.xlabel('k')
plt.ylabel('Recall-at-k')
plt.grid(True)
plt.legend(loc="lower right")
p1=plt.show(explicit)
p2=plt.show(implicit)
p3=plt.show(hybrid)

