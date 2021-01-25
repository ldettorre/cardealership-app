window.onload = function () {

    let selector = document.querySelector("#carmake");
    selector.addEventListener('change', function () {

        let carmakeName = selector.value;
        // The reason we are calling the add option function right after removing the child is because 
        // this stops the field from being totally empty after multiple revised selections.
        // The same has been done for the year field.
        removeChilds(document.getElementById('carmodel'));
        add_option("", "Any")

        // There is no conditional statement in this function because no matter what the carmake id changes to, we 
        // need it to reset the other fields./

        ajax_request(carmakeName);

    });


    function ajax_request(name) {
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                res = JSON.parse(this.responseText)
                carmodels = res.carmodels;
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






$(document).on('change', '#carmodel', function () {
    let selector = document.querySelector("#carmodel")
    carmodel = selector.value
    if (carmodel == "") {
        removeChilds(document.getElementById('caryear'));
        add_option("", "Any")
    }
    else {
        ajax_request2(carmodel);
    }
})


function ajax_request2(carmodel) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            res = JSON.parse(this.responseText)
            caryears = res.caryears;
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
    var opt = document.createElement('option');
    opt.appendChild(document.createTextNode(text));
    opt.value = val;
    sel.appendChild(opt);
}




var removeChilds = function (node) {
    var last;
    while (last = node.lastChild) node.removeChild(last);
};




function add_options(val, text, elementId) {
    var sel = document.getElementById(elementId);
    var opt = document.createElement('option');
    opt.appendChild(document.createTextNode(text));
    opt.value = val;
    sel.appendChild(opt);
}

let makeFieldId = document.querySelector("#carmake");
makeFieldId.addEventListener('change', function () {
    removeChilds(document.getElementById('carmodel'));
    add_options("", "Any", 'carmodel')
    removeChilds(document.getElementById('caryear'));
    add_options("", "Any", 'caryear')
})

let modelFieldId = document.querySelector("#carmodel");
modelFieldId.addEventListener('change', function () {
    removeChilds(document.getElementById('caryear'));
    add_options("", "Any", 'caryear')
})



