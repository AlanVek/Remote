
const ip = 'http://192.168.0.96:8000/';                                          

const myFunc = keyword => {

    let sender = ip;
    let x = new XMLHttpRequest();

    if (keyword === exit_string){
        sender += exit_string;
        document.getElementById("checkbox").checked = false;
    }
    else{
        if (keyword.indexOf(hotkey) !== -1) sender += keyword;
        else if (keyword.indexOf(mouse) !== -1 || keyword.indexOf(mouseclick) !== -1) sender += keyword;
        else{
            if (keyword !== go_string) sender += keyboard + keyword + key_separator;
            sender += document.getElementById(input).value;
        }
    }

    sender = sender.replaceAll('?', question)

    x.open("GET", sender, true);
    x.send( null );
    document.getElementById(input).value = ''
};

/* Keywords */
const exit_string = "__exit__";
const keyboard = "__special__";
const key_separator = '__separator__';
const question = '__sign__';
const mouse = '__mouse__';

const input = "input";
const go_string = "Go";

/* Keys */
const enter = 'enter';
const supr = 'delete';
const back = 'backspace';
const space = 'space';
const up = 'up';
const down = 'down';
const left = 'left';
const right = 'right';
const ctrl = 'ctrl';
const esc = 'esc';
const altf4 = 'alt+f4';
const voldown = 'media_volume_down';
const volup = 'media_volume_up';
const cmd = 'cmd';
const tab = 'tab';
const wintab = 'cmd+tab';
const rclick = 'right';
const lclick = 'left';
const mouseclick = '__click__';

const checkbox = "__checkbox__";
const hotkey = '__hotkey__';




