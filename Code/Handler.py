# Networking
from http.server import BaseHTTPRequestHandler

# Keyboard
from keyDict import *

# URL parsing
from urllib.parse import unquote

# PyInstaller patches
import sys
from os.path import abspath, join

# Keywords
KEYWORD_KEY = '__special__'
KEY_SEPARATOR = '__separator__'
QUESTION = '__sign__'
KEYWORD_EXIT = '__exit__'
# HOTKEY = 'hotkey'

# Workaround for PyInstaller dependencies.
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = abspath(".")

    return join(base_path, relative_path)

# Updates Behaviour.js with current IP for requests.
def update_ip(cls):
    with open(resource_path('.\\templates\\js\\Networking.js'), 'rt') as file: data = file.read()

    data = data.replace(data[data.find('const ip =') : data.find('const ip =') + 39], f"const ip = 'http://{cls.IP}:8000/'; ")
    with open(resource_path('.\\templates\\js\\Networking.js'), 'wt') as file: file.write(data)

# Class RHandler for server.
class RHandler(BaseHTTPRequestHandler):

    running = True

    # Project files
    files = {
        'html' : '',
        'js_beh' : '',
        'js_net' : '',
        'css' : ''
    }

    # Sends response to client
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        #self.send_header('Access-Control-Allow-Origin', RHandler.IP)
        self.end_headers()

    # GET handling
    def do_GET(self):
        self._set_response()

        # Checks request for HTML
        if self.req_file(posible = ['/', '/HTML.html', ], variable = 'html', location = 'HTML.html'): pass

        # Checks requets for CSS
        elif self.req_file(posible = ['/css/style.css'], variable = 'css', location = 'css\\style.css'): pass

        # Checks requst for JS Behaviour
        elif self.req_file(posible = ['/js/Behavior.js'], variable = 'js_beh', location = 'js\\Behavior.js'): pass

        # Checks requst for JS Networking
        elif self.req_file(posible = ['/js/Networking.js'], variable = 'js_net', location = 'js\\Networking.js'): pass

        elif 'alt+f4' in self.path:
            hotkey('alt', 'f4')

        # elif 'hotkey' in self.path:
        #     print(self.path)
        #     pos = self.path.find('hotkey')
        #     hotkey(*self.path[pos + 6 : ].split('+'))

        # Checks special/repeat keys
        elif KEYWORD_KEY in self.path:
            pos = self.path.rfind(KEY_SEPARATOR)

            maybe_special = self.path[self.path.find(KEYWORD_KEY) + len(KEYWORD_KEY) : pos]

            # Special key handling
            if maybe_special in ['ctrl', 'alt', 'shift']: self.special_key(pos = pos, maybe_special = maybe_special)

            # Repeat key handling
            else: self.repeat_key(pos = pos)

        # Text input handling
        else: self.just_text()

    # Input parser from URL to usable info
    def path_parser(self):
        return unquote(self.path[1:].replace('favicon.ico', '')).replace(QUESTION, '?')

    # Prevents server from logging output
    def log_message(self, format, *args):
        return

    # Loads file and writes it to client
    def req_file(self, posible : [list[str], tuple[str]], variable : str, location : str):

        # Checks if path is one of the posibilities
        if self.path in posible:

            # Checks if file has already been loaded
            if not len(self.files[variable]):

                # Loads file in its key from self.files
                with open(resource_path(f'.\\templates\\{location}'), 'rt') as file: self.files[variable] = file.read()

            # Writes output to client
            self.wfile.write(self.files[variable].encode('utf-8'))
            return True

        return False

    # Special key handling
    def special_key(self, pos : int, maybe_special : str):

        # Checks if special key comes with extra letter
        try: key_letter = self.path[pos + len(KEY_SEPARATOR) : ].lower()
        except IndexError: key_letter = False

        # presses and releases (Hot)Key.
        if key_letter: hotkey(
           maybe_special,
            key_letter
        )
        else: controller.tap(keyDict[maybe_special])

    # Repeat key handling
    def repeat_key(self, pos : int):

        # Translates repeat key
        key = keyDict[self.path[self.path.find(KEYWORD_KEY) + len(KEYWORD_KEY) : pos]]
        self.path = self.path[pos + len(KEY_SEPARATOR) - 1 : ]

        self.just_text()

        # Taps key
        controller.tap(key)

    # Text input handling
    def just_text(self):

        # Input parser from path
        word = self.path_parser()

        # If word matches exit sequence, sets running flag to False
        if word == KEYWORD_EXIT: RHandler.running = False

        # If word doesn't match exit sequence, types word
        else: controller.type(word)


