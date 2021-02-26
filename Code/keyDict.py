from pynput import keyboard
from ctypes import ArgumentError

key_cont = keyboard.Controller()

class __defDict(dict):
    def __init__(self, *args, **kwargs):
        if 'function' in kwargs: self.function = kwargs.pop('function')
        else: self.function = lambda v: v
        super().__init__(*args, **kwargs)

    def __getitem__(self, item):
        if not item in self: super().__setitem__(item, self.function(item))
        return super().__getitem__(item)

keyDict = __defDict({
    "alt": keyboard.Key.alt,
    "alt_l": keyboard.Key.alt_l,
    "alt_r": keyboard.Key.alt_r,
    "alt_gr": keyboard.Key.alt_gr,
    "backspace": keyboard.Key.backspace,
    "caps_lock": keyboard.Key.caps_lock,
    "cmd": keyboard.Key.cmd,
    "cmd_l": keyboard.Key.cmd_l,
    "cmd_r": keyboard.Key.cmd_r,
    "ctrl": keyboard.Key.ctrl,
    "ctrl_l": keyboard.Key.ctrl_l,
    "ctrl_r": keyboard.Key.ctrl_r,
    "delete": keyboard.Key.delete,
    "down": keyboard.Key.down,
    "end": keyboard.Key.end,
    "enter": keyboard.Key.enter,
    "esc": keyboard.Key.esc,
    "f1": keyboard.Key.f1,
    "f2": keyboard.Key.f2,
    "f3": keyboard.Key.f3,
    "f4": keyboard.Key.f4,
    "f5": keyboard.Key.f5,
    "f6": keyboard.Key.f6,
    "f7": keyboard.Key.f7,
    "f8": keyboard.Key.f8,
    "f9": keyboard.Key.f9,
    "f10": keyboard.Key.f10,
    "f11": keyboard.Key.f11,
    "f12": keyboard.Key.f12,
    "f13": keyboard.Key.f13,
    "f14": keyboard.Key.f14,
    "f15": keyboard.Key.f15,
    "f16": keyboard.Key.f16,
    "f17": keyboard.Key.f17,
    "f18": keyboard.Key.f18,
    "f19": keyboard.Key.f19,
    "f20": keyboard.Key.f20,
    "home": keyboard.Key.home,
    "left": keyboard.Key.left,
    "page_down": keyboard.Key.page_down,
    "page_up": keyboard.Key.page_up,
    "right": keyboard.Key.right,
    "shift": keyboard.Key.shift,
    "shift_l": keyboard.Key.shift_l,
    "shift_r": keyboard.Key.shift_r,
    "space": keyboard.Key.space,
    "tab": keyboard.Key.tab,
    "up": keyboard.Key.up,
    "media_play_pause": keyboard.Key.media_play_pause,
    "media_volume_mute": keyboard.Key.media_volume_mute,
    "media_volume_down": keyboard.Key.media_volume_down,
    "media_volume_up": keyboard.Key.media_volume_up,
    "media_previous": keyboard.Key.media_previous,
    "media_next": keyboard.Key.media_next,
    "insert": keyboard.Key.insert,
    "menu": keyboard.Key.menu,
    "num_lock": keyboard.Key.num_lock,
    "pause": keyboard.Key.pause,
    "print_screen": keyboard.Key.print_screen,
    "scroll_lock": keyboard.Key.scroll_lock
}, function = keyboard.KeyCode.from_char)

def hotkey(*args):
    try:
        for arg in args: key_cont.press(keyDict[arg])
        for arg in reversed(args): key_cont.release(keyDict[arg])
    except ArgumentError: pass
