const currentNumberwrapper = document.getElementById('currentNumber');
let cout = 0;

function increment() {
    cout++;
    currentNumberwrapper.innerHTML = cout;
}

function decrement() {
    cout--;
    currentNumberwrapper.innerHTML = cout;
}

// Boa idéia 