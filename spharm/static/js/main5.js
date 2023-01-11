jQuery(document).ready(function ($) {
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
        if (storage == "city1") {
            $('li').each(function () {
                var item = $(this);
                var data = item.data();
                if (data.filter.food_or_beverage == "city1") {
                    item.show();
                }
            });
        }
        if (storage == "city2") {
            $('li').each(function () {
                var item = $(this);
                var data = item.data();
                if (data.filter.food_or_beverage == "city2") {
                    item.show();
                }
            });
        }
        if (storage == "city3") {
            $('li').each(function () {
                var item = $(this);
                var data = item.data();
                if (data.filter.food_or_beverage == "city3") {
                    item.show();
                }
            });
        }
        if (storage == "city4") {
            $('li').each(function () {
                var item = $(this);
                var data = item.data();
                if (data.filter.food_or_beverage == "city4") {
                    item.show();
                }
            });
        }

        $('li:visible').each(function () {
            console.log('val');
            var item_filter = $(this).data();
            var item = $(this);
            if (val == "pharmacy1" && item_filter.filter.type != "pharmacy1") {
                item.hide();
            }
            if (val == "pharmacy2" && item_filter.filter.type != "pharmacy2") {
                item.hide();
            }
            if (val == "pharmacy3" && item_filter.filter.type != "pharmacy3") {
                item.hide();
            }
            if (val == "pharmacy4" && item_filter.filter.type != "pharmacy4") {
                item.hide();
            }
        });
    });
});