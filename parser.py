import re
import operator
import sys
import time
import datetime
import mysql.connector

# cnx = mysql.connector.connect(user='scott', database='employees')
# setup mysql connection

time.sleep(5)
# wait for airodump-ng initialization

pattern=r"\s*(?P<sourceMac>([0-9A-Fa-f]{2}[:]){5}([0-9A-Fa-f]{2})|(\(not associated\)))\s+(?P<destMac>([0-9A-Fa-f]{2}[:]){5}([0-9A-Fa-f]{2}) | (\(not associated\)))(?P<PWR>\s+)\d+(?P<RATE>\s+\d+-\d+)\s+(?P<LOST>\d+)\s+(?P<PACKETS>)\d+(\s+(?P<destSSID>\w+)|)"
cpn=re.compile(pattern)

for line in sys.stdin:
	
	line = line.rstrip()
	sniffResult = cpn.match(line)

	if sniffResult is not None:
		sourceMac = sniffResult.group('sourceMac')
		destMac = sniffResult.group('destMac')
		PWR = sniffResult.group('PWR')
		RATE = sniffResult.group('RATE')
		LOST = sniffResult.group('LOST')
		PACKETS = sniffResult.group('PACKETS')
		destSSID = sniffResult.group('destSSID')
		timeStamp = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
		# send this information to screen or perhaps a file. Eventually a server.
		print "%s, %s, %s" %(sourceMac,destSSID, timeStamp)

	else:
		print "failed to parse for line %s" % (line)


