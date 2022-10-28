//1.
 const colors = ['red', 'blue', 'green' ]

 const printClr = function (color) {
  console.log(color)
 }

 colors.forEach(printClr)

//2. 
colors.forEach(function (color) {
  console.log(color)
  })

//3. js가 사랑하는 구조
colors.forEach((color) => {
  console.log(color)
})

//4.한줄 (굳이 x)
colors.forEach((color) => console.log(color))