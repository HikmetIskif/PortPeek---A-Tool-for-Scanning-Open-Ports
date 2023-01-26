#!/usr/bin/env python3
import socket
from datetime import datetime as dt
import sys

if len(sys.argv) == 4:
  target = socket.gethostbyname(sys.argv[1]) # translates host to ipv4
  firstport = int(sys.argv[2])
  lastport = int(sys.argv[3])
else:
  print("Improper use. The correct syntax is python3 port_scanner.py (ip) (first port) (last port)")

print("The target getting scanned: " + target)
print("Start time: " + str(dt.now()))
print('-' * 40)

try:
  for port in range(firstport,lastport):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
      print("port {} is open".format(port))
    s.close
except KeyboardInterrupt:
  print('Keyboard interrup detected, exitting..')
  sys.exit()
except socket.error:
  print("A problem occured when connecting to server")
  sys.exit()
except socket.gaierror:
  print("There was a problem when hostname was getting resolved")
  sys.exit()




print("Finished: " + str(dt.now()))
