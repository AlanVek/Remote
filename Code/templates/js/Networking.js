/* Keywords */
const exit_string = "CodeEscape_Exit";
const keyboard = "keyboard.Key.";
const key_separator = '?';
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
const altf4 = 'altf4';

const myFunc = keyword => {

    const ip = 'http://192.168.0.96:8000/';                              
    let sender = ip;
    let x = new XMLHttpRequest();

    if (keyword === exit_string) sender += exit_string;
    else{
        if (keyword !== go_string) sender += keyboard + keyword + key_separator;
        sender += document.getElementById(input).value;
    }

    console.log(sender);

    x.open("GET", sender, true);
    x.send( null );
    document.getElementById(input).value = ''
};