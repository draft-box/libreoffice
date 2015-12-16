#!/usr/bin/python3

import os
import threading
import os.path
from timeit import Timer

def convert(infile, outfile, trans_type):
    for i in range(5):
        if trans_type == 1:
            print("trans use 2002 port")
            os.system("./DocumentConverter.py " + infile + " " + outfile)
        else:
            print("trans use 2003 port")
            os.system("./DocumentConverter2.py " + infile + " " + outfile)
    
def myRun(infile, outfile, trans_type):
    ti = Timer("convert(\"" + infile + "\",\"" + outfile + "\"," + str(trans_type) + ")", "from __main__ import convert")
    print("erase:%s" %  ti.repeat(3, 1))

class myThread (threading.Thread):
    def __init__(self, infile, outfile, trans_type):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile
        self.trans_type = trans_type
    def run(self):
        myRun(self.infile, self.outfile, self.trans_type)

threads = []

# 创建新线程
thread1 = myThread("2.doc", "2_1.pdf", 1)
thread2 = myThread("2.doc", "2_2.pdf", 2)

# 开启新线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()

print("Exiting Main Thread")
