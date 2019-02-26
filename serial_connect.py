#!usr/bin/python

#https://www.cnblogs.com/dongxiaodong/p/9992083.html

import serial
import sys
import os
import time
import re

try:
    #portx="COM3"
    portx = "/dev/ttyS0"
    bps=115200
    timex=5
    ser =serial.Serial(portx,bps,timeout=timex)

    result =ser.write("104B".encode("gbk"))
    print("写总字节数：",result)

    ser.close()

except Exception as e:
    print("--异常--：",e)