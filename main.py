import NewFPA
import numpy as np
import math
import FPA
import matplotlib.pyplot as plt
import tFPA
import OPFPA
import  SInCos
import CSINCOS
import benchmark

# print(SInCos.sca(0.8,20,3,-5,5,1,3000))
# print('-----------------')
# print(FPA.fpa(20,0.8,3000,-5,5,3))


times=3000
# x=[]
# y=FPA.fpa(20, 0.8, times,-5,5,30)
# for i in range(times):
#     x.append(i)
#
#
#
#
#
# plt.figure(figsize=(8,4)) #创建绘图对象
# plt.plot(x,y,"b--",linewidth=1)   #在当前绘图对象绘图（X轴，Y轴，蓝色虚线，线宽度）
# plt.xlabel("Time(s)") #X轴标签
# plt.ylabel("Fitness")  #Y轴标签
# plt.title("折线图") #图标题
# plt.show()  #显示图

# zz=0
# for i in range(0,10):
#     zz=zz+OPFPA.fpa(20, 0.8, times,-5,5,3)
# print(zz/10)
# for i in range(0,10):
#     zz=zz+OPFPA.fpa(20, 0.8, times,-5,5,3)
# print(zz/20)
# for i in range(0,10):
#     zz=zz+OPFPA.fpa(20, 0.8, times,-5,5,3)
# print(zz/30)
# for i in range(0,10):
#     zz=zz+OPFPA.fpa(20, 0.8, times,-5,5,3)
# print(zz/40)

#df=SInCos.sca(0.8, 20, 3000, -5, 5, 1, 8000)
#OPFPA.fpa(20, 0.8, 8000,-5,5,3)


# zz=0
# pp=[]
# for i in range(0,10):
#     df=SInCos.sca(0.8, 20, 1000, -5, 5, 1, 8000)
#     zz=zz+df
# print(zz/10)
# for i in range(0,10):
#     df = SInCos.sca(0.8, 20, 1000, -5, 5, 1, 8000)
#     zz = zz + df
# print(zz/20)
# for i in range(0,10):
#     df = SInCos.sca(0.8, 20, 1000, -5, 5, 1, 8000)
#     zz = zz + df
# print(zz/30)
# print(sorted(pp))

# zz=0
# pp=[]
# for i in range(0,10):
#     df=OPFPA.fpa(20, 0.8, times,-5,5,3)
#     zz=zz+df
#     pp.append(df)
# print(zz/10)
# for i in range(0,10):
#     df = OPFPA.fpa(20, 0.8, times,-5,5,3)
#     zz = zz + df
#     pp.append(df)
# print(zz/20)
# for i in range(0,10):
#     df = OPFPA.fpa(20, 0.8, times,-5,5,3)
#     zz = zz + df
#     pp.append(df)
# print(zz/30)
# print(sorted(pp))

# df = SInCos.sca(0.8, 20, 20, -5, 5, 1, 8000,2)
FPA.fpa(20,0.8,10000,-4,8,2,11)
# benchmark.benchmark()
