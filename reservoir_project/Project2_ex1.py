# -*- coding: utf-8 -*-
"""
Title:      Project 2 - Exercise 1
Author:     Aleksander B. Jakobsen
Created:    Wed Sep 30 10:13:15 2020

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


tf = 4
dt = 0.001
q = 1
V = 1
c0 = 1

def analytical(t,c0=c0,q=q,V=V):
    tau = V/q
    return c0*np.exp(-t/tau)

def one_step(c,q,V,dt):
    fact = dt*q/V
    return(1-fact)*c
    
def euler(dt=dt,c0=c0,q=q,V=V,tf=tf):
    clock = 0.
    tau = V/q
    fact = dt/tau
    t = []
    c = []
    t.append(clock)
    c.append(c0)
    while(clock <= tf):
        clock += dt
        c.append(one_step(c[-1],q,V,dt))
        t.append(clock)
    return np.array(t),np.array(c)

def adaptive_euler(c0=c0,q=q,V=V,tf=tf,tol=1e-3):
    clock = 0.
    t = []
    c = []
    t.append(clock)
    c.append(c0)
    dt=1e-3
    no_steps = 0
    while (clock <= tf):
        toli=10*tol
        while(toli>tol):
            DT = dt
            #one large step
            ys = one_step(c[-1],q,V,dt)
            #two small steps
            k1 = one_step(c[-1],q,V,0.5*dt)
            y1 = one_step(k1,q,V,0.5*dt)
            toli = np.abs(ys-y1)
            dt = dt*np.sqrt(tol/toli)
            no_steps += 3 #one larg and two small
        clock += DT
        t.append(clock)
        c.append(2*y1-ys)
    print("No steps",no_steps)
    return np.array(t),np.array(c)


t, c = euler()
ca = analytical(t)



tad,cad = adaptive_euler()
ca2 = analytical (tad)


plt.plot(t,c,'*',label='euler scheme')
plt.plot(t,ca,label='analytical')
plt.plot(tad,cad,'*',label='adaptive euler scheme')
plt.grid()
plt.legend()
plt.show()

print("Numerical error Euler ",np.abs(ca[-1]-c[1]), "no steps",len(t))
print("Numerical error adaptive euler", )

            
            