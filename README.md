# PortPeek
A tool for scanning open ports of the target.

>**USAGE**
PortPeek has 2 ways of scan:
1-Scan for common ports (Scans for common ports (ftp, ssh, telnet, smtp, dns ,http, https, pop3, smb, Imap)
2-Scan the range limited by user.

**Scan for Common Ports**
python3 portpeek.py -a (address) -c

**Scan a Spesific Range**
python3 portpeek.py -a (address) -r -s (the starting port) -e (the ending port)

**Setting the Speed of Scan**
PortPeek has 3 speed levels. Level 1 is the slowest and level 3 is the fastest. Default is 2. Scanning faster increases chance of getting inaccurate result.

python3 portpeek.py -a (address) -c -q (speed level)

python3 portpeek.py -a (address) -r -s (the starting port) -e (the ending port) -q (speed level)

**Verbose Mode**
In order to see what port is scanning at the moment, PortPeek can be run on verbose mode. Adding -v activates verbose mode.

python3 portpeek.py -a (address) -c -q (speed level) -v

python3 portpeek.py -a (address) -r -s (the starting port) -e (the ending port) -q (speed level) -v
