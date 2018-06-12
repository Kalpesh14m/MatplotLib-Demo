import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

#sublpot(211) ==> 2->Vertically, 1->horizontally, 1->1st Graph
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2))

#sublpot(212) ==> 2->Vertically, 1->horizontally, 1->2nd Graph
plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2))

# plt.subplot(223)
# plt.plot(t1, f(t1), 'bo', t2, f(t2))
#
# plt.subplot(224)
# plt.plot(t1, f(t1), 'bo', t2, f(t2))

plt.show()
