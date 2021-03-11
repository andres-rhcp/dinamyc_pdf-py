// JS code for dinamyc operations in quotes

var qty;
var x;
var y;

var dx;
var dy;

function init() {
  // so head it off here.
  if (global.initialized) return;
  global.initialized = true;

  score = 0;
  lives = 3;

  x = CANVAS_WIDTH/2;
  y = 430;

  dx = 2;
  dy = 2;

  qty = 0;
  bands = [];
  bricks = [];
  
  global.count = 3;

  global.mouseX = CANVAS_WIDTH/2;
  global.paused = false;
  
  cont = false;
  start();
}
//init table headers
var productNameHeader = this.getField('productNameHeader');
var dimensionsHeader = this.getField('dimensionsHeader');
var materialHeader = this.getField('materialHeader');
var parttolHeader = this.getField('parttolHeader');
var holetolHeader = this.getField('holetolHeader');
var finishHeader = this.getField('finishHeader');
var coatingHeader = this.getField('coatingHeader');
var unitPriceHeader = this.getField('unitPriceHeader');
var qtyHeader = this.getField('qtyHeader');
var totalPriceHeader = this.getField('totalPriceHeader');
var leadTimeHeader = this.getField('leadTimeHeader');
subtotal = this.getField('subtotal');
grandTotal = this.getField('grandTotal');
subtotalRes = this.getField('subtotalRes');
grandTotalRes = this.getField('grandTotalRes');

function drawQty(){
  // //Drawing table headers
  productNameHeader.value = '    Product Name     ';
  dimensionsHeader.value =  ' Aprox. Dimensions ';
  materialHeader.value =    '  Material  ';
  parttolHeader.value =     '  Part Tol  ';
  holetolHeader.value =     ' Hole Tol ';
  finishHeader.value =      '   Finish   ';
  coatingHeader.value =     ' Coaating ';
  unitPriceHeader.value =   ' Unit Price';
  qtyHeader.value =         '     Qty     ';
  totalPriceHeader.value =  'Total Price';
  leadTimeHeader.value =    ' Lead Time';
  subtotal.value = 'Subtotal:';
  grandTotal.value = "Grand Total:";
  var newJson = JSON.parse(JSON.stringify(quotesJson))
  newJson = JSON.parse(newJson.replace(/'/g, "\""));
  var st = 0
  for (var i=0; i< newJson['quotes'].length; i++)
  {
    id = newJson['quotes'][i].id;
   
    if(!cont)
    { 
      var temp = 'productName-'+id;
      tempField=this.getField(temp);
      tempField.value=newJson['quotes'][i].productName;
      temp = 'dimensions-' + id;
      tempField=this.getField(temp);
      tempField.value=newJson['quotes'][i].dimensions;
      temp = 'material-'+id;
      tempField=this.getField(temp);
      tempField.value=newJson['quotes'][i].material;
      temp = 'parttol-'+ id;
      tempField=this.getField(temp);
      tempField.value=newJson['quotes'][i].parttol;
      temp = 'holetol-'+ id;
      tempField=this.getField(temp);
      tempField.value=newJson['quotes'][i].holetol;
      temp = 'finish-'+ id;
      tempField=this.getField(temp);
      tempField.value=newJson['quotes'][i].finish;
      temp = 'coating-'+ id;
      tempField=this.getField(temp);
      tempField.value=newJson['quotes'][i].coating;
      temp = 'unitPrice-'+ id;
      tempField=this.getField(temp);
      tempField.value=newJson['quotes'][i].unitPrice;
      temp = 'qty-'+ id;
      tempField=this.getField(temp);
      tempField.value=newJson['quotes'][i].qty;
      temp = 'totalPrice-'+ id;
      tempField=this.getField(temp);
      tempField.value=newJson['quotes'][i].totalPrice;
      temp = 'leadTime-'+ id;
      tempField=this.getField(temp);
      tempField.value=newJson['quotes'][i].leadTime;

      this.getField('totalPrice-'+ id).value = parseFloat((parseFloat(('unitPrice-'+id).value).toFixed(2) * Number(newJson['quotes'][i].qty)).toFixed(2)).toFixed(2);
      subtotalRes.value = parseFloat(Number(('totalPrice-'+id).value)+ Number(('totalPrice-'+id).value)).toFixed(2);
      grandTotalRes.value = parseFloat(Number(('totalPrice-'+id).value)+ Number(('totalPrice-'+id).value)).toFixed(2);
    }
    maxqty = ((Number(newJson['quotes'][i].qty))*2) + ((newJson['quotes'][i].qty.toString().length)*10);
    // app.alert(maxqty)
    if(Number(this.getField('qty-'+id).value)>Number(maxqty))
    {
      app.alert('Max quanity should be < '+maxqty);
      this.getField('qty-'+id).value = newJson['quotes'][i].qty;
    }
    if(Number(this.getField('qty-'+id).value)<Number(newJson['quotes'][i].qty))
    {
      app.alert('Min quanity should be > '+newJson['quotes'][i].qty);
      this.getField('qty-'+id).value = newJson['quotes'][i].qty
    }
    // app.alert(this.getField('totalPrice-'+ id).value);
    this.getField('totalPrice-'+ id).value = parseFloat((parseFloat(this.getField('unitPrice-'+id).value).toFixed(2) * Number(this.getField('qty-'+id).value)).toFixed(2)).toFixed(2);
    st = st + parseFloat(Number(this.getField('totalPrice-'+id).value));

  }
  subtotalRes.value = st.toFixed(2);
  grandTotalRes.value = st.toFixed(2);
  cont = true;
}

var countdownField = this.getField('countdown');
function draw() {
  drawQty();
  x += dx;
  y += dy;
}

var whole = this.getField('whole');
function wrappedDraw() {
  try {
    whole.display = display.visible;
    draw();
    whole.display = display.hidden;

  } catch (e) {
    app.alert(e.toString())
  }
}

function start() {
  app.setInterval('wrappedDraw()', 15);
}

init();
