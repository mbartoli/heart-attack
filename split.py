import array
import os
import csv
import sys
import struct
import socket
import time
import select
import re
from optparse import OptionParser

options = OptionParser(usage='%prog file max', description='Test for SSL')


def main():
	temp1 = 1
	opts, args = options.parse_args()
	filename = args[0]
	splitnum = args[1]
	print args[0]
	print args[1]
	for x in range (1, int(splitnum)+1):
		newfilename = "segment"+str(temp1)+".txt"
		if os.path.isfile(newfilename):
			os.remove(newfilename)
		ofile = open(newfilename, 'wb')
		writer = csv.writer(ofile, delimiter=',')
		
		with open(filename, 'rb') as csvfile:
			reader = csv.reader(csvfile, delimiter=',')
			rownum = 0 
			for row in reader:
				if (rownum % int(splitnum))+1 == temp1:
					writer.writerow(row)
				rownum += 1
	
		ofile.close()
		
		#print newfilename
		print "test # " + str(temp1)
		temp1 += 1
	
	
if __name__ == '__main__':
	main()
