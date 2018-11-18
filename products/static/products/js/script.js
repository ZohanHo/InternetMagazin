$(document).ready(function () {   // document селектор - ето вся страница целиком, ready метод (событие)

    $("#js_bay").on('click', function (event) {
        event.preventDefault(); //клик по ссылке не отправляет по новому урлу
        var ref = $("#js_bay"); // наша ссылка где прописан data-new_car_id, и остальные
        var new_car_id = ref.data("new_car_id"); // помещает в переменную результат
        var new_car_name = ref.data("new_car_name");
        var new_car_price = ref.data("new_car_price");
        var session_key = ref.data("session_key");
        var new_car_price_int = parseInt(new_car_price);
        var num = parseInt(6);
        var total = new_car_price_int * num;



        // AJAX
        var data = {}; // data ето то что мы отправляем, название, цена
        var url = "/product/" + new_car_id + "/";  //form.attr("action") - так можно считать url c атрибута формы если указать не путь

        data.product_id = new_car_id;  // добавил в словарь date  - new_car_id
        data.new_car_name = new_car_name;  // добавил в словарь date  - new_car_id
        data.new_car_price = new_car_price;  // добавил в словарь date  - new_car_id
        data.session_key = session_key;  // добавил в словарь date  - new_car_id

        //var csrf_token = $('#csrf_getting_form[name="csrfmiddlewaretoken"]').val();  //вытянуть токен и использовать если нужно
        //data["csrfmiddlewaretoken"] = csrf_token; //ложим его в наш словарь data


        $.ajax({
            url: url,
            type: 'GET',
            data: data,
            cache: true,
            success: function () {
            $(".basket-item ul").append(new_car_name+ '<br>' + '$' + new_car_price + ' <a class="delete" href="">' +
                                                'Delete</a>' + '</li>'); //по клику добавляем елемент, с перемен. + конкатен
            console.log('OK');
            console.log(data);
            },
            error: function () {
                console.log('error');
            }
        });
    });


    //функция
    // function test(a, b) {
    //     var too = 2;
    //     var res = a + b;
    //     document.write(res)
    // }
    //
    // test(5, 5);


    var basket_container = $(".basket-container");
    var basket_item = $(".basket-item");

    // basket_container.on('click', function (e) {
    //     e.preventDefault();  // отменяет событие
    //     basket_item.toggleClass("d-none");
    // });

    basket_container.mouseover(function () { // или клие или наведение
        basket_item.toggleClass("d-none"); //при наведении удаляется временно класс если он есть
    });

    basket_container.mouseout(function () { // или клие или наведение
        basket_item.toggleClass("d-none"); //при наведении удаляется временно класс
    });
});

$(document).on('click','.delete',function () {
    $(this).closest('li').remove(); // closest ето ближайший к нему елемент и указуем что нам нужен li, удаляем,
});






// function show() {
//     $(document).ready(function () {
//         var tag = $('#testajx');
//         var datenew = tag.data("datatime");
//
//         $.ajax({
//             url: "test.html",
//             cache: false,
//             datenew: datenew,
//             tag: tag,
//             success: function (datenew) {
//             console.log('OK');
//             tag.html(datenew);

//
//     }
// });
//
//
//
//
//     });
// }
//setInterval('show()', 1000);


//var number = 50; // переменная число
//var bool = true; // bool переменная
//var string = "hello zohan"; // переменная строка

//var zohan;
//zohan = 20;



//document.write("Hello" + " world " + (number*zohan)); // вывод на экран
//document.write(bool); // вывод на экран переменной

//alert("Сайт в разработке")


// $('document').ready(function () {   // document селектор - ето вся страница целиком, ready метод (событие)
//     $("p").append('<a href="https://translate.google.cn/m/translate?hl=ru">Google</a>'); // в body подключили тег а (добавили елемент)
//
// });


// функция выводит значение на новой странице которое вбиваем в форму
// можно в теге передать id и по нему присваивать определенному тегу действия jquery
//$('document').ready(function () {
    //$("button").on('click', function () {  // по клику на  выполняется действие (событие)
        //s = $("input").val(); // берется значение из input или еще какогото елемента
        //s = parseInt(s); // переконвертирует с int
        //d = parseInt(10);
        //var c = s + d;
            //document.write(c);
    //});
 //});

//изменить значение в div допустим после нажания ввода в поле input

//$("document").ready(function () {
    //$("input").keyup(function () {  // используется событие keyup для кнопки
        //var val1 = 10;
        //$("div").html(val1)
    //})
//});


//окно с вопросом, отображение в div
//$("document").ready(function () {
    //test1 = prompt("Как ваше имя ?", ""); // событие prompt (появится окно с первым аргументом,
                                            // то что введем выведется во всех div, можем только одному div, илии еще какому тегу)
    //$("div").html(test1)
//});


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