import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

arrivingtime=np.random.uniform(0,10,size=20)
arrivingtime.sort()
workingtime=np.random.uniform(1,3,size=20)

startingtime=[0 for i in range(20)]
finishingtime=[0 for i in range(20)]
waitingtime=[0 for i in range(20)]
emptytime=[0 for i in range(20)]

print("arrivingtime\n",arrivingtime,"\n")
print("workingtime\n",workingtime,"\n")
print("startingtime\n",startingtime,"\n")
print("finishingtime\n",finishingtime,"\n")
print("waitingtime\n",waitingtime,"\n")
print("emptytime\n",emptytime,"\n")

startingtime[0]=arrivingtime[0]
finishingtime[0]=startingtime[0]+workingtime[0]
waitingtime[0]=startingtime[0]-arrivingtime[0]

print(startingtime[0])
print(finishingtime[0])
print(waitingtime[0])

for i in range(1,len(arrivingtime)):
    if finishingtime[i-1]>arrivingtime[i]:
        startingtime[i]=finishingtime[i-1]
    else:
        startingtime[i]=arrivingtime[i]
        emptytime[i]=arrivingtime[i]-finishingtime[i-1]
    finishingtime[i]=startingtime[i]+workingtime[i]
    waitingtime[i]=startingtime[i]-arrivingtime[i]
    print("第%d个人：到达时间 开始时间 “工作”时间 完成时间 等待时间\n" %i,
          arrivingtime[i],
          startingtime[i],
          workingtime[i],
          finishingtime[i],
          waitingtime[i],
          "\n")
print("average waiting time is %f" %np.mean(waitingtime))

sns.set(style='ticks',context="notebook")
fig=plt.figure(figsize=(8,6))
arrivingtime,=plt.plot(arrivingtime,label='arrivingtime')
startingtime,=plt.plot(startingtime,label='startingtime')
finishingtime,=plt.plot(finishingtime,label='finishingtime')
workingtime,=plt.plot(workingtime,label='workingtime')
waitingtime,=plt.plot(waitingtime,label='waitingtime')

plt.title(("Queuing problem random simulation experiment").title())
plt.xlabel("Arriving Time(min)")
plt.ylabel("Total Time(min)")
plt.legend(handles=[arrivingtime,startingtime,finishingtime,workingtime,waitingtime],loc='best')
plt.show()