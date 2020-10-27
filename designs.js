
const colorPicker = document.body.querySelector('#colorPicker');
const pixelCanvas = document.body.querySelector('#pixelCanvas');
const sizePicker = document.body.querySelector('#sizePicker');

//add event listeners to the relevant DOM elements,
//giving access and catch user input for table size and cell backgroundColor
// When size is submitted by the user, call makeGrid()
sizePicker.addEventListener('submit', (e) => {
  makeGrid(e);
});
// Dynamically produce HTML code and update the page.
function makeGrid(e) {
  e.preventDefault();
  //reset pixelCanvas
  while (pixelCanvas.firstChild)
      pixelCanvas.removeChild(pixelCanvas.firstChild);
  //draw the table based on N and M size
  //JavaScript loops to dynamically create the html table (rows and cells) based on user input.
  for (let n=0; n<sizePicker.inputHeight.value; n++){
    //Rows are inserted to the table and return value is stored in row variable
    let tr = pixelCanvas.insertRow(n);
    for (let m=0; m<sizePicker.inputWidth.value; m++) {
      //Cells are interted to the row and return value is stored in cell variable
      let td = tr.insertCell(m);
      //Click event is raised when the user clicks on the table cell
      td.onclick = function() {
        //This cell is given the chosen backgroundColor when event is raised
        this.style.backgroundColor = colorPicker.value;
      };
    }
 }
}
