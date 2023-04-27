// demo 2
// JS event propagation

var tds = document.getElementsByTagName('td'); // list of all cell elements
var trs = document.getElementsByTagName('tr'); // list of all rows
var table = document.getElementsByTagName('table');//[0]; // why do we need 0 here?
// get Elements makes a list
// even though we only have 1 table, we have to specify first table from the list
console.log(table);

var clicky = function(e) {
  alert( this.innerHTML );
};

// adds event listener to table
table[0].addEventListener('click', clicky);  

// adds event listeners to all cells
for (var x=0; x < tds.length; x++) {
  tds[x].addEventListener('click', clicky);
}

// adds event listeners to all rows
for (x=0; x < trs.length; x++) { 
  trs[x].addEventListener('click', clicky);
}


// Q: When user clicks on a cell, in what order will the pop-ups appear?
// text in cell, html for row, html for whole table