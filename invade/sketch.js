let ship;
let bullets = [];
let propsA = [];

let t = [0,188,227];
let f = [255,255,0];
// let propsB = [];
// let propsC = [];
let allprops = [];


function setup() {
  createCanvas(600, 400);
  
  ship = new Ship();
  
  // bullet = new Bullet(width/2,height);
  for (var i = 0; i < 6; i++) {
    propsA[i] = new Prop(i * 100 + 40, 40, random([1, 2, 2, 2]));
  }

  // for (var i = 0; i < 6; i++) {
  //   propsB[i] = new Prop(i * 100 + 40, 80, random([1, 2, 2, 2]));
  // }

  // for (var i = 0; i < 6; i++) {
  //   propsC[i] = new Prop(i * 100 + 40, 120, random([1, 2, 2, 2]));
  // }

  // allprops = concat(propsA,propsB,propsC);

}

function draw() {
  background(0);
  ship.show();
  
   for (var i = 0; i < bullets.length; i++) {
    bullets[i].show();
    bullets[i].move();

      for (var j = 0; j < propsA.length; j++){
        if (bullets[i].hits(propsA[j])){
          
          // bullets[i].x = 5000; //need to remove these from the array
          // propsA[j].x = -5000; //need to remove these from the array
          // bullets[i].kill();
          propsA[j].explode();
          // bullets.splice(i,1);
          // console.log("hit");
        }

      }
   }

    for (var i = 0; i < propsA.length; i++) {
        propsA[i].show();
        if (propsA[i].todel){
          propsA.splice(i,1);
        }
      }

    // for (var i = bullets.length-1; i >= 0; i--) {
    //   if (bullets[i].getout){
    //     bullets.splice(i,1);
    //   }
    // }
    // console.log(propsA[0].tvalues)
    // console.log(propsA[1].tvalues)

  
 
  // for (var i = 0; i < propsB.length; i++) {
  //   propsB[i].show();
   
  // }
  // for (var i = 0; i < propsB.length; i++) {
  //   propsC[i].show();
  // }
  
 

}



function keyPressed() {
  if (key === ' '){
    let bullet = new Bullet(ship.x-5,height);
    bullets.push(bullet);
  }
  if (keyCode === RIGHT_ARROW) {
    ship.move(1);
  } else if (keyCode === LEFT_ARROW) {
    ship.move(-1);
  }
}


