const numbers = [90, 80, 70, 100]

//총합

const sumNum = numbers.reduce(function (result, number) {return result + number}, 0)  //number빈 값이면 error가 나므로 0을 넣어준다.

console.log(sumNum)

const sumNum = numbers.reduce((result, number) => {
  return result + number
}, 0)

const avgNum = numbers.reduce((result, number) => result + number, 0) / numbers.length