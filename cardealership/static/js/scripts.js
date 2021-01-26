// Notes
// The terms 'reset/resetting' used in comments refers to combined use of the removeChilds() and add_option() function. Together, these effectively remove the options from a field and then
// create a single default option with a value of "" and text "Any".

window.onload = function () {
    let selector = document.querySelector("#carmake");
    selector.addEventListener('change', function () {
        let carmakeName = selector.value;
        ajax_request_carmake(carmakeName);

    });


    // This function triggers the ajax_handler view in home/views.py
    // The response text is a dict with the key/value pairs being set to the carmodel value within the db.
    // Those values are then added to the carmodel field.
    function ajax_request_carmake(name) {
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


    // Used in a loop within the ajax request above. 
    // This grabs the carmodel id, creates a new option element, creates a text node and sets the value of the newly created option.
    function add_option(val, text) {
        var sel = document.getElementById('carmodel');
        var opt = document.createElement('option');
        opt.appendChild(document.createTextNode(text));
        opt.value = val;
        sel.appendChild(opt);
    }
}


// Changing the carmodel field triggers the ajax request returning car years..
// The ajax request is then called to render years available to that carmodel option.
$(document).on('change', '#carmodel', function () {
    let selector = document.querySelector("#carmodel")
    carmodel = selector.value
    ajax_request_carmodel(carmodel);
})


function ajax_request_carmodel(carmodel) {
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


// Removes the options or 'children' of the targeted field.
var removeChilds = function (node) {
    var last;
    while (last = node.lastChild) node.removeChild(last);
};


// This altered version of the add_option function is used for resetting fields one after another.
function dynamic_add_option(val, text, elementId) {
    var sel = document.getElementById(elementId);
    var opt = document.createElement('option');
    opt.appendChild(document.createTextNode(text));
    opt.value = val;
    sel.appendChild(opt);
}


// Ideally I wanted to have one chain link of eventListeners that would 'reset' all the fields that followed the trigger event.
// But I couldn't seem to get it working as desired. Instead, I settled on creating a 'reset' event chain per field.


// Changing carmake results in all following fields to be reset.
let makeFieldId = document.querySelector("#carmake");
makeFieldId.addEventListener('change', function () {
    removeChilds(document.getElementById('carmodel'));
    dynamic_add_option("", "Any", 'carmodel')
    removeChilds(document.getElementById('caryear'));
    dynamic_add_option("", "Any", 'caryear')
})


// Changing carmodel results in all its following fields to be reset.
let modelFieldId = document.querySelector("#carmodel");
modelFieldId.addEventListener('change', function () {
    removeChilds(document.getElementById('caryear'));
    dynamic_add_option("", "Any", 'caryear')
})



// Min Price number generator
// let minPriceField = document.querySelector("#pricemin");
// minPriceField.addEventListener('change', function () {