function Prop(x, y, a) {
  this.x = x;
  this.y = y;
  this.todel =false;
  this.arity = a;

  // let t = [0,188,227];
  // let f = [255,255,0];
  this.tvalues = [random([t,f]),random([t,f])];

  this.explode = function() {
    fill(0,188,227);
    circle(this.x, this.y, 25);
    this.todel  = true;
  }

  this.wrong = function() {
    fill(255,0,0);
    circle(this.x, this.y, 25);
  }
 

  this.show = function () {
    if (this.arity == 1) {
      push();
      fill(this.tvalues[0]);
      rect(this.x, this.y, 60, 25);
      pop();
    } else if (this.arity == 2) {
      push();
      noStroke();
      fill(this.tvalues[0]);
      rect(this.x - 18, this.y, 27, 25);
      push();
      noStroke();
      fill(this.tvalues[1]);
      rect(this.x + 18, this.y, 27, 25);

      push();
      stroke(255);
      strokeWeight(3);

      line(this.x - 4, this.y, this.x + 4, this.y);
      pop();
    }
  }
  
}
