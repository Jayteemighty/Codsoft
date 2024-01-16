// static/calc.js
function calculate(operation) {
    const inputField = document.getElementById('inputext');
    const currentInput = parseFloat(inputField.value);

    // Add logic to handle different operations and update the input field

    // Example: Send the calculation to the server using fetch
    fetch(`/calculate/${operation}/?num1=${currentInput}&num2=${parseFloat(inputField.value)}`)
        .then(response => response.json())
        .then(data => {
            if ('result' in data) {
                inputField.value = data.result;
            } else if ('error' in data) {
                console.error(data.error);
            }
        })
        .catch(error => console.error('Error:', error));
}

function Result() {
    // Handle the equal button logic if needed
}

// Add other JavaScript logic as needed
