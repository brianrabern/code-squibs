function mode(numbers) {
    let d = {}

    for (let i of numbers){
        d[i] = 0;
    }

     for (let i of numbers){
        d[i] +=1;
    }

    let mode = 0;

    for (let key in d){
        if (d[key] > mode){
            mode = key;
        }
    }
    return mode;

}



let arr1 = [];

for(let i=0;i<4;i++){
    arr1.push(i)
}
arr1



// let arr2 = [];

// for(const i=0;i<4;i++){
// arr2.push(i)
// }
// arr2

let range = [0,1,2,3,4,4,5,6,];
let arr3 = [];


for (const i in range){
    i
    arr3.push(i)

}

arr3
