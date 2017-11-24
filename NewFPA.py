import numpy as np
import math


def levy(d):
    lamda = 3 / 2
    sigma=(math.gamma(1+lamda)*math.sin(math.pi*lamda/2)/(math.gamma((1+lamda)/2)*lamda*(2**((lamda-1)/2))))**(1/lamda)
    u=np.random.randn(1,d)*sigma
    v=np.random.randn(1,d)
    step=u/abs(v)**(1/lamda)
    return 0.01*step

def checkbounds(s,lb,ub):
    for i in range(0,3):
        if s[i]<lb:
            s[i]=lb
        elif s[i]>ub:
            s[i]=ub
    return s


def function(x):
    y=(1-x[0])**2+100*(x[1]-x[0]**2)**2+100*(x[2]-x[1]**2)**2
    return y

def fpa():
    n=20
    p=0.8
    N_time=8000

    d=3
    lb=-5
    ub=5
    sol = np.ones((n, d))
    fitness = np.ones((n, 1))
    for i in range(0, n):
        sol[i,] = lb + (ub - lb) * np.random.rand(1, d)
        fitness[i, 0] = function(sol[i,])
    fmin = fitness.min(0)
    I=fitness.argmin(0)
    best = sol[I,]
    s=sol.copy()
    for t in range(0,N_time):
        for j in range(0,n):
            if np.random.random_sample()>p:
                s[j,]=s[j,]+levy(d)*(s[j,]-best)
            else:
                jk = np.random.permutation(n)
                while jk[0]==j or jk[1]==j:
                    jk = np.random.permutation(n)
                s[j,] =s[j,]+np.random.random_sample()*(sol[jk[0],]-sol[jk[1],])
            s[j,]=checkbounds(s[j,],lb,ub)
            fitnessNew = function(s[j,])
            if fitnessNew < fitness[j, 0]:
                fitness[j,0] = fitnessNew
                sol[j,]=s[j,]

            if fitnessNew < fmin:
                fmin = fitness[j,0]
                best = s[j,]
        print(best)
        print(fmin)








