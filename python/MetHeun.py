import numpy as np
import matplotlib.pyplot as plt

dt = 0.001
t = 0

n = 10000

Y = np.array([1,0])
Yt = np.zeros((2,n+1))
tt = np.zeros((n+1))
Yt[:,0]=Y
def F(Y):
    x,y = Y
    return np.array([y, -x+(1-x**2)*y])  #Funciones
    #return np.array([y, -x])

for i in range(n):
    Y = Y + dt*F(Y)  #Met Euler con vectorial
    Ym = Y + dt*F(Y)
    Y = Y +dt/2*(F(Y)+ F(Ym))
    t = t + dt
    #print(Y,t)
    Yt[:,i+1] = Y
    tt[i+1] = t


plt.figure(1)
plt.grid()
plt.plot(tt,Yt.T,'-')
plt.show()

plt.figure(2)
plt.clf()
plt.grid()
plt.plot(Yt[0,:], Yt[1,:],'-')
plt.plot(Yt[0,0], Yt[1,0], 'or')
plt.axis('equal')
plt.show()
