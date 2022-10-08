/*
* 1. Write a JavaScript code to calculate multiplication and division of two numbers (input from user). : 5min

*/

/*
stage is yours




















*/

/*
 * 2. area calculation: 7min
 * area of any triangle (given only sides)
 * area of rectangle (given only sides)
 * area of circle (given only radius)
 * perimeter of circle (given only radius)
 * pi sayisi olarak :  Math.PI / 3.1415
 */

let side1 = +prompt('Enter first side');
let side2 = +prompt('Enter second side');
let side3 = +prompt('Enter third side');

const perimeter = (side1 + side2 + side3) / 2;
const area = Math.sqrt(
  perimeter * ((perimeter - side1) * (perimeter - side2) * (perimeter - side3)),
);

console.log(`Area of triangle is ${area}, perimeter is ${perimeter}.`);

/*
stage is yours



*/

/*
* 3. temperature convertion : 8min
* celcius to fahrenheit
* fahrenheit to celcius

*/

/*
stage is yours








*/

/*
 * 4. print today's date separately :8min
 * day of month is 11
 * month of year is 8
 * year is 2022
 */
const today = new Date();
console.log(today.getFullYear());
// * use today (.) for needed functions

/*
stage is yours





*/

/*

* 5. check from three given numbers (non negative integers) that two or all of them have the same rightmost digit. : 10min

* 22 32 42 => true
* 15 24 45 => true
* 33 34 35 => false

*/

/*
stage is yours


*/
