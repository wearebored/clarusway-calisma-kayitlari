// ? ===================================================
// ?                FONKSİYONLAR-SCOPE
// ? ====================================================
console.log("******* 3 - SCOPE ********");

let sayi1 = 5; //! Global Scope
console.log(sayi1); //! 5

const fonks1 = function () {
  sayi1 = 22;
  console.log(sayi1); //! 22
};
fonks1();

console.log(++sayi1); //! 23
console.log(sayi1); //!23

//? --------------------------------------
const sayi2 = 7; //! Global scope
console.log(sayi2); //! 7

const fonks2 = () => {
  const sayi2 = 11; //! Function-scope
  console.log(sayi2); //! 11
};

fonks2();
console.log(sayi2); //!7

if (sayi2 === 8) {
  let sonuc = "Merhaba";
} else {
  sonuc = "Nasilsin"; //! Hoisting oluyor, yani degisken global hale geliyor.
  // console.log(sonuc);
}

console.log(sonuc);
