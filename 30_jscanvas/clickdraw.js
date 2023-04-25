// Elmo :: Ryan Lee, Emily Ortiz
// SoftDev pd8
// K30 -- JS Paint
// 2023-04-24m

//retrieve node in DOM via ID
var c = document.getElementById("slate");

//instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

//init globar state var
var mode = "rect";

//var toggleMode = function(e){
var toggleMode = (e) => {
    console.log("toggling...");
    if (mode === "rect") {
        mode = "circ";
        bToggler.innerHTML = "circ";
    }
    else {
        mode = "rect";
        bToggler.innerHTML = "rect";
    }
}

//var drawCircle = function(e) {
var drawCircle = (e) => {
    var mouseX = e.offsetX; //gets X-coor of mouse when event is fired
    var mouseY = e.offsetY;//gets Y-coor of mouse when event is fired
    console.log("mouseclicked registered at ", mouseX, mouseY);
    ctx.fillStyle = "red";
    ctx.strokeStyle = "black";
    ctx.beginPath();
    ctx.arc(mouseX, mouseY, 40, 0, Math.PI * 2);
    ctx.fill();
    ctx.stroke();
}

var drawRect = function(e) {
    var mouseX = e.offsetX //gets X-coor of mouse when event is fired
    var mouseY = e.offsetY//gets Y-coor of mouse when event is fired
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.fillStyle = "red";
    ctx.fillRect(mouseX, mouseY, 75, 125);
}

var draw = (e) => {
    if (mode === "rect") {
        drawRect(e);
    }
    else {
        drawCircle(e);
    }
}

//var wipeCanvas = function() {
var wipeCanvas = () => {
    ctx.clearRect(0,0,600,600);
}

c.addEventListener("click", draw) //passes the mouse event as parameter for the function
var bToggler = document.getElementById("buttonToggle");
bToggler.addEventListener("click", toggleMode)
var clearB = document.getElementById("buttonClear");
clearB.addEventListener("click",  wipeCanvas);