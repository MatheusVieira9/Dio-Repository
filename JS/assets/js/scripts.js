const currentNumberwrapper = document.getElementById('currentNumber');
let cnumber = 0;


function increment() {
    if (cnumber < 10){
        cnumber++;
        currentNumberwrapper.innerHTML = cnumber;
    }
}

function decrement() {
    if (cnumber > -10){
    cnumber--;
    currentNumberwrapper.innerHTML = cnumber;   
    }
}
