# Networking
from http.server import HTTPServer
from socket import gethostname, gethostbyname
from subprocess import Popen, PIPE
import re

# Handler
from Request_Handler.Handler import RHandler, update_ip, resource_path, sys

def print_instructions():
    with open (resource_path("Code\\Instructions.txt"), 'rb') as file: text = file.read()
    print(text.decode('utf-8'))

def get_network_name():
    netshcmd = Popen('Netsh WLAN show interfaces', shell=True, stderr=PIPE, stdout=PIPE)
    output, errors = netshcmd.communicate()
    if errors: sys.exit(errors)
    else:
        try:
            output = output.decode('utf-8')
            wifinet = dict(map(str.strip, re.split('\s+:\s+', i)) for i in output.strip().splitlines() if i.startswith('    '))['Profile']
        except: wifinet = 'Network Not Found'

    return wifinet

if __name__ == '__main__':

    # Gets local IP
    myIP = gethostbyname(gethostname())
    RHandler.IP = myIP
    update_ip(RHandler)

    # Instructions
    if not '-I' in sys.argv: print_instructions()
    print(f"\nNetwork: {get_network_name()}\nIP:Port --> {myIP}:8000\n")

    # Creates server
    server = HTTPServer(server_address=('', 8000), RequestHandlerClass=RHandler)

    # Loops until 'Exit' is pressed
    while RHandler.running: server.handle_request()
    server.server_close()

