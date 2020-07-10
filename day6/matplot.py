import numpy as np
import matplotlib.pyplot as plt


""" 
x=np.arange(0,1,0.1)
print(x) 


x=np.arange(0,3*np.pi,0.1)
y=np.sin(x)
plt.plot(x,y)
plt.show()

x=np.arange(0,3*np.pi,0.1)
y=np.tan(x)
plt.plot(x,y)
plt.show()
"""
x=np.arange(0,3*np.pi,0.1)
y_cos=np.cos(x)
y_sin=np.sin(x)

plt.plot(x,y_cos)
plt.plot(x,y_sin)

plt.xlabel("x axis label")
plt.ylabel("y axis label")
plt.title("sin and cos graph")
plt.legend(["cos","sine"])
plt.show()