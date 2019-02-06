# 1. Парсер однопоточный
# 2. Замер времени
# 3. multiprocessing Pool
# 4. Замер времена
# 4. Експорт в csv

# Парсим при помощи библитеки BeautifulSoup4 предварительно установив как и реквест через pip install
# pip install BeautifulSoup4
# pip install request



import requests  # Библиотека будет получать код страницы и возвращать код в другую фунцию
from bs4 import BeautifulSoup
import csv
from datetime import datetime
from multiprocessing import Pool

def get_html(ulr): # в качестве аргумента принимае url, которую будем парсить
    response_server = requests.get(ulr) # response сервера получим
    return response_server.text # возвращает с респонса только текст (html код страницы которая передана в качестве аргусента)


def get_all_links(html): # Принимает html код страницы
    soup = BeautifulSoup(html, 'lxml') # принимает html и назавание парсера
    # вызываем метод find и в качестве первого аргумента передаем html тег тейбл и id тега, далее ищим все td и класс тега currency-name
    # Получаем список обьктов soup, не список td, к которому приминимы все свойства обьекта soup
    td = soup.find('table', id="currencies-all").find_all('td', class_ = 'currency-name')

    links = []
    for foo in td:
        a = foo.find('a').get("href") # ищим тег а и забираем путь с href, ето уже строка
        link = 'https://coinmarketcap.com' + a # конкатенация для добавления домена
        links.append(link)
    return links

    # Парсим все ссылки
def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        # вызываем свойство текст, после чего обьект soup стфновится строкой, strip - удаляет все непечатаемые символы (типа каретки и переноса строки)
        name = soup.find('h1',  class_="text-bold").text.strip() # Парсим имя
    except:
        name = ''

    try:
        price = soup.find('span', id="quote_price" ).text.strip()  # Парсим цену
    except:
        price = ''



    data = {'name' : name, 'price': price}

    return data # возврашаем словарь

#  Записываем данные в фаил
def write_csv(data):
    with open('coinmarket.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow( (data["name"], data["price"]))
        print(data["name"], "Спарсено имя")
        print(data["price"], "Спарсено цену")


def make_all(url):
    html = get_html(url)
    data = get_page_data(html)
    write_csv(data)

def main():
    start = datetime.now()

    url = 'https://coinmarketcap.com/all/views/all'
    all_links = get_all_links(get_html(url)) # список со ссылками


    # for index, url in enumerate(all_links):
    #     html = get_html(url)
    #     data = get_page_data(html)
    #     write_csv(data)

    with Pool(50) as p:
        p.map(make_all, all_links)

    end = datetime.now()
    total = end - start
    print(str(total))

if  __name__ == '__main__':
    main()



