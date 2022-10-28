const myInfo = {
  name : 'jack',
  phoneNumber : '123456',
  'samsung product' : {
    buds : 'Buds pro',
    galaxy : 'S99',
  },
}

console.log(myInfo.name)
console.log(myInfo['name'])
console.log(myInfo['samsung product'].galaxy)

//3. 계산된 속성

const key = 'ssafy'
const value = ['한국', '미국', '일본', '중국']
const my0bj = {
  [key]: value,
}
console.log(my0bj)
console.log(my0bj.ssafy)


const jsonData = {
  coffee : 'Americano'
  iceCream : 'Mint Choco'
}
// Onject -> json
const objToJson = JSON.stringify(jsonData)
console.log(typeof onjToJson) //string

// json -> Object api는 json을 주니 이 부분이 더 중요하다
const jsonToonj = JSON.parse(objToJson)
// 파이썬에서는 response.json()