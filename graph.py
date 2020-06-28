# -*- coding: utf-8 -*-


import pylab as plt

def linear_graph(a,b,x):
    return 2*x

def square_graph(a,b,c,x):
    return x**2+3

def reversed_proportion(x):
    return 1*x-2

def relu(x):
    return 5*x-x**2-7

def draylz(x):
    return 6*x+1

vals=range (-10,10)
    
lin=[]

sq=[]

rp=[]

re=[]

ks=[]


for i in vals:
    lin.append(linear_graph(1,0,i))
    sq.append(square_graph(1,1,0,i))
    rp.append(reversed_proportion(i))
    re.append(relu(i))
    ks.append(draylz(i))
    
print (ks)
    
fig=plt.figure(1, figsize=(12,13))
    
plt.subplots_adjust(hspace = 0.5)
    
    
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
    
ax1.plot(vals,lin,'b', label="linear")
ax1.plot(vals,sq,'r', label="square")
    
ax2.plot(vals,rp,'b', label="reverse proportion")
ax2.plot(vals,re,'r', label="relu")
ax2.plot(vals,ks,'g', label="square")
    
ax1.legend(loc='lower right')
ax2.legend(loc='lower right')
    
plt.savefig("graphs.png")
    
plt.show()