import numpy as np
import math


def fun(u, d,f):
    selectedFunction = f
    z = 0
    if selectedFunction==1:
        for i in range(0,d-1):
            z = z+(u[i]-1) ** 2 + 100 * (u[i+1] - u[i] ** 2) ** 2
    elif selectedFunction==2:
        for i in range(0,d):
            z=z+u[i]**2
    elif selectedFunction==3:
        for i in range(0, d):
            z = z + u[i] ** 2 - 10 * math.cos(2 * math.pi * u[i]) + 10
    elif selectedFunction==4:
        fsum=0
        fproduct=1
        for i in range(0,d):
            fsum=fsum+abs(u[i])
            fproduct=fproduct*abs(u[i])
        z=fsum+fproduct
    elif selectedFunction==5:
        z=(math.sin(math.sqrt(u[0]**2+u[1]**2))**2-0.5)/(1+0.001*(u[0]**2+u[1]**2))**2-0.5
    elif selectedFunction==6:
        for i in range(0,5):
            z=z+1/(i+1+(u[i]-1)**2)
        z=(z+0.01)**-1
    elif selectedFunction==7:
        p1=0
        p2=0
        for i in range(0,d):
            p1=p1+u[i]**2
            p2=p2+(i+1)*u[i]
        z=p1+(0.5*p2)**2+(0.5*p2)**4
    elif selectedFunction==8:
        p1=0
        p2=0
        for i in range(0,d):
            p1=p1+u[i]**2
            p2=p2+math.cos(2*math.pi*u[i])
        z=-20*math.exp(-0.2*math.sqrt(1/d*p1))-math.exp(1/d*p2)+20+math.e
    elif selectedFunction==9:
        p1 = 0
        p2 = 1
        for i in range(0, d):
            p1=p1+u[i]**2
            p2=p2*math.cos(u[i]/math.sqrt(i+1))
        z=1+1/40000*p1-p2
    elif selectedFunction==10:
        z=u[0]**2+u[1]**2-math.cos(18*u[0])-math.cos(18*u[1])
    return z

def sca(w,n,d,lb,ub,a,N_iter,f):
    fmincol = []
    sol = np.ones((n, d))
    soltemp = sol.copy();
    OX = np.ones((n, d))
    fitness = np.ones((2 * n, 2))
    r2 = np.random.random_sample()*2*math.pi
    r3 = np.random.random_sample() * 2
    r4 = np.random.random_sample()
    for i in range(0, n):
        for j in range(0, d):
            soltemp[i, j] = lb + (ub - lb) * np.random.random_sample()
        fitness[i, 0] = fun(soltemp[i,], d,f)
    for i in range(0, n):
        for j in range(0, d):
            OX[i, j] = (ub + lb) - soltemp[i, j]

    for i in range(0, n):
        fitness[i, 0] = fun(soltemp[i,], d,f)
        fitness[i, 1] = i
    for i in range(n, 2 * n):
        fitness[i, 0] = fun(OX[i - 20,], d,f)
        fitness[i, 1] = i
    newFit = fitness[np.lexsort(fitness[:, ::-1].T)]
    for i in range(0, n):
        fitness[i, 0] = newFit[i, 0]

    for i in range(0, n):
        index = int(fitness[i, 1])
        if index < 20:
            sol[i,] = soltemp[index,]
        else:
            sol[i,] = OX[index - 20,]
    best = sol[0,]
    fmin = fitness[0, 0]

    S = sol.copy()


    for t in range(0,N_iter):
        r1=a-a*t/N_iter
        w=0.8-0.7*t/N_iter
        for i in range(0,n):
            if r4<0.5:
                S[i,]=w*sol[i,]+r1*math.sin(r2)*abs(r3*best-sol[i,])
            else:
                S[i,] = w*sol[i,] + r1 * math.cos(r2) * abs(r3 * best - sol[i,])
            Fnew = fun(S[i,], d,f)
            if Fnew <= fitness[i,0]:
                sol[i,] = S[i,]
                fitness[i] = Fnew
            if Fnew <= fmin:
                best = S[i,]
                fmin = Fnew
            if fmin<10**-10:
                print(best)
                print(fmin)
                print(t)
                #return t
            # elif t==N_iter-1:
            #     return t
    print("best:")
    print(best)
    print("fmin")
    print(fmin)



