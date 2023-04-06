const shorterThan5 = function(strings) {
    const results = [];

    for (let s of strings){
        if (s.length <5){
            results.push(s)
        }
    }

    return results;
};


input = [
    "base",
    "basket",
    "foot",
    "hand",
    "racquet"
]

console.log(shorterThan5(input))


const shorterThan = function(strings,maxLength) {
    const results = [];

    for (let s of strings){
        if (s.length <maxLength){
            results.push(s)
        }
    }

    return results;
};


input1 = [
    "base",
    "basket",
    "foot",
    "hand",
    "racquet"
]

console.log(shorterThan(input1,5))


i = [
    "base",
    "basket",
    "foot",
    "hand",
    "racquet"
]



const shorterThanX = function(strings, maxLength) {
    return strings.filter(s => s.length < maxLength);
};





console.log(shorterThanX(i,10))
