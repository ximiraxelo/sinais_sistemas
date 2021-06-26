# author: XimiraXelo, reach me at esdrasbattostisilva@gmail.com

import numpy as np
import matplotlib.pyplot as plt

def u(t):
    # Heaviside step function
    if t < 0: 
        return 0 
    return 1


def g(t, delta=1):
    # Gate function
    if abs(t) <= delta/2:
        return 1
    return 0


def d(t):
    # Dirac Delta Function
    midle = int((PIECES-1)/2) 
    if t == points[midle]:
        return 1
    return 0


A = -20 # x_min and y_min
B = 20 # x_max and y_max
PIECES = 1001
points = np.linspace(A, B, num=PIECES)
        
res = []
function = input('Digite a função: f(t) = ')
          
for t in points:
    res.append(eval(function))

plt.plot(points, res)
plt.title(f'${function}$')
plt.xlabel('$t$')
plt.ylabel('$f(t)$')
plt.grid()
plt.show()