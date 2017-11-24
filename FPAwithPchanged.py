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


def levy(d):
    lamda = 1.5
    sigma = (math.gamma(1 + lamda) * math.sin(math.pi * lamda / 2) / (
    math.gamma((1 + lamda) / 2) * lamda * (2 ** ((lamda - 1) / 2)))) ** (1 / lamda)
    # sigma = 0.6965745025576968
    u = np.random.randn(1, d) * sigma
    v = np.random.randn(1, d)
    step = u / abs(v) ** (1 / lamda)
    return 0.01 * step


def simple(s, lb, ub, d):
    ns_tmp = s
    for i in range(0, d):
        if ns_tmp[i] < lb:
            ns_tmp[i] = lb
        if ns_tmp[i] > ub:
            ns_tmp[i] = ub
    return ns_tmp


def fpa(n, p, N_iter, lb, ub, d,f):
    sol = np.ones((n, d))
    fitness = np.ones((n, 1))
    for i in range(0, n):
        sol[i,] = lb + (ub - lb) * np.random.rand(1, d)
        fitness[i, 0] = fun(sol[i,], d,f)
    fmin, I = fitness.min(0), fitness.argmin(0)
    best = sol[I,]
    S = sol.copy()

    for t in range(0, N_iter):
        for i in range(0, n):
            p=0.8-0.6*t/N_iter
            if np.random.random() < p:
                L = levy(d)
                S[i,] = sol[i,] + L * (sol[i,] - best)
            else:
                epsilon = np.random.random_sample()
                jk = np.random.permutation(n)
                S[i,] = S[i,] + epsilon * (sol[jk[0],] - sol[jk[1],])
            S[i,] = simple(S[i,], lb, ub, d)
            Fnew = fun(S[i,], d,f)
            if Fnew <= fitness[i]:
                sol[i,] = S[i,]
                fitness[i] = Fnew
            if Fnew <= fmin:
                best = S[i,]
                fmin = Fnew
            if t % 100 == 0:
                print(best)
                print(fmin)
                print(t)
            # if fmin < 10 ** -10:
            #     # print(t)
            #     return t+1
            # elif t==N_iter-1:
            #     return t+1

    print("best:")
    print(best)
    print("fmin")
    print(fmin)
