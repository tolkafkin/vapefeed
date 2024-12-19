import json
import csv
import os
from datetime import datetime

from vapes.models import Vape, ManufacturerVape


def run():
    """
    Скрипт проверяет есть ли новые девайсы или бренды после парсинга, если да создаёт их,
    созданные девайсы он записывает в CSV файл, в формате Год-Месяц-День
    """
    directory = 'vapes/json_data'
    files = os.listdir(directory)
    sorted_files = sorted(files)

    # Проверяем если там один файл, то создаём все объекты
    if len(sorted_files) == 1:
        data = sorted_files[0]
        data = os.path.join(directory, data)

        with open(data, 'r') as data:
            data = json.load(data)
            new_dict_data = data
    # В противном случае создаём только новые объекты где нет старых
    else:
        data_new = sorted_files[-1]
        data_new = os.path.join(directory, data_new)

        data_old = sorted_files[-2]
        data_old = os.path.join(directory, data_old)

        with open(data_new, 'r') as data_new:
            data_new = json.load(data_new)

        with open(data_old, 'r') as data_old:
            data_old = json.load(data_old)

        new_dict_data = {}
        for brand, devices_new in data_new.items():
            if brand in data_old:
                devices_old = data_old[brand]
                new_devices = [device for device in devices_new if device not in devices_old]

                if not new_devices:
                    continue
            else:
                new_devices = devices_new

            new_dict_data[brand] = new_devices

    if new_dict_data:

        directory = 'vapes/csv_data'
        if not os.path.exists(directory):
            os.makedirs(directory)

        timestamp = datetime.now().strftime('%Y-%m-%d')
        filename = os.path.join(directory, f'{timestamp}.csv')
        with open(filename, "w", encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(
                ('brand', 'device', 'created')
            )

        for brand, devices in new_dict_data.items():
            manufacturer, created = ManufacturerVape.objects.get_or_create(brand_name=brand)

            for name in devices:
                vape, created = Vape.objects.get_or_create(
                    name=name,
                    manufacturer=manufacturer
                )

                with open(filename, "a", encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow(
                        (manufacturer, vape, timestamp)
                    )
    else:
        print('Изменений нет')
