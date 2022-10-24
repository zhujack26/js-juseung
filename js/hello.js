function add(num1, num2) {
    return num1 + num2
}

console.log(add(2, 7))


const sub = function (num1, num2) {
  return num1 - num2
}

console.log(sub(7,2)) 


// 원래 식
const greeting = function (name = 'juseung') {
  return `Hi ${name}`
}

// 1단계
const greeting = (name) => {
  return `Hi ${name}`
}

// 2단계(Airbnb에서 권장 x)
const greeting = name => {
  return `Hi ${name}`
}

// 3단계
const greeting = name => `Hi ${name}`


//1단계 
function (num) {return num **3}

//2단계
(num) => { return num **3 }

//3단계
((num)=> num **3)(2)
