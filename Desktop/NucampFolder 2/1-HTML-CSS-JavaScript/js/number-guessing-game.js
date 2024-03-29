function runGame() {
let guessString = '';
let guessNumber = 0;
let correct = false;  
let numTries = 0;  
// generate random number
const target = Math.floor(Math.random() * 100) + 1;
console.log(target);
//get guess from player
do {
    guessString = prompt('I am thinking of a number between 1 and 100.\n\n What is the number?')
    if (guessString === null) {
        return;
    }
    guessNumber = +guessString
    numTries += 1;
    correct = checkGuess(guessNumber, target)

} while (!correct)

alert('You got it!  The number was ' + target + '.\n\n It took you ' + numTries + ' tries.')

}

function checkGuess(guessNumber, target) {
    let correct = false;
    if (isNaN(guessNumber)) {
        alert('You have not entered a number.\n\n Please enter a number between 1 and 100.')
    }else if (guessNumber < 1 || guessNumber >100) {
        alert('Please enter an integer between 1 and 100.')
    }else if (guessNumber > target) {
        alert('Your number is too large!')
    }else if (guessNumber < target) {
        alert('Your number is too small!')
    }else {
        correct = true;
    }
    return correct
}

