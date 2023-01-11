filterSelection("all") // Execute the function and show all columns
function filterSelection(c) {
    var x, i;
    x = document.getElementsByClassName("column");
    if (c == "all") c = "";
    // Add the "show" class (display:block) to the filtered elements, and remove the "show" class from the elements that are not selected
    for (i = 0; i < x.length; i++) {
        w3RemoveClass(x[i], "show");
        if (x[i].className.indexOf(c) > -1) w3AddClass(x[i], "show");
    }
}

// Show filtered elements
function w3AddClass(element, name) {
    var i, arr1, arr2;
    arr1 = element.className.split(" ");
    arr2 = name.split(" ");
    for (i = 0; i < arr2.length; i++) {
        if (arr1.indexOf(arr2[i]) == -1) {
            element.className += " " + arr2[i];
        }
    }
}

// Hide elements that are not selected
function w3RemoveClass(element, name) {
    var i, arr1, arr2;
    arr1 = element.className.split(" ");
    arr2 = name.split(" ");
    for (i = 0; i < arr2.length; i++) {
        while (arr1.indexOf(arr2[i]) > -1) {
            arr1.splice(arr1.indexOf(arr2[i]), 1);
        }
    }
    element.className = arr1.join(" ");
}

// Add active class to the current button (highlight it)
var btnContainer = document.getElementById("myBtnContainer");
var btns = btnContainer.getElementsByClassName("btn");
for (var i = 0; i < btns.length; i++) {
    btns[i].addEventListener("click", function () {
        var current = document.getElementsByClassName("active");
        current[0].className = current[0].className.replace(" active", "");
        this.className += " active";
    });
}

localStorage.setItem('fob', 'select');

$('#fob').on('change', function () {
    var val = $(this).val();
    localStorage.setItem('fob', val);
    $('select#type>option').each(function () {
        var filter = $(this).data();
        var elem = $(this);
        if ((filter.filter.food_or_beverage != val) && filter.filter.food_or_beverage != "") {
            elem.hide();
        } else if (filter.filter.food_or_beverage != "") {
            elem.show();
        } else {
            elem.show();
        }
    });
    $('li').each(function () {
        var item_filter = $(this).data();
        var item = $(this);
        if (item_filter.filter.food_or_beverage != val && val != "select") {
            item.hide();
        } else {
            item.show();
        }
    });
    $('#type').val("select");
    if (val == "select") {
        $('select#type>option').each(function () {
            $(this).show();
        });
        $('#type').val("select");
    }
});

$('#type').on('change', function () {
    var val = $(this).val();
    var storage = localStorage.getItem('fob');
    if (storage == "select") {
        $('li').each(function () {
            var item = $(this);
            item.show()
        });
    }
    if (storage == "food") {
        $('li').each(function () {
            var item = $(this);
            var data = item.data();
            if (data.filter.food_or_beverage == "food") {
                item.show();
            }
        });
    }
    if (storage == "beverage") {
        $('li').each(function () {
            var item = $(this);
            var data = item.data();
            if (data.filter.food_or_beverage == "beverage") {
                item.show();
            }
        });
    }

    $('li:visible').each(function () {
        console.log('val');
        var item_filter = $(this).data();
        var item = $(this);
        if (val == "fruit" && item_filter.filter.type != "fruit") {
            item.hide();
        }
        if (val == "vegetable" && item_filter.filter.type != "vegetable") {
            item.hide();
        }
        if (val == "juice" && item_filter.filter.type != "juice") {
            item.hide();
        }
        if (val == "nojuice" && item_filter.filter.type != "nojuice") {
            item.hide();
        }
    });
});





