from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

x1 = [1,4,8]
y1 = [5,3,7]

x2 = [2,3,8]
y2 = [5,2,9]

plt.plot(x1, y1, label='Line One', linewidth=5)
plt.plot(x2, y2, label='Line Two', linewidth=5)


plt.title("Style And Labeling Info")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.legend()

plt.grid(True, color='k')

plt.show()
