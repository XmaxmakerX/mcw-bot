import pywikibot
import requests
import json

SOURCE_URL = "https://raw.githubusercontent.com/misode/mcmeta/summary/item_components/data.json"
COMMIT_API_URL = "https://api.github.com/repos/misode/mcmeta/commits"
PAGE_TITLE = "Модуль:Компоненты предмета по умолчанию/data.json"

# Скачивание JSON с GitHub
print("Скачивание данных с GitHub...")
try:
    response = requests.get(SOURCE_URL)
    response.raise_for_status()
    data = response.json()
    print("Данные успешно скачаны и распарсены.")
except requests.exceptions.RequestException as e:
    print(f"Ошибка при скачивании: {e}")
    exit(1)
except json.JSONDecodeError as e:
    print(f"Ошибка: полученный файл не является валидным JSON: {e}")
    exit(1)

# Получение хеша и сообщения последнего коммита для этого файла
print("Получение информации о последнем коммите...")
commit_sha = "unknown"
commit_message = "unknown"
try:
    params = {
        "path": "item_components/data.json",
        "sha": "summary",
        "per_page": 1
    }
    commit_response = requests.get(COMMIT_API_URL, params=params)
    commit_response.raise_for_status()
    commits = commit_response.json()
    if commits:
        commit_sha = commits[0]["sha"][:7]
        commit_message = commits[0]["commit"]["message"].strip()
        commit_message = commit_message.split("\n")[0].strip()
        while commit_message and not (commit_message[0].isalnum() or commit_message[0] == '-'):
            commit_message = commit_message[1:].strip()
        if commit_message.startswith("Update summary for "):
            commit_message = commit_message.replace("Update summary for ", "", 1)
        print(f"Коммит: {commit_sha} — {commit_message}")
    else:
        print("Коммиты не найдены.")
except Exception as e:
    print(f"Не удалось получить информацию о коммите: {e}")

# Формирование итогового описания правки
summary = f"Обновление в соответствии с {commit_message} ({commit_sha})"

# Подключение к вики
site = pywikibot.Site(code='ru', fam='mcw')
page = pywikibot.Page(site, PAGE_TITLE)

# Форматирование нового JSON для записи
new_text = json.dumps(data, ensure_ascii=False, indent=2)

# Сохранение
print(f"Сохранение с описанием: {summary}")
page.text = new_text
try:
    page.save(summary=summary)
    print("Страница успешно обновлена!")
except Exception as e:
    print(f"Ошибка при сохранении страницы: {e}")
