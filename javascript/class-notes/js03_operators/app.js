console.log('app js running');

/*
* 1. Write a JavaScript code to calculate multiplication and division of two numbers (input from user). : 5min

*/

// let num1 = +prompt('Enter first number');
// let num2 = +prompt('Enter second number');
// console.log(`${num1} x ${num2} is ${num1 * num2}, \n${num1} / ${num2} is ${num1 / num2}`);

/*
 * 2. area calculation: 7min
 * area of any triangle (given only sides) ---

 * area of rectangle (given only sides)
 * area of circle (given only radius)
 * perimeter of circle (given only radius)
 *
 * pi sayisi olarak :  Math.PI / 3.141592653589793
 */

// let side1 = +prompt('Enter first side');
// let side2 = +prompt('Enter second side');
// let side3 = +prompt('Enter third side');

// const perimeter = (side1 + side2 + side3) / 2;
// const area = Math.sqrt(
//   perimeter * ((perimeter - side1) * (perimeter - side2) * (perimeter - side3)),
// );

// console.log(`Area of triangle is ${area}, perimeter is ${perimeter}.`);
/*
* 3. temperature convertion : 8min
* celcius to fahrenheit
* fahrenheit to celcius

*/

// let cTemp = +prompt('Enter celcius temperature');
// const cToFahr = (cTemp * 9) / 5 + 32;
// console.log(`${cTemp}°C equals ${cToFahr.toFixed(2)}°F`);

// let fTemp = +prompt('Enter fahrenheit temperature');
// const fToCel = ((fTemp - 32) * 5) / 9;
// console.log(`${fTemp}°F equals  ${fToCel.toFixed(2)}°C`);

/*
 * 4. print today's date separately :8min
 * day of month is 11
 * month of year is 8
 * year is 2022
 */
// const today = new Date();
// console.log(today);

// console.log(today.getFullYear());
// // * use today (.) for needed functions

// console.log(`day of month is ${today.getDate()}`);
// console.log(`month of year is ${today.getMonth() + 1}`);
// console.log(`year is ${today.getFullYear()}`);

/*

* 5. check from three given numbers (non negative integers) that two or all of them have the same rightmost digit. : 10min

* 22 32 42 => true
* 15 24 45 => true
* 33 34 35 => false

*/

/*
stage is yours
There are at least 2 numbers having same first digit: true/false

*/

let p = +prompt('Enter first number');
let q = +prompt('Enter second number');
let r = +prompt('Enter third number');

const result = p % 10 === q % 10 || p % 10 === r % 10 || q % 10 === r % 10;

console.log(`There are at least 2 numbers having same first digit: ${result}`);
