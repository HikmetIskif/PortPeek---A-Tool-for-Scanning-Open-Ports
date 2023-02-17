#!/usr/bin/env python3

import socket
import sys
import argparse
import pyfiglet

def get_arguments():
    parser = argparse.ArgumentParser(description='portpeek - port scanner',
                                     usage=f'python3 {sys.argv[0]} -a <address> -c  '
                                           f'OR python3 {sys.argv[0]} -a <address> -r -s <startingport> -e <endingport> ',
                                     epilog=f'Example Usage - python3 {sys.argv[0]} -a 10.8.21.18 -c  '
                                            f'python3 {sys.argv[0]} -a 10.8.21.18 -r -s 52 -e 450')

    parser.add_argument('-a', '--address', metavar='address', dest='address', help='Enter the address')

    parser.add_argument('-c', '--common', action='store_true', help='Scans for common ports (ftp,ssh,telnet,'
                                                                    'smtp,dns,http,https,pop3,smb,Imap)')

    parser.add_argument('-r', '--ranged', action='store_true', help='Scans a spesific range.')

    parser.add_argument('-s', '--portstart', metavar='portstart', dest='portstart', help='Enter the starting port '
                                                                                         'if you want to scan a spesific range.')

    parser.add_argument('-e', '--portend', metavar='portend', dest='portend', help='Enter the ending port '
                                                                                       'if you want to scan a spesific range.')

    parser.add_argument('-q', '--quickness', metavar='quickness', dest='quickness', help='Select the quickness of the scan.'
                                                                                         'Faster scans may have inaccurate results.'
                                                                                         'Options are 1, 2, 3  with 1 being the slowest'
                                                                                         'and 3 being the fastest (default is 2.)')

    parser.add_argument('-v', '--verbose', action='store_true', help='Activates verbose to see which port is scanning at the moment.')

    args = parser.parse_args()

    if len(sys.argv) <= 3:
        parser.print_usage()
        sys.exit()


    return args

args = get_arguments()

header_text = "PORTPEEK"
header_ascii = pyfiglet.figlet_format(header_text)
print(header_ascii)
print("Welcome to PortPeek! Starting port scan...")

address = args.address

try:
    speed = int(args.quickness)
except TypeError:
    speed = 2
except ValueError:
    print("The input of quickness must be 1, 2 or 3 with 3 being the fastest and 1 being the slowest. Default is 2.")
    sys.exit()


if speed == 3:
    quickness = 0.5
elif speed == 2:
    quickness = 1
elif speed == 1:
    quickness = 1.5
elif speed != 3 and speed != 2 and speed != 1 :
    print("The levels of quickness are 1, 2 and 3. Other inputs are not accepted.")
    sys.exit()


common_ports = {"ftp" : 21 , "ssh" : 22 , "telnet" : 23 , "smtp"  : 25 , "dns" : 53 , "http" : 80 , "https" : 443 ,
                "pop3" : 110, "smb139": 139, "smb445" : 445 , "Imap" : 143}

def get_keys(value):
    keys = [k for k, v in common_ports.items() if v == value]
    return ', '.join(keys)

def common_ports_scan():
    try:
        for port in common_ports.values():
            if args.verbose:
                print(f"Scanning port {port}.")
            scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(quickness)
            outcome = scan.connect_ex((address, port))
            if outcome == 0:
                print(f"{get_keys(port)} port {port} is open.")
            scan.close
    except socket.error:
        print("There was a problem when connecting to target.")
        sys.exit()
    except KeyboardInterrupt:
        print("Keyboard interrupt detected, exitting..")
    except socket.gaierror:
        print("A problem occured when hostname was getting resolved.")

def ranged_port_scan():
    try:
        for port in range(portstart, portend + 1):
            if args.verbose:
                print(f"Scanning port {port}.")
            scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(quickness)
            outcome = scan.connect_ex((address, port))
            if outcome == 0:
                print(f"port {port} is open.")
            scan.close
    except socket.error:
        print("There was a problem when connecting to target.")
        sys.exit()
    except KeyboardInterrupt:
        print("Keyboard interrupt detected, exitting..")
    except socket.gaierror:
        print("A problem occured when hostname was getting resolved.")


if args.common:
    common_ports_scan()

if args.ranged:
    portstart = int(args.portstart)
    portend = int(args.portend)
    ranged_port_scan()

print("Finished.")
