window.onload = function () {

    let selector = document.querySelector("#carmake");
    selector.addEventListener('change', function () {

        let carmakeName = selector.value;
        console.log(carmakeName)
        if (carmakeName == "no_carmake") {
            removeChilds(document.getElementById('carmodel'));
        }
        else {
            ajax_request(carmakeName);
        }
    });


    function ajax_request(name) {
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                // console.log(this.responseText);
                res = JSON.parse(this.responseText)
                carmodels = res.carmodels;
                removeChilds(document.getElementById('carmodel'));
                for (const prop in carmodels) {
                    add_option(prop, carmodels[prop]);
                }
            }
        };
        xhttp.open("GET", `/ajax_handler/${name}`, true);
        xhttp.send();
    }


    function add_option(val, text) {
        var sel = document.getElementById('carmodel');

        // create new option element
        var opt = document.createElement('option');

        // create text node to add to option element (opt)
        opt.appendChild(document.createTextNode(text));

        // set value property of opt
        opt.value = val;

        // add opt to end of select box (sel)
        sel.appendChild(opt);
    }
}






$(document).on('change', '#carmodel', function(){
    let selector = document.querySelector("#carmodel")
    carmodel = selector.value
    if (carmodel == "no_carmodel") {
        removeChilds(document.getElementById('caryear'));
    }
    else {
        ajax_request2(carmodel);
    }


    function ajax_request2(carmodel) {
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                // console.log(this.responseText);
                res = JSON.parse(this.responseText)
                caryears = res.caryears;
                removeChilds(document.getElementById('caryear'));
                for (const prop in caryears) {
                    add_option(prop, caryears[prop]);
                }
            }
        };
        xhttp.open("GET", `/ajax_handler2/${carmodel}`, true);
        xhttp.send();
    }
    
    function add_option(val, text) {
        var sel = document.getElementById('caryear');

        // create new option element
        var opt = document.createElement('option');

        // create text node to add to option element (opt)
        opt.appendChild(document.createTextNode(text));

        // set value property of opt
        opt.value = val;

        // add opt to end of select box (sel)
        sel.appendChild(opt);
    }

})


var removeChilds = function (node) {
    var last;
    while (last = node.lastChild) node.removeChild(last);
};


