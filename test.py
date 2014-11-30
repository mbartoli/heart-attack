import sys

from optparse import OptionParser

options = OptionParser(usage='%prog file max', description='Test for SSL heartbleed vulnerability (CVE-2014-0160) on multiple domains, takes in Alexa top X CSV file')

(opts, args) = options.parse_args()
    
#if len(args) < 2:
#    print "error"


print opts, args