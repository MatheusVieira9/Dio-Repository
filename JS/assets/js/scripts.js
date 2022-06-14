const currentNumberwrapper = document.getElementById('currentNumber');
let cnumber = 0;


function increment() {
    cnumber++;
    currentNumberwrapper.innerHTML = cnumber;
}

function decrement() {
    cnumber--;
    currentNumberwrapper.innerHTML = cnumber;
}

// Boa idéia 