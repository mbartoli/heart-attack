import os
import sys
import struct
import socket
import time
import select
import re
from optparse import OptionParser


options = OptionParser(usage='%prog file max', description='Test for SSL heartbleed vulnerability (CVE-2014-0160) on multiple domains, takes in Alexa top X CSV file')

def main():
    opts, args = options.parse_args()
    url  =  args[0]
    filename = "temp_spear.txt"
    wrt = "1,"+url+"\n"
    if os.path.isfile(filename):
        os.remove(filename)
    f = open(filename, 'a')
    f.write(wrt)
    f.close()

if __name__ == '__main__':
    main()

