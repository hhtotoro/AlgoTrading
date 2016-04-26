import threading
from WindPy import *
import datetime as dt
w.start()

def DemoWSQCallback(data):
    print "original data"
    print data
    print "new data"
    print gNewDataCome

if __name__ == "__main__":

    #print w.isconnected
    #data = w.wsi("000001.SZ", "mf_amt", "2016-04-25 09:00:00", "2016-04-26 13:30:37", "")
    #data = w.wsd("600000.SH", "mf_amt", "2016-03-27", "2016-04-25", "")
    #
    data = w.wsq("600000.SH",
          "rt_mf_amt,rt_bidvol,rt_askvol,rt_insti_vip_bid,rt_insti_vip_ask,rt_trans_sum_vol,rt_activenetin_amt")
    print data
    print gNewDataCome