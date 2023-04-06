function Bullet(x, y) {
  this.x = x;
  this.y = y;
  this.r = 30;
  // this.getout = false;

  // let t = [0,188,227];
  // let f = [255,255,0];

  let wedge = '\u2227';
  let vee = '\u2228';
  let top = '\u22A4';
  let arrow = '\u2B62';
  let neg = '\u00AC';
  let dneg = '\u00AC\n\u00AC';
  let darrow = '\u2194'
  
  this.inHole;
  this.onDeck;
  this.connective =random([wedge,vee,neg,arrow,darrow,dneg,top]);

  this.show = function(){
   
    textSize(20);
    fill(255);
    textLeading(7);
    // triangle(this.x, this.y, this.x+10, this.y+30, this.x+10, this.y+10);
    text(this.connective, this.x, this.y);
  
  }
  
  this.move = function(){
    this.y = this.y-3;
  
  }
  
 

  this.hits = function(prop){
    
  let d = dist(this.x,this.y, prop.x,prop.y);

  if (d < this.r){

    //top
    if ((this.connective == top)){
    return true;
    }
    //neg
    if ((prop.arity == 1) && (this.connective == neg) && (prop.tvalues[0] == f)){
        return true;
    }
    //dneg
    if ((prop.arity == 1) && (this.connective == dneg) && (prop.tvalues[0] == t)){
      return true;
    }
    //wedge
    if ((prop.arity == 2) && (this.connective == wedge) && (prop.tvalues[0] == t) && (prop.tvalues[1] == t)){
    return true;
    } 
      //vee
    if ((prop.arity == 2) && (this.connective == vee) && ((prop.tvalues[0] == t) || (prop.tvalues[1] == t))){
    return true;
    } 
    //arrow
    if ((prop.arity == 2) && (this.connective == arrow) && ((prop.tvalues[0] == f) || (prop.tvalues[1] == t))){
    return true;
    } 
    //darrow
    if ((prop.arity == 2) && (this.connective == darrow) && (prop.tvalues[0] == prop.tvalues[1])){
    return true;
    }
    else if (prop.arity > 0) {
      prop.wrong();

    }

  } else {return false;}

}

}

  // this.out = function(){
  //   this.getout = true;
  // }
