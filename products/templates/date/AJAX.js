// осуществляем асинхронный запрос к файлу для того что бы полусить JSON данные


// XMLHttprequest   -  В javascript есть встроеный обьект, который реалтзует нам ajax, ответы можно получать в разных форматах не только XML и JSON

function LoadJson () {


    var Object_XML_H_R = new XMLHttpRequest(); // создаем екземпляр класса XMLHttpRequest
    console.log(Object_XML_H_R);


    Object_XML_H_R.open("GET", 'players.json', true); // конфигурируем запрос с помощью метода open, первое тип запросв, второе, путь("/url/") или имя файла,
    // третее тип запроса, синх. тлт асинх. (метод опен не отправляет данные на сервер, только готовит)

    // могут быть синхронные и асинхронные зарносы, синхронный не работвет дальне (не выполняется никакие функции пока не получен ответ)
    //asinc = true   запрос асинхронный, почти всегда используются асинхронные запросы
    //asinc = false   запрос синхронный

        Object_XML_H_R.send(); // отправляет запрос на сервер
    // в пост запросе есть обязательный парамент body  ObjectXML_H_R.send(body);


    Object_XML_H_R.onreadystatechange = function () {  // onreadystatechange - собыие состояния сервера (готов ли сервер с нами работать проверяем)

        // у сервера есть 5 состояний, 0 - сотояние, 1 - конфигурация, 2 - отправка, 3 - получение ответа, 4 - ответ сформирован
        if (Object_XML_H_R.readyState != 4) return; // если ответ не готов то выходим отсюда

        if (Object_XML_H_R.status != 200) {
            console.log(Object_XML_H_R.status, +': ' + Object_XML_H_R.statusText)
        } else { // если статус 200
            document.write(Object_XML_H_R.responseText);  // responseText - выводим наши данные в виде строки если все гуд

            var parse = JSON.parse(Object_XML_H_R.responseText);
            console.log(typeof Object_XML_H_R.responseText); // typeof - можем узнать тип обьекта
            document.write(parse["players"][0]["lastname"]) // распарсил что бы получить имя
        }
    };

}
