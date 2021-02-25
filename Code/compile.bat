pyinstaller ./main.py --onefile --hidden-import="pynput.keyboard._win32" ^
--hidden-import="pynput.mouse._win32" -n "Remote_Keyboard.exe" ^
--add-data "./templates/HTML.html;./templates" ^
--add-data "./templates/css/style.css;./templates/css" ^
--add-data "./templates/js/Behavior.js;./templates/js" ^
--add-data "./templates/js/Networking.js;./templates/js" ^
--add-data "./Instructions.txt;." ^
--hidden-import "./Handler.py" ^
--hidden-import "./keyDict.py" ^
--exclude pandas --exclude numpy --exclude scipy --exclude PyQt5 ^
--exclude matplotlib --exclude PIL
cd..
copy .\Code\dist\Remote_Keyboard.exe .\Executable /Y