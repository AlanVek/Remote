# Networking
from http.server import HTTPServer
import platform

p = platform.system()

# Handler
from Request_Handler.Handler import RHandler, update_ip, resource_path, sys, join

if p == 'Windows':
    from socket import gethostname, gethostbyname
    from subprocess import Popen, PIPE
    import re

elif p == 'Linux':
    from subprocess import check_output
    import platform

else: sys.exit()

def print_instructions():
    with open (resource_path(join("Code", "Instructions.txt")), 'rb') as file: text = file.read()
    print(text.decode('utf-8'))

def get_network_name():
    if p == 'Windows':
        netshcmd = Popen('Netsh WLAN show interfaces', shell=True, stderr=PIPE, stdout=PIPE)
        output, errors = netshcmd.communicate()
        if errors: sys.exit(errors)
        else:
            try:
                output = output.decode('utf-8')
                wifinet = dict(map(str.strip, re.split('\s+:\s+', i)) for i in output.strip().splitlines() if i.startswith('    '))['Profile']
            except: wifinet = 'Network Not Found'
        return wifinet
    elif p == 'Linux':
        s = check_output(["iwgetid"]).decode('utf-8').split('ESSID:')[1]
        return s[1:s.rfind('"')]
    else: return 'Network Not Found'

def get_ip():
    if p == 'Windows': return gethostbyname(gethostname())
    elif p == 'Linux': return check_output(["hostname", "-I"]).decode('utf-8').split(' ')[0]
    else: return None

def main():

    # Gets local IP
    myIP = get_ip()
    RHandler.IP = myIP
    update_ip(RHandler)

    # Instructions
    if not '-I' in sys.argv: print_instructions()
    print(f"\nNetwork: {get_network_name()}\nIP:Port --> {myIP}:8000\n")

    # Creates server
    server = HTTPServer(server_address=('', 8000), RequestHandlerClass=RHandler)

    # Loops until 'Exit' is pressed
    try:
        while RHandler.running: server.handle_request()
    except KeyboardInterrupt: pass

    server.server_close()

if __name__ == '__main__':
    main()