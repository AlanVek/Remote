from pynput import mouse

mouse_cont = mouse.Controller()

mouseDict = {
    "unknown": mouse.Button.unknown,
    "left": mouse.Button.left,
    "middle": mouse.Button.middle,
    "right": mouse.Button.right
}