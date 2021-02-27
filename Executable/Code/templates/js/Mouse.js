let joystick = document.getElementById("joystick");

const centerX = window.innerWidth * 0.5;
const centerY = window.innerHeight * 750/1000;
const radius = 165/1000 * window.innerHeight;
const radius_ball = 55 /1000 * window.innerHeight;

let posy = 0;
let posx = 0;

function move(e) {

    let distX = (-centerX + e.touches[0].clientX);
    let distY = (-centerY + e.touches[0].clientY);

    let distAbs = Math.sqrt(Math.pow(distX, 2) + Math.pow(distY, 2));

    if (distAbs > radius){
        let arg = Math.atan2(distY, distX);

        posx = centerX + Math.cos(arg) * radius - radius_ball;
        posy = centerY + Math.sin(arg) * radius - radius_ball;
    }
    else{

        posx = (e.touches[0].clientX-radius_ball);
        posy = (e.touches[0].clientY-radius_ball);

    }

    joystick.style.left = posx.toString();
    joystick.style.top = posy.toString();

    let porc_x = (posx - centerX) / radius;
    let porc_y = (posy - centerY + radius_ball) / radius;
    myFunc(mouse + '-x=' + porc_x.toString() + 'y=' + porc_y.toString());
}

function removeEvent() {
    window.removeEventListener('touchmove', move);
    joystick.style.top = "64vh";
    joystick.style.left = 'calc(50vw - 5.5vh)';
    window.addEventListener('touchstart', startMoving);
}

