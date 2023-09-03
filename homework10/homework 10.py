import sqlite3

# Підключення до бази даних (створення, якщо її немає)
conn = sqlite3.connect("weather.db")
cursor = conn.cursor()

# Створення таблиці для зберігання даних погоди
cursor.execute('''CREATE TABLE IF NOT EXISTS weather_data
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   date_time DATETIME,
                   temperature TEXT)''')

# Збереження змін у БД
conn.commit()
conn.close()

import requests
from bs4 import BeautifulSoup
import sqlite3
import datetime

# URL веб-сайту з погодою
url = "https://www.bbc.com/weather/2950159"

# Отримання HTML-сторінки
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Пошук елементу з температурою (використовуємо клас "temp" або "wr-value--temperature--c")
temperature_element = soup.find("span", class_=["wr-value--temperature--c"])

if temperature_element:
    temperature = temperature_element.get_text().strip()
else:
    temperature = "N/A"

# Отримання поточної дати та години без хвилин
current_datetime = datetime.datetime.now()
current_datetime_without_minutes = current_datetime.replace(minute=0, second=0, microsecond=0)

# Підключення до бази даних
conn = sqlite3.connect("weather.db")
cursor = conn.cursor()

# Вставка запису в БД
cursor.execute("INSERT INTO weather_data (date_time, temperature) VALUES (?, ?)",
               (current_datetime_without_minutes, temperature))

# Збереження змін у БД
conn.commit()
conn.close()
