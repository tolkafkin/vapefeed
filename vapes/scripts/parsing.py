from bs4 import BeautifulSoup
import requests
import os
import json
from datetime import datetime


def get_brands(url):
    """
    Функция для сбора имени брендов и ссылок на них.
    :param url: Ссылка где находятся все вендоры
    :type url: str
    :return: Словарь, где ключ это имя, а значение ссылка на бренд
    :rtype: dict
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    brands = soup.find_all('div', class_='manufactured-item')
    dict_brands = {}

    for brand in brands:
        brand_name = brand.find('p', class_='manufactured-item-title').text
        brand_link = brand.find('a')['onclick'].split("'")[1]
        dict_brands[brand_name] = brand_link

    return dict_brands


def get_devices(brand, url):
    """
    Функция для сбора всех уникальных девайсов одного бренда
    :param brand: Название бренда
    :type brand:
    :param url: Ссылка на бренд
    :type url: str
    :return: Список уникальных девайсов
    :rtype: list
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    devices = soup.find_all('div', class_='lighter-item')
    unique_device_names = set()

    # Перебираем линейки
    for device in devices:
        device_name = device.find('p', class_='lighter-item-title').text
        unique_device_names.add(device_name)

    # Если линеек нет, то проходимся по каждому девайсу и узнаём их линейку
    if not unique_device_names:
        devices = soup.find_all('h3', class_="product-title")
        for device in devices:
            device_name = device.text.lower()
            # Проверяем есть ли эта линейка в нашем списке, если её нет до добавляем, если есть то идём дальше
            if not any(item.lower() in device_name for item in unique_device_names):
                device_link = device.find('a')['href']
                full_device_link = "https://smokenvape.shop" + device_link
                response = requests.get(full_device_link)
                # Иногда страница девайса может быть не найдена
                if response.status_code != 404:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    brand_span = soup.find('span', string='Бренд')
                    if brand_span:
                        brand_name = brand_span.find_next('a').text
                        # Проверяем является ли бренд таким же в каком вендоре мы сейчас находимся,
                        # если нет то идём к следующему вендору
                        if brand_name != brand:
                            break
                    line_span = soup.find('span', string='Линейка')
                    if line_span:
                        line_name = line_span.find_next('a').text
                        unique_device_names.add(line_name)
    return list(unique_device_names)


def run():
    """
    Скрипт выполняет парсинг брендов и девайсов, затем сохраняет их в виде JSON,
    в каталоге data_vape, по имени Год-месяц-день
    """
    url = 'https://smokenvape.shop/vendors/'
    brands = get_brands(url)
    devices = {brand: get_devices(brand, 'https://smokenvape.shop' + url) for brand, url in brands.items()}

    directory = 'vapes/json_data'
    if not os.path.exists(directory):
        os.makedirs(directory)

    timestamp = datetime.now().strftime('%Y-%m-%d')
    filename = os.path.join(directory, f'{timestamp}.json')

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(devices, f, ensure_ascii=False, indent=4)
