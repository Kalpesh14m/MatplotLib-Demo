import matplotlib.pyplot as plt

x = [1,3,5,7,9]
y = [5,2,7,8,2]
plt.scatter(x, y, label="skitscar", color='k')

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter Plot Info")

plt.legend()

plt.show()
