$(document).ready(function () {   // document селектор - ето вся страница целиком, ready метод (событие)

    var form = $('#csrf_form');
    var ref = $("#js_bay");
    console.log(form);

    form.on('click', function (event) {
        event.preventDefault(); //клик по ссылке не отправляет по новому урлу
         // наша ссылка где прописан data-new_car_id, и остальные
        var new_car_id = form.data("new_car_id"); // помещает в переменную результат
        var new_car_name = form.data("new_car_name");
        var new_car_price = form.data("new_car_price");
        var number = form.data("number");
        var session_key = form.data("session_key");
        var new_car_price_int = parseInt("new_car_price");
        var num = parseInt(6);


        // AJAX

        var data = {}; // data ето то что мы отправляем, название, цена
        var url = form.attr("action");  //form.attr("action"); - так можно считать url c атрибута формы если указать не путь
        // "/product/" + new_car_id + "/";
        var csrftoken = $("[name=csrfmiddlewaretoken]").val(); //вытянуть токен и использовать если нужно
        data["csrfmiddlewaretoken"] = csrftoken; //ложим его в наш словарь data

        data.product_id = new_car_id;  // добавил в словарь date  - new_car_id
        data.new_car_name = new_car_name;  // добавил в словарь date  - new_car_id
        data.new_car_price = new_car_price;  // добавил в словарь date  - new_car_id
        data.session_key = session_key;  // добавил в словарь date  - new_car_id
        data.number = number;  // добавил в словарь date  - new_car_id
        //data.products_total_num = products_total_num;

        console.log(data);


        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: false,
            success: function (data) {  // data - словарь который передаем во views.py jsonresponse в словаре

            if (data.products_total_num){
                $('#span').text("("+ data.products_total_num  +")");
            }
            //console.log(data);
            //css свойство укаали scrollTop() то всегда всерху где бы небыли на странице + 220


            var off = $('#offspring');

            console.log(off);

            function popup() {
                popup = $('.popup');
                popup.css({"top": $(window).scrollTop() + 220}).addClass('active');
                var bg_popup = $('.bg_popup');
                bg_popup.fadeIn();
                bg_popup.click(function () {   // удаляем при нажати на на люьом месте кроме окна котрое появилось
                    $('.popup').removeClass('active');
                    bg_popup.fadeOut();
                });
            }

            popup();


            $(".basket-item ul").append('<li>' + new_car_name + '$' + new_car_price + ' <a class="delete" href="#">' +
                'Delete' + '</a>' + '</li>' + '</br>' ); //по клику добавляем елемент, с перемен. + конкатен

                console.log('OK - add - ajax');
            },
            error: function () {
                console.log('error');
            }
        });

        form.off()
    });



 //  -------------- hover ------------------

    var basket_container = $(".basket-container");
    var basket_item = $(".basket-item");


    basket_container.mouseover(function () { // или клие или наведение
        basket_item.toggleClass("d-none"); //при наведении удаляется временно класс если он есть
    });

    basket_container.mouseout(function () { // или клие или наведение
        basket_item.toggleClass("d-none"); //при наведении удаляется временно класс
    });

});



//-------------------------------------------------- del -----------------------
//var new_car_id = ref.data("new_car_id"); // помещает в переменную результат
    data = {}; // data ето то что мы отправляем, название, цена
    var url = "/product/" + "85" + "/";  //form.attr("action") - так можно считать url c атрибута формы если указать не путь


$(document).on('click', ".delete",function () {

    $.ajax({
        url: url,
        type: 'get',
        data: data,
        cache: false,
        success: function () {
            $(".delete").closest('li').remove();
            console.log('OK - del - ajax');

        },
        error: function () {
            console.log('error');
        }
     });
});

//--------------------------------------------------        ------------------------



// $(document).ready(function () {   // document селектор - ето вся страница целиком, ready метод (событие)
//
//     var registrations = $('#registrations');
//
//     data = {}; // data ето то что мы отправляем, название, цена
//     var url = "/accounts/login/";
//
//     registrations.on('click', function () {
//
//      console.log("hi");
//
//         $.ajax({
//         url: url,
//         type: 'get',
//         data: data,
//         cache: false,
//         success: function () {
//
//             function popup() {
//                 popup = $('.popup');
//                 popup.css({"top": $(window).scrollTop() + 220}).addClass('active');
//                 var bg_popup = $('.bg_popup');
//                 bg_popup.fadeIn();
//                 bg_popup.click(function () {   // удаляем при нажати на на люьом месте кроме окна котрое появилось
//                     $('.popup').removeClass('active');
//                     bg_popup.fadeOut();
//                 });
//             }
//
//             popup();
//
//             console.log('OK - del - ajax');
//
//         },
//             error: function () {
//                 console.log('error');
//             }
//         });
//     });
// });


