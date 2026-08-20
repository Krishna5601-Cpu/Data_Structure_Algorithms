const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function calculator() {
    rl.question("Enter first number: ", (aInput) => {
        const a = parseFloat(aInput);
        
        rl.question("Enter second number: ", (bInput) => {
            const b = parseFloat(bInput);
            
            rl.question("Enter the operation (+, -, *, /, %): ", (op) => {
                let result;
                
                switch(op) {
                    case '+':
                        result = a + b;
                        console.log(`${a} + ${b} = ${result}`);
                        break;
                        
                    case '-':
                        result = a - b;
                        console.log(`${a} - ${b} = ${result}`);
                        break;
                        
                    case '*':
                        result = a * b;
                        console.log(`${a} * ${b} = ${result}`);
                        break;
                        
                    case '/':
                        if (b === 0) {
                            console.log("Error: Division by zero is not allowed!");
                        } else {
                            result = a / b;
                            console.log(`${a} / ${b} = ${result}`);
                        }
                        break;
                        
                    case '%':
                        if (b === 0) {
                            console.log("Error: Modulus by zero is not allowed!");
                        } else {
                            result = Math.floor(a) % Math.floor(b);
                            console.log(`${Math.floor(a)} % ${Math.floor(b)} = ${result}`);
                        }
                        break;
                        
                    default:
                        console.log("Invalid Input! Please use +, -, *, /, or %");
                }
                
                rl.close();
            });
        });
    });
}

calculator();