$(document).ready(function () {   // document селектор - ето вся страница целиком, ready метод (событие)
    $("#js_bay").on('click', function () {
        var ref = $("#js_bay"); // наша ссылка где прописан data-new_car_id, и остальные
        var new_car_id = ref.data("new_car_id"); // помещает в переменную результат
        var new_car_name = ref.data("new_car_name");
        var new_car_price = ref.data("new_car_price");
        var new_car_price_int = parseInt(new_car_price);
        var num = parseInt(6);
        var total = new_car_price_int * num;

    $("#basket-item ul").append('<li>' + new_car_name+ '<br>' + '$' + new_car_price + '   <a class="delete" href="">Delete</a>' + '</li>'); //по клику добавляем елемент, с перемен. + конкатен


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


$(document).on('click','.delete',function (e) {
    e.preventDefault();
    $(this).closest('li').remove(); // closes ето ближайший к нему елемент и указуем что нам нужен li, удаляем,
});





//var number = 50; // переменная число
//var bool = true; // bool переменная
//var string = "hello zohan"; // переменная строка

//var zohan;
//zohan = 20;



//document.write("Hello" + " world " + (number*zohan)); // вывод на экран
//document.write(bool); // вывод на экран переменной

//alert("Сайт в разработке")


//$('document').ready(function () {   // document селектор - ето вся страница целиком, ready метод (событие)
    //$("body").append('<a href="https://translate.google.cn/m/translate?hl=ru">Google</a>'); // в body подключили тег а (добавили елемент)

    //$("h2").remove(); // по селектору удаляет все тега p

    //var clone;
    //clone= $("p").clone(); // клонирование елементов
    //$("div").append(clone)
//});


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