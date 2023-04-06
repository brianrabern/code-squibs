// const uppercaseAll = function (strings) {
//     const result = [];

//     for (let s of strings){
//         result.push(s.toUpperCase())

//     }

//     return result;
// }


// const uppercaseAll2 = function (strings) {

//     return strings.map(s => s.toUpperCase())

// }

const uppercaseAll2 = function (strings) {
    const result = strings.map(function(string) {
        return string.toUpperCase();
    });
    return result
}

let input = [
    "arrays in JavaScript, lists in Python",
    "objects in JavaScript, dictionaries in Python"
]

console.log(uppercaseAll2(input))
