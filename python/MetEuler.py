import numpy as np
import matplotlib.pyplot as plt

#Var
t = 0
dt = 0.1
x = 1
y = 1

n = 1000

xt = np.zeros(n+1)
yt = np.zeros(n+1)
tt = np.zeros(n+1)

xt[0]= x
yt[0]= y 
tt[0]= t 


# Met Euler
for i in range(n):
    m = y             #Funciones
    n = -x+(1-x**2)*y #Funciones

    x = x + m*dt
    y = y + n*dt
    t = t + dt

    xt[i+1]=x
    yt[i+1]=y
    tt[i+1]=t
    print([x,y])


plt.figure(1)
plt.plot(tt,xt,'-')
plt.plot(tt,yt,'-')
plt.xlabel('$t$',fontsize=20)
plt.grid(True)

#

plt.figure(2)
plt.plot(xt,yt,'-')
plt.grid(True)
plt.xlabel('$x$',fontsize=20)
plt.ylabel('$y$',fontsize=20)
plt.plot(xt[0],yt[0], 'or')
plt.axis('equal')
