import re
import operator
import sys

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
		# send this information to screen or perhaps a file. Eventually a server.
		print "%s, %s" %(sourceMac,destSSID)
	else:
		print "failed to parse for line %s" % (line)


