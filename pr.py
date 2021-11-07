import matplotlib.pyplot as plt
# our X values:
k = list(range(5,40,5))
print(k)
# our Y values:
pr1_values = [25.6, 29.1, 32.7, 38, 46, 53,48]
pr2_values = [16, 18, 23, 36, 40, 46,45]
pr3_values = [29.5,33.6,35,40,48.5,60.5,58.7]
explicit=plt.plot(k, pr1_values,color='orange', label='explicit',linewidth=5)
implicit=plt.plot(k, pr2_values,color='blue', label='implicit',linewidth=5)
hybrid=plt.plot(k, pr3_values,color='green', label='hybrid',linewidth=5)
plt.xlabel('k')
plt.ylabel('Precision-at-k')
plt.grid(True)
plt.legend(loc="lower right")
p1=plt.show(explicit)
p2=plt.show(implicit)
p3=plt.show(hybrid)

