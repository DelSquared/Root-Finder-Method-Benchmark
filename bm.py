import time
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np

dx=0.04
n=600
times=20

def f(x,der=False):
  if der==False:
    return x*x-2
  else:
    return 2*x

def rootGD(func,dx,iter):
  vals = []
  x=20
  vals.append(x)
  for i in range(iter):
    x  -= func(x)*dx
    vals.append(x)
  return vals

def rootNR(func,dx,iter):
  vals = []
  x=20
  vals.append(x)
  for i in range(iter):
    if func(x,der=True)==0: break
    x  -= func(x)*dx/func(x,der=True)
    vals.append(x)
  return vals

def rootH(func,dx,iter):
  vals = []
  x=20
  k=75
  vals.append(x)
  for i in range(k):
    x  -= func(x)*dx
    vals.append(x)
  for i in range(iter-k):
    if func(x,der=True)==0: break
    x  -= func(x)*dx/func(x,der=True)
    vals.append(x)
  return vals

GD,NR,H=0,0,0
tGD,tNR,tH=0,0,0

t0 = time.time()
for i in range(times):
    GD = rootGD(f,dx,n)
t1 = time.time()

tGD=t1-t0

t0 = time.time()
for i in range(times):
    NR = rootNR(f,1,n)
t1 = time.time()

tNR=t1-t0

t0 = time.time()
for i in range(times):
    H = rootH(f,dx,n)
t1 = time.time()

tH=t1-t0

print("GD:\n")
print("value: {}\nerror: {}\ntime: {}\n".format(GD[len(GD)-1],abs(f(GD[len(GD)-1])),tGD))
print("NR:\n")
print("value: {}\nerror: {}\ntime: {}\n".format(NR[len(NR)-1],abs(f(NR[len(NR)-1])),tNR))
print("H:\n")
print("value: {}\nerror: {}\ntime: {}\n".format(H[len(H)-1],abs(f(H[len(H)-1])),tH))

dtGD = np.linspace(0,10*tGD,len(GD))
dtNR = np.linspace(0,10*tNR,len(NR))
dtH = np.linspace(0,10*tH,len(H))

fig=plt.figure()
plt.plot(dtGD, GD,label="GD")
plt.plot(dtNR, NR,label="NR")
plt.plot(dtH, H,label="H")
plt.legend()
plt.xlim(0,tGD)
#plt.ylim(0,2)
fig.savefig("plot.jpg")
