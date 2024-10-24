import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 YaBrowser/24.1.0.0 Safari/537.36'}

url = str(input('Введите ссылку: '))
# url = f'https://scrapingclub.com/exercise/list_basic/?page={count}'
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'lxml')

data = soup.find_all('div', class_='w-full rounded border')
for i in data:
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
      print(response.status_code)
      # print(response.text)
      # print(soup)
      # print(data)
      # print(name)
      # print(price)
      # print(url_image)