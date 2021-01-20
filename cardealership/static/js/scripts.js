window.onload = function(){
    
    let selector = document.querySelector("#carmake");
    selector.addEventListener('change',function(){

        let carmake_id = selector.value;
        console.log(carmake_id)
        if(carmake_id == "no_carmake"){
            removeChilds(document.getElementById('carmodel'));
        }
        else{
            ajax_request(carmake_id);
        }
        
    });


function ajax_request(id){
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     console.log(this.responseText);
     res = JSON.parse(this.responseText)
     carmodels = res.carmodels;
     removeChilds(document.getElementById('carmodel'));
     for(const prop in carmodels){
        add_option(prop,carmodels[prop]);
     }
    }
  };
  xhttp.open("GET", `/ajax_handler/${id}`, true);
  xhttp.send();
}


function add_option(val,text){
    var sel = document.getElementById('carmodel');
    
// create new option element
var opt = document.createElement('option');

// create text node to add to option element (opt)
opt.appendChild( document.createTextNode(text) );

// set value property of opt
opt.value = val; 

// add opt to end of select box (sel)
sel.appendChild(opt); 
}

}

var removeChilds = function (node) {
    var last;
    while (last = node.lastChild) node.removeChild(last);
};

