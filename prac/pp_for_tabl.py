# Сайт https://scrapingclub.com/exercise/list_basic/?page=1
import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 YaBrowser/24.1.0.0 Safari/537.36'}

# УСТАНОВКА КАРТИНКИ
def download (url):
      # STREAM TRUE - ПОТОКОВАЯ ПЕРЕДАЧА (ТОЕСТЬ КАРТИНКА СРАЗУ НЕ ЦЕЛЕКОМ БУДЕТ ГРУЗИТЬСЯ В ОПЕРАТИВКУ А БУДЕТ ПОРЦИОННО ПОДАВАТЬСЯ)
      resp = requests.get(url, stream=True)
      image_path = 'D:\\Works\\Python\\____3_kurs_works\\pred_cen_kvar\\prac\\images\\' + url.split('/')[-1]

      # СОЗДАНИЕ ФАЙЛА ДЛЯ ЗАПИСИ БАЙТОВ ПОЛУЧ КАРТИНКИ
      with open(image_path, 'wb') as r:
            for value in resp.iter_content(1024 * 1024):
                  r.write(value)

def get_url():
      for count in range(1,8):

            # url = str(input('Введите ссылку: '))
            url = f'https://scrapingclub.com/exercise/list_basic/?page={count}'

            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')
            data = soup.find_all('div', class_='w-full rounded border')

            for i in data:
                  # ПАРС С ЗАХОДОМ В КАЖД СТР
                  card_url = 'https://scrapingclub.com' + i.find('a').get('href')

                  # yield - это создание генератора который позволяет работать с последовательностями данных более эффективно, чем обычные функции, возвращающие все значения сразу. 
                  yield card_url

                  # ПРОХОДИТ ПО ВСЕМ С КЛАССОМ W- И Т.Д.
                  # name = i.find('h4').text
                  # price = i.find('h5').text
                  # url_image = 'https://scrapingclub.com' + i.find('img', class_='card-img-top img-fluid').get('src')

                  # print(name + '\n' + price + '\n' + url_image + '\n')

            # data = soup.find('div', class_='w-full rounded border')
            # name = data.find('h4').text
            # price = data.find('h5').text
            # url_image = 'https://scrapingclub.com' + data.find('img', class_='card-img-top img-fluid').get('src')

# ДЕФ ВЫВОД
# print(response.status_code)
# print(response.text)
# print(soup)
# print(data)
# print(name)
# print(price)
# print(url_image)

# Т.К. ЭТО ГЕНЕРАТОР ТО ОНА СТРАРТАНЁТ И ЗАПРОСИТ ЗНАЧЕНИЯ ГЕНЕРАТОРА get_url()
def array():
    # Базовый URL
    base_url = 'https://scrapingclub.com'

    # ПАРС С ЗАХОДОМ В КАЖД СТР ПРОД
    for card_url in get_url():
        response = requests.get(card_url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        sleep(1)

        data = soup.find('div', class_='my-8 w-full rounded border')
        name = data.find('h3').text
        price = data.find('h4').text
        disc = data.find('p').text

        # Получение URL изображения и добавление базового URL
        url_img = data.find('img').get('src')
        if not url_img.startswith('http'):
            # Формируем абсолютный URL
            url_img = base_url + url_img 

        download(url_img)

      # ПОСЛЕ ТОГО КАК ОН СПАРСИТ ЭТИ ЗНАЧЕНИЯ С 1 КАРТОЧКИ ЭТИ ЗНАЧЕНИЯ ВЕРНУТСЯ В writer()
      # КАК ТОЛЬКО ПОЛУЧАЕТ НУЖНЫЕ ДАННЫЕ ТО СРАЗУ ИХ ЗАПИСЫВАЕТ И ПОТОМ ТОЛЬКО ЗАПРАШИВАЕТ СЛЕД.
        yield name, price, disc, url_img