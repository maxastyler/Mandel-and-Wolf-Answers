import matplotlib.pyplot as plt
import numpy as np
NS=[0,2, 4, 6]
def dist_gen(n):
    return lambda x: (x**n)*((1-x)**n)*(2*n+1)*((np.math.factorial(2*n))/(np.math.factorial(n)**2))
xs=np.linspace(0, 1, 100)
for i in NS:
    a=dist_gen(i)
    plt.plot(xs, a(xs))
plt.legend([r"$N={}$".format(i) for i in NS])
plt.savefig("bayes_graphs.svg")
