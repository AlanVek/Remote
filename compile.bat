pyinstaller Code/main.py --onefile --hidden-import="pynput.keyboard._win32" ^
--hidden-import="pynput.mouse._win32" -n "Remote" ^
--add-data "Code/Request_Handler/templates/HTML.html;Code/Request_Handler/templates" ^
--add-data "Code/Request_Handler/templates/css/style.css;Code/Request_Handler/templates/css" ^
--add-data "Code/Request_Handler/templates/js/Behavior.js;Code/Request_Handler/templates/js" ^
--add-data "Code/Request_Handler/templates/js/Keyboard.js;Code/Request_Handler/templates/js" ^
--add-data "Code/Request_Handler/templates/js/Mouse.js;Code/Request_Handler/templates/js" ^
--add-data "Code/Instructions.txt;Code" ^
--hidden-import "Code/Request_Handler/Handler.py" ^
--hidden-import "Code/Request_Handler/Pynput/keyDict.py" ^
--hidden-import "Code/Request_Handler/Pynput/mouseDict.py" ^
--exclude pandas --exclude numpy --exclude scipy --exclude PyQt5 ^
--exclude matplotlib --exclude PIL ^
--icon=Executable/Icon/Controller_Icon.ico

copy .\dist\Remote.exe .\Executable /Y