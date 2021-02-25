/* Keywords */
const exit_string = "__exit__";
const keyboard = "__special__";
const key_separator = '__separator__';
const question = '__sign__';
/* Keywords */

const input = "input";
const go_string = "Go";

/* Keys */
const enter = 'enter';
const alt = 'alt';
const supr = 'delete';
const back = 'backspace';
const space = 'space';
const up = 'up';
const down = 'down';
const left = 'left';
const right = 'right';
const ctrl = 'ctrl';
const esc = 'esc';
const shft = 'shift';
const altf4 = 'alt+f4';
const voldown = 'media_volume_down';
const volup = 'media_volume_up';
//const voldown = 'volumedown';
//const volup = 'volumeup';
const cmd = 'cmd';

const hotkey = 'hotkey';

const myFunc = keyword => {

    const ip = 'http://192.168.0.96:8000/';                                                                                                
    let sender = ip;
    let x = new XMLHttpRequest();

    if (keyword === exit_string) sender += exit_string;
    else{
//        if (keyword === hotkey) sender += keyword;
        if (keyword !== go_string) sender += keyboard + keyword + key_separator;
        sender += document.getElementById(input).value;
    }

    sender = sender.replaceAll('?', question)

    x.open("GET", sender, true);
    x.send( null );
    document.getElementById(input).value = ''
};

