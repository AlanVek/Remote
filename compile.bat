pyinstaller Code/main.py --onefile --hidden-import="pynput.keyboard._win32" ^
--hidden-import="pynput.mouse._win32" -n "Remote_Keyboard.exe" ^
--add-data "Code/Handler/templates/HTML.html;Code/Handler/templates" ^
--add-data "Code/Handler/templates/css/style.css;Code/Handler/templates/css" ^
--add-data "Code/Handler/templates/js/Behavior.js;Code/Handler/templates/js" ^
--add-data "Code/Handler/templates/js/Keyboard.js;Code/Handler/templates/js" ^
--add-data "Code/Handler/templates/js/Mouse.js;Code/Handler/templates/js" ^
--add-data "Code/Instructions.txt;Code" ^
--hidden-import "Code/Handler/Handler.py" ^
--hidden-import "Code/Handler/Pynput/keyDict.py" ^
--hidden-import "Code/Handler/Pynput/mouseDict.py" ^
--exclude pandas --exclude numpy --exclude scipy --exclude PyQt5 ^
--exclude matplotlib --exclude PIL

copy .\dist\Remote_Keyboard.exe .\Executable /Y