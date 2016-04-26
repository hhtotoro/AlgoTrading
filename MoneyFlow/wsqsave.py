import threading
from WindPy import *
import time
w.start()

#define the callback function
def myCallback(indata):
    print time.ctime()
    if indata.ErrorCode!=0:
        print('error code:'+str(indata.ErrorCode)+'\n')
        return()

    global begintime
    lastvalue =""
    for k in range(0,len(indata.Fields)):
         #print indata.Fields[k]
         if(indata.Fields[k] == "RT_MF_AMT"):
            lastvalue = str(indata.Data[k][0])

    string =  lastvalue +"\n"
    print string

    #call pf.close() after w.cancelRequest
    #pf.close();



exit=False

class feeder(threading.Thread):
    def __init__(self,threadID,name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        w.start()
        w.wsq("600000.SH","rt_mf_amt",func=myCallback)
#to subscribe if14.CFE

thread1 =feeder(1,"feder-1")
thread1.start()
while(1):
    if (exit):
        break;