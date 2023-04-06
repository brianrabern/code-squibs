
function uppercaseArray(values){
    let result = []

    for (x of values){
        result.push(x.toUpperCase())
    }

}



["a", "d", "z"]


// function simpleSearch(values, searchTerm) {
//     if (values.includes(searchTerm)){
//         return true
//     }
//     return false
// }

// function propertyInObject(values, propertyName) {
//     let result = []

//     for (let d of values){
//         if (propertyName in d){
//             result.push(true)
//         }
//         else{
//             result.push(false)
//         }
//     }
//     return result
// }


// console.log(propertyInObject([{"age": 10}, {"remote": false}],"age"))

// def key_in_dict(list_of_dicts, key):

//     result = []

//     for d in list_of_dicts:
//         if key in d:
//             result.append(True)
//         else:
//             result.append(False)
//     return result


// function uppercaseArray(values){
//     let result = [];
//     for (let x in values){
//         if (typeof x === 'number'){
//             result.push(x)
//         }
//         else {
//             result.push(x.toUpper())
//         }

//     }
//     return result;
// }


// function filterBetween(values, lower, upper) {
//     let filt = values.filter((x) => x >= lower && x <= upper);
//     return filt;
// }




// function filter_less_than_or_equal_to(values, threshold) {
//     let filt = values.filter((x) => x <= threshold);
//     return filt;

// }







// function keyForValue(jsonString, propertyValue) {
//     let d = JSON.parse(jsonString)

//     for (let key in d){
//         if (d[key]===propertyValue){
//             return key
//         }
//     }
//     return null

// }

// console.log(keyForValue('{"age": 32, "name": "Evander"}', "j"))

// '{"age": 23}'
// '{"name": "Noor"}'

// d = json.loads(json_string)

// for key in d:
//     if d[key] == property_value:
//         return key

// return None


// function hasProperty(jsonString, propertyName) {
//     let d = JSON.parse(jsonString);

//     if (propertyName in d){
//         return true;
//     }else {
//         return false;
//     }
// }
