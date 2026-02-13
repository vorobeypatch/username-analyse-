# username-analyse
Скрипт для поиска информации о username, на формах, соц-сети, сайты.


# Как использовать ? 
User Information Finder Bot

📋 Описание

Бот для поиска информации о пользователе в открытых источниках: социальные сети, форумы, сайты и возможные утечки данных.

✨ Функции

· Поиск аккаунтов в 30+ социальных сетях
· Проверка упоминаний на форумах и сайтах
· Поиск возможных утечек данных
· Анимированный процесс поиска
· Сохранение результатов в JSON формате
· Интерактивный интерфейс

🔧 Установка

Windows

```bash
# Установка Python с официального сайта
# https://www.python.org/downloads/

# Установка библиотек
pip install requests beautifulsoup4

# Запуск
python user_bot.py
```

Linux / Ubuntu

```bash
# Установка Python и pip
sudo apt update
sudo apt install python3 python3-pip -y

# Установка библиотек
pip3 install requests beautifulsoup4

# Запуск
python3 user_bot.py
```

📦 Зависимости

```
requests
beautifulsoup4
```

🚀 Использование

1. Запустите бота
2. Введите username для поиска
3. Дождитесь завершения анализа
4. Просмотрите результаты
5. Найдите JSON отчет в папке с программой

📁 Формат JSON отчета

```json
{
  "username": "example",
  "scan_date": "2024-01-01 12:00:00",
  "social_media_accounts": {
    "Telegram": "https://t.me/example",
    "GitHub": "https://github.com/example"
  },
  "forum_mentions": [...],
  "leak_mentions": [...]
}
```

⚠️ Примечание

Используйте только для законных целей и с согласия проверяемых лиц.

👨‍💻 Автор

vorobey patch
