function setup() {
  var myCanvas = createCanvas(400, 400, WEBGL);
  myCanvas.parent("#logo");
}

function draw() {
  background(7,7,7);
  var rx = 70;
  var ry = 77.4;
  rotateX(rx * 0.01);
  rotateY(ry * 0.01);
  stroke(255,255,255);
  fill(0,255,205,100);
  box(250);
}