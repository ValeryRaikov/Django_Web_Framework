const buttonElement = document.getElementById('greet_btn');
const ownersBtnElement = document.getElementById('owners');

const h2Element = document.querySelector('.greet');
const ulListElement = document.querySelector('.owners-list');

buttonElement.addEventListener('click', () => {
    if (buttonElement.textContent === 'Click me!') {
        h2Element.style.display = 'block';
        buttonElement.textContent = 'Close';
    } else {
        h2Element.style.display = 'none';
        buttonElement.textContent = 'Click me!';
    }
});

ownersBtnElement.addEventListener('click', () => {
    if (ownersBtnElement.textContent === 'Show owners') {
        ulListElement.style.display = 'block';
        ownersBtnElement.textContent = 'Close';
    } else {
        ulListElement.style.display = 'none';
        ownersBtnElement.textContent = 'Show owners';
    }
});