//---------------------------------------------


// // function show() {
// //     $(document).ready(function () {
// //         var tag = $('#testajx');
// //         var datenew = tag.data("datatime");
// //
// //         $.ajax({
// //             url: "test.html",
// //             cache: false,
// //             datenew: datenew,
// //             tag: tag,
// //             success: function (datenew) {
// //             console.log('OK');
// //             tag.html(datenew);
//
// //
// //     }
// // });
// //
// //
// //
// //
// //     });
// // }
// //setInterval('show()', 1000);
//
//
// //var number = 50; // переменная число
// //var bool = true; // bool переменная
// //var string = "hello zohan"; // переменная строка
//
// //var zohan;
// //zohan = 20;
//
//
//
// //document.write("Hello" + " world " + (number*zohan)); // вывод на экран
// //document.write(bool); // вывод на экран переменной
//
// //alert("Сайт в разработке")
//
//
// // $('document').ready(function () {   // document селектор - ето вся страница целиком, ready метод (событие)
// //     $("p").append('<a href="https://translate.google.cn/m/translate?hl=ru">Google</a>'); // в body подключили тег а (добавили елемент)
// //
// // });
//
//
// // функция выводит значение на новой странице которое вбиваем в форму
// // можно в теге передать id и по нему присваивать определенному тегу действия jquery
// //$('document').ready(function () {
//     //$("button").on('click', function () {  // по клику на  выполняется действие (событие)
//         //s = $("input").val(); // берется значение из input или еще какогото елемента
//         //s = parseInt(s); // переконвертирует с int
//         //d = parseInt(10);
//         //var c = s + d;
//             //document.write(c);
//     //});
//  //});
//
// //изменить значение в div допустим после нажания ввода в поле input
//
// //$("document").ready(function () {
//     //$("input").keyup(function () {  // используется событие keyup для кнопки
//         //var val1 = 10;
//         //$("div").html(val1)
//     //})
// //});
//
//
// //окно с вопросом, отображение в div
// $(document).ready(function () {
//     test1 = prompt("Как ваше имя ?", ""); // событие prompt (появится окно с первым аргументом,
//                                            // то что введем выведется во всех div, можем только одному div, илии еще какому тегу)
//     $("div").html(test1);
// });


// $("document").ready(function () {
//     $.ajax({
//         url: "/date/",
//         cache: false,
//         success: function (p) {
//             $('#testajx').html(p);
//             concole.log("ok");
//         }
//     });
//});

//    -----------------   откат ---------------------
//  $("#js_bay").on('click', function (event) {
//         event.preventDefault(); //клик по ссылке не отправляет по новому урлу
//         var form = $('#csrf');
//         var ref = $("#js_bay"); // наша ссылка где прописан data-new_car_id, и остальные
//         var new_car_id = ref.data("new_car_id"); // помещает в переменную результат
//         var new_car_name = ref.data("new_car_name");
//         var new_car_price = ref.data("new_car_price");
//         var session_key = ref.data("session_key");
//         var new_car_price_int = parseInt(new_car_price);
//         var num = parseInt(6);
//         var total = new_car_price_int * num;

    // ------------------------------


//     //функция
//     // function test(a, b) {
//     //     var too = 2;
//     //     var res = a + b;
//     //     document.write(res)
//     // }
//     //
//     // test(5, 5);



//popup
$(document).ready(function () {   // document селектор - ето вся страница целиком, ready метод (событие)

    var registrations = $('.registrations');

    data = {}; // data ето то что мы отправляем, название, цена
    var url = "/accounts/login/";

    registrations.on('click', function (event) {
        event.preventDefault();

        $.ajax({
            url: url,
            type: 'get',
            data: data,
            cache: false,
            success: function () {

                function popup() {
                    popup = $('.popup');
                    popup.css({"top": $(window).scrollTop() + 220}).addClass('active');
                    var bg_popup = $('.bg_popup');
                    bg_popup.fadeIn();
                    bg_popup.click(function () {   // удаляем при нажати на на люьом месте кроме окна котрое появилось
                        $('.popup').removeClass('active');
                        bg_popup.fadeOut();
                    });
                }

                popup();

                console.log('OK - del - ajax');

            },
            error: function () {
                console.log('error');
            }
        });
    });
});