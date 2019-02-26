# coding:utf-8

import serial.tools.list_ports

plist = list(serial.tools.list_ports.comports())

if len(plist) <= 0:
    print("没有发现端口!")
else:
    plist_0 = list(plist[0])
    serialName = plist_0[0]
    serialFd = serial.Serial(serialName, 9600, timeout=60)
    print("可用端口名>>>", serialFd.name)

#错误1：PermissionError: [Errno 13] Permission denied: '/dev/ttyS0'

#hx-104b@hx104b-System-Product-Name:~/wheel$ sudo python serial_test.py
#可用端口名>>> /dev/ttyS0



