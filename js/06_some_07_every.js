const arr = [1, 2, 3, 4, 5]
// 1. 
const result = arr.find(function (elem) {
  return elem % 2 ===0
})

// 2. 
const reuslt = arr.find((elem) => {
  return elem % 2 === 0
})

//3.
const result = arr.some((elem) => elem % 2 === 0 )

console.log(result)

// every
const newResult = arr.every((elem) => elem % 2 === 0)

console.log(newResult)