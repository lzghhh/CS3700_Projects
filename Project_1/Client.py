#!/usr/bin/env python3
import socket, threading, argparse

parser = argparse.ArgumentParser(description='Client Comm')
parser.add_argument('-p', '--port', type = int, metavar='', help='Server Port')
parser.add_argument('-s','--flag', type = int, metavar='', help='Server Port')
parser.add_argument('hostname', type = str, metavar='', help='The name of the server')
parser.add_argument('username', type = str, metavar='', help='Northeastern Username')
args = parser.parse_args()

if args.port is not None:
    PORT = args.port
else:
    PORT = 27993

if args.flag is not None:
    SEVER = args.flag
    if PORT == 27993:
        PORT = 27994
else:
    SERVER = socket.gethostbyname(socket.gethostbyname())

ADDR = (SERVER, PORT)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)




if __name__ == '__main__':
    print(args.port + args.flag)
    print(args.hostname + args.username)