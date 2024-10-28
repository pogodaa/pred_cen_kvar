# Сайт https://quotes.toscrape.com/

# session сохраняет файлы cookie
from requests import Session
from bs4 import BeautifulSoup
from time import sleep

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 YaBrowser/24.1.0.0 Safari/537.36'}

def get_disc_autor():
      work = Session()
      work.get('https://quotes.toscrape.com/', headers=headers)
      response = work.get('https://quotes.toscrape.com/login', headers=headers)

      soup = BeautifulSoup(response.text, 'lxml')

      token = soup.find('form').find('input').get('value')

      data = {"csrf_token": token, "username": "not_fake", "password": "777"}

      # allow_redirectcts - ПЕРЕНАПРАВЛЕНИЕ
      result = work.post("https://quotes.toscrape.com/login", headers=headers, data=data, allow_redirects=True)

      while True:
            soup_updt = BeautifulSoup(result.text, 'lxml')
            dataZ = soup_updt.find_all('div', class_='quote')

            for elem in dataZ:
                  disc = elem.find('span', class_='text').text
                  author = elem.find('small').text
                  yield disc, author

            # Проверка на наличие следующей страницы
            next_page = soup_updt.find('li', class_='next')
            if next_page:
                  url = 'https://quotes.toscrape.com' + next_page.find('a')['href']
                  # sleep(1)
            else:
                  break