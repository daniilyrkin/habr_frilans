import requests
from bs4 import BeautifulSoup
import json
import os


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Host': 'freelance.habr.com',
    'Referer': 'https://freelance.habr.com/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '0',
    'sec-ch-ua-platform': "Linux"
}


def download_html():
    for i in range(1, 4):
        url = f'https://freelance.habr.com/tasks?page={i}&q=python'
        response = requests.get(url=url, headers=headers)
        with open(f'index_{i}.html', 'w', encoding='utf-8') as file:
            file.write(response.text)


# Функция для чтения HTML файлов
def read_html():
    for i in range(1, 4):
        with open(f'index_{i}.html', 'r', encoding='utf-8') as f:
            yield f.read()


# Функция для обработки HTML файлов и извлечения данных
def get_data():
    data = []
    for html in read_html():
        soup = BeautifulSoup(html, 'lxml')
        articles = soup.find_all('li', class_='content-list__item')

        for article in articles:
            src = article.find('a')
            title = src.text
            link = 'https://freelance.habr.com' + src.get('href')
            data.append({
                'title': title,
                'link': link})
    return data


def save_json():
    data = get_data()
    print(data)
    open('orders.json', 'w').close()
    with open('orders.json', 'a+', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    delete_html()


def delete_html():
    for i in range(1, 4):
        file_path = f'index_{i}.html'
        os.remove(file_path)
