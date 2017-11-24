import time
import FPA
import FPAwithPchanged
import OPFPA
import SInCos
import tFPA

def benchmark():
    start = time.time()
    ###############################
    times=0
    for function in range(1,11):
        if function == 6:
            continue
        funtimes=0
        imax=5
        for i in range(0, imax):
            #currenttime=tf.sca(0.8, 20, 3, -5, 5, 1, 8000,function)
            currenttime=FPA.fpa(20, 0.8, 8000, -5, 5, 5, function)+1
            times=times+currenttime
            funtimes=funtimes+currenttime
            print('函数{p1}第{p2}次迭代次数为{p3}'.format(p1=function, p2=i,p3=currenttime))
        funtimes=funtimes/imax
        print('{functionname}达到精度所需次数： {maxt}'.format(functionname=function, maxt=funtimes))
    print('所有函数各十次所需次数： {allmaxt}'.format(allmaxt=times))
    end = time.time()
    print(end-start)
