import matplotlib.pyplot as plt

slices = [7,2,2,13]
activities = ['sleeping', 'eating', 'working', 'playing']
cols=['m','c','r','b']

plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow=True,
        explode=(0,0,0,0),
        autopct='%1  .1f%%')

plt.title("Pie Plot Info")

plt.show()
