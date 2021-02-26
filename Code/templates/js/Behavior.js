
let form = document.getElementById("myForm");
form.addEventListener('submit', event => event.preventDefault());

let meta = document.createElement('meta');
meta = Object.assign(meta,{
    name: 'viewport',
    content: 'width=device-width,height=' + window.innerHeight + ', initial-scale=1.0'
});

document.getElementsByTagName('head')[0].appendChild(meta);

document.addEventListener('touchmove', event => event.preventDefault(), false);

const _focus = () => document.getElementById("input").focus();

window.addEventListener('touchstart', startMoving);

function startMoving() {
    window.removeEventListener('touchstart', startMoving);
    window.addEventListener('touchmove', move);
    window.addEventListener('touchend', removeEvent);
}
