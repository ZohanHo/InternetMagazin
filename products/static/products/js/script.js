
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
        //s = $("input").val(); // берется значение из input
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