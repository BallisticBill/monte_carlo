import matplotlib.pyplot as plt
import numpy as np
import random as rnd
import math
from scipy.stats import expon

def circle_area(radius,iter):
    res=0
    for i in range(iter):
        x = rnd.uniform(-radius,radius)
        y = rnd.uniform(-radius,radius)
        if x**2 + y**2 <= 1:
            res = res + 1
    return (2*radius)**2 * res/iter

def integral_sin(limits,iter):
    a,b = limits
    res=0
    for i in range(iter):
        x = rnd.uniform(a,b)
        res += math.sin(x)
    return (b-a)/iter * res


def hard_integral(iter):
    res=0
    x = np.random.exponential(size=iter)
    x_val=[]
    y_val=[]
    for i in range(1,iter):
        res += (1/(x[i]**2 + math.cos(x[i])**2))*(np.exp(x[i]))
        y_val.append(res/i)
        x_val.append(i)
    return x_val,y_val

def plot_sin_integral():
    x = [i*20 for i in range(1,500)]
    y=[integral_sin((0,math.pi),i) for i in x]
    plt.plot(x,y)
    plt.plot([10,10000],[2,2])
    plt.ylim(ymax=2.5,ymin=1.75)
    plt.title(r"Plot of $\int_0^\pi  \sin(x) dx$ For Different Iterations")
    plt.xlabel('No. of trials',fontsize=12)
    plt.ylabel('Integral of sin(x) from 0 to pi',fontsize=12)
    plt.legend(['Result', 'Actual value'],fontsize=12)
    print("value at 5000 iterations: "+str(y[250]))
    print("value at 10000 iterations: "+str(y[len(y)-1]))
    plt.show()

def plot_circle_area():
    x = [i*20 for i in range(1,500)]
    y=[circle_area(1,i) for i in x]
    plt.plot(x,y)
    plt.plot([10,10000],[math.pi,math.pi])
    plt.ylim(ymax=4,ymin=2)
    plt.title(r"Area Of Unit Circle For Different Iterations")
    plt.xlabel('No. of trials',fontsize=12)
    plt.ylabel('Area',fontsize=12)
    plt.legend(['Result', 'Actual value'],fontsize=12)
    print("value at 5000 iterations: "+str(y[250]))
    print("value at 10000 iterations: "+str(y[len(y)-1]))
    plt.show()

def plot_hard_integral():
    x = np.linspace(0,100,1000)
    plt.plot(x,1/((x**2 + np.cos(x)**2)))
    plt.title(r"Plot of $\frac{1}{ x^{2} + cos^{2}(x) ​}$")
    plt.xlabel('x',fontsize=12)
    plt.ylabel(r"$\frac{1}{ x^{2} + cos^{2}(x) ​}$",fontsize=12)
    plt.show()
    val = 1.89344
    x,y = hard_integral(10000)
    plt.plot(x,y)
    plt.plot([0,10000],[val,val])
    plt.ylim(0,3)
    plt.title(r"Convergence Graph of  $\int_0^\infty  \frac{1}{x^{2} + cos^{2}(x) } dx$ ")
    plt.xlabel('No. of Samples',fontsize=12)
    plt.ylabel('Integral of f(x)',fontsize=12)
    plt.legend(['Result', 'Actual value'],fontsize=12)
    print("value at 5000 iterations: "+str(y[5000]))
    print("value at 10000 iterations: "+str(y[len(y)-1]))
    plt.show()

plot_hard_integral()
plot_sin_integral()
plot_circle_area()