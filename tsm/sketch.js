

var cities = [];
totalCities = 5;
var order =[];

var totalPermutations;
var count =0;

var recordDistance;
var bestPath;

function setup() {
    createCanvas(800, 600);

    for (var i = 0; i < totalCities; i++){
        var v = createVector(random(width),random(height/2));
        cities[i] = v;
        order[i] = i;
    }
    var d = calcDist(cities,order);
    recordDistance = d;
    bestPath = order.slice();

    totalPermutations = factorial(totalCities);


}


function draw() {
    // frameRate(1);
    background(0);
    fill(255);
    for (var i = 0; i < cities.length; i++){
        ellipse(cities[i].x,cities[i].y,8,8);
    }


    // draw bestpath
    stroke(0, 255, 0);
    strokeWeight(3);
    noFill();
    beginShape();

    for (var i = 0; i < order.length; i++){
        var n = bestPath[i];
        vertex(cities[n].x,cities[n].y);
    }

    endShape();


    translate(10, (height/2)-5);
    stroke(255);
    strokeWeight(1);
    noFill();
    beginShape();

      for (var i = 0; i < order.length; i++){
          var n = order[i];
          vertex(cities[n].x,cities[n].y);
      }
      endShape();
    // var i = floor(random(cities.length));
    // var j = floor(random(cities.length));
    // swap(cities,i,j);

    var d = calcDist(cities,order);
    if (d < recordDistance){
        recordDistance = d;
        bestPath = order.slice();
        console.log(floor(recordDistance));
        }


    fill(255);
    text(s, 20, height-50);
    // fill(255);
    // var percent = 100 * (count / totalPermutations);
    // text(nf(percent, 0, 2) + "% completed", 0, height / 2);
    text('traveling sales person: shortest path', 0, 0);
    fill(255);
    textSize(32);
    fill(255);
    var s = '';
    for (var i=0; i < order.length; i++){
        s+=order[i];
    }
    nextOrder();

}

function swap(a,i,j){
    temp = a[i];
    a[i] = a[j];
    a[j] = temp;
}


function calcDist(points,order){
    var sum =0;
    for (var i = 0; i < (order.length-1); i++){
        var cityA = points[order[i]];
        var cityB = points[order[i+1]];
        var d = dist(cityA.x, cityA.y,cityB.x, cityB.y);
        sum+=d;
    }
    return sum;
}





// lexical order algorithm
function nextOrder(){

//step 1
var largestI = -1;
for (var i = 0; i<  order.length-1;i++){
    if (order[i] < order[i+1]){
        largestI = i;
    }
}
if (largestI == -1){
    noLoop();
    console.log('finsished');
}

 //step 2
 var largestJ = -1;
 for (var j=0; j < order.length;j++){
     if (order[largestI] < order[j]){
         largestJ = j;
     }
 }

 //step 3
 swap(order,largestI,largestJ);

 //step 4
 var endArray = order.splice(largestI+1);
 endArray.reverse();
order = order.concat(endArray);


}


function factorial(n) {
    if (n == 1) {
      return 1;
    } else {
      return n * factorial(n - 1);
    }
  }
