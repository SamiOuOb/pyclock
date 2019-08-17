import sys
import time, datetime
import gc
import os

n0=([1,1,1],[1,0,1],[1,0,1],[1,0,1],[1,1,1])
n1=([1,1,0],[0,1,0],[0,1,0],[0,1,0],[1,1,1])
n2=([1,1,1],[0,0,1],[1,1,1],[1,0,0],[1,1,1])
n3=([1,1,1],[0,0,1],[1,1,1],[0,0,1],[1,1,1])
n4=([1,0,1],[1,0,1],[1,1,1],[0,0,1],[0,0,1])
n5=([1,1,1],[1,0,0],[1,1,1],[0,0,1],[1,1,1])
n6=([1,1,1],[1,0,0],[1,1,1],[1,0,1],[1,1,1])
n7=([1,1,1],[1,0,1],[1,0,1],[0,0,1],[0,0,1])
n8=([1,1,1],[1,0,1],[1,1,1],[1,0,1],[1,1,1])
n9=([1,1,1],[1,0,1],[1,1,1],[0,0,1],[1,1,1])
n10=([0,0,0],[0,0,0],[1,1,1],[0,0,0],[0,0,0])
n11=([0,0,0],[0,1,0],[0,0,0],[0,1,0],[0,0,0])
n12=([0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0])
number=[n0,n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12]
temp=[]
timeM2=[]
sentence='9487 又是快樂的一天 Yeeeeeeee'

while(1):
    localtime = time.localtime(time.time())
    timeM=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    timeM = list(filter(str.isdigit, timeM))

    timeM.insert(4,12)
    timeM.insert(7,10)
    timeM.insert(10,12)

    timeM.insert(13,11)
    timeM.insert(16,11)

    if(timeM2!=timeM):
        os.system("cls")
        for r in range(5):
            for n in range(19):
                print(' ',end=' ')
                for l in range(3):
                    if(number[int(timeM[n])][r][l]==1):
                        print('▓',end=' ')
                    else:
                        print(' ',end=' ')
                if(n==13):
                    print(' ',end=' ')
            print('\n')
            temp=[]
        print(sentence)
        time.sleep(0.25)
        timeM2=timeM








