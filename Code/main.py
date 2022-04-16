# Networking
from http.server import HTTPServer
import platform

p = platform.system()

# Handler
from Request_Handler.Handler import RHandler, update_ip, sys

if p == 'Windows':
    from socket import gethostname, gethostbyname
    from subprocess import Popen, PIPE
    import re

elif p == 'Linux':
    from subprocess import check_output
    import platform

else: sys.exit()

def print_instructions():
    from textwrap import dedent
    print(
        dedent(
            """
            ******************************************************************
                Remote (Alan Vekselman, Natán Vekselman - 2021)
            ******************************************************************

            ******************************************************************
            * After the instructions, the terminal will display network and
            * IP:Port to which the user must connect using any web browser. 
            * Both phone and computer must be connected to the same network.
            ******************************************************************
            * To enter text, the user must write it in the text-input slot and
            * press "Send".
            ******************************************************************
            * To use hotkeys (ctrl), the user must write the second key in the
            * text-input slot and press the special key.

            Example: 

            Objective: ctrl+v

            Steps: Write 'v' (or 'V') and press 'ctrl'.
            ******************************************************************
            * For special keys (except ctrl), all the text written in the
            * text-input slot will be written in the computer before pressing
            * said key.

            Example: 

            Objective: 'Hello' + enter

            Steps: Write 'Hello' and press 'Enter'.
            ******************************************************************
            * While the checkbox "Alt" is checked, 'alt' will be held down
            * (the intention is to use, for example, in combination with 'tab'
            * to change tabs).
            ******************************************************************
            * While the checkbox "Lclick" is checked, the left click will be
            * held down. To click, touch the word Lclick (not the checkbox).
            ******************************************************************
            * Press "Exit" to close the program in the computer.
            ******************************************************************
            """
        )
    )

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