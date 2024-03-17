'use strict';

/*
console.log(document.querySelector('.message').textContent); //As we have enclosed the document query in the console it will show the id called message with the text containing in it. 

document.querySelector('.message').textContent = '🎉 Correct Number!'; // Now we are canging the html part of the id called message. We have changed the html part to Correct Number! from Start guessing

console.log(document.querySelector('.message').textContent); // Now the correct number is shown as the result

document.querySelector('.number').textContent = 13; //This will change the html part of the id = number from ? to 13

document.querySelector('.score').textContent = 20; //This will change the id = score part to 20 from 0

//document.querySelector('guess').value = 23; //This is supposed to be 23 but not working right now in this version we need to find out an alternative
//console.log(document.querySelector('.guess').value); //This is supposed to show the rewritten thing

*/

//HANDLING CLICK

/*
const number = Math.random(); //This will always give an number between 0 t0 1 in decimal form.

console.log(number);

Math.trunc(Math.random()*20); //Here we will be abel to get number between 0 to 20 without decimal values

document.querySelector('.check').addEventListener('click',function(){
    const guess = Number(document.querySelector('.guess').value);
    console.log(guess,typeof guess);

    if(!guess)
    {
        document.querySelector('.message').textContent = '⛔ No number!'
    }

});
*/
 /*
i) we have selected the id = check part using queryselector
ii) then we have selected other method called addEventListener this method is used to pass the event to the selected part. so here we have used the click as the event.
iii) As an output we have the function, this function does not work as the script works it works when the event took place once the event took place then the function will be called and then the output from the function which is the value present in the guess id which will be displayed in the console part
*/

function num()
{
    const numb = Math.trunc(Math.random()*20);
    return numb;
}

let number = num();

let sco = 20;
let high = 0;

document.querySelector('.check').addEventListener('click',function(){
    const guess = Number(document.querySelector('.guess').value);

    if(!guess)
    {
        document.querySelector('.message').textContent = "⛔No number passed"
    }
    else if(guess !== number)
    {
        sco = sco-2;
        document.querySelector('.message').textContent = "Try again 🔁";
        if(guess < number)
        {
            document.querySelector(".message").textContent = "\nThe number is greater";
        }
        else
        {
            document.querySelector(".message").textContent = "\nThe number is smaller";
        }
    }
    else if(guess === number)
    {
        document.querySelector('.message').textContent = "Congratulations 🎉";
        document.querySelector('.score').textContent = sco;
        document.querySelector('body').style.backgroundColor = "green";
        document.querySelector('.number').style.width = '30rem';
        document.querySelector('.number').textContent = number;

        if(sco > high)
        {
            high = sco;
            document.querySelector('.highscore').textContent = high;
        }
        else
        {
            document.querySelector('.score').textContent = sco;
        }
    }
})

document.querySelector('.again').addEventListener('click',function(){
    document.querySelector('.guess').value = null;
    document.querySelector('.score').textContent = 20;
    sco = 20;
    number = num();
    document.querySelector('.message').textContent = "Start guessing...";
    document.querySelector('body').style.backgroundColor = "#222";
    document.querySelector('.number').style.width = '15rem';
    document.querySelector('.number').textContent = '?';

})