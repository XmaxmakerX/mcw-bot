## Информация

Простой бот для [русскоязычной Minecraft Wiki](https://ru.minecraft.wiki/) от [XmaxmakerX](https://ru.minecraft.wiki/User:XmaxmakerX).

- [Страница бота](https://ru.minecraft.wiki/User:XmaxmakerXBot) · [Обсуждение](https://ru.minecraft.wiki/User_talk:XmaxmakerXBot)

## Основные задачи

- Обновление [данных компонентов предметов по умолчанию](https://ru.minecraft.wiki/Module:Компоненты_предмета_по_умолчанию/data.json) на основе [item_components/data.json](https://github.com/misode/mcmeta/blob/summary/item_components/data.json) в [misode/mcmeta](https://github.com/misode/mcmeta).

Запуск бота происходит каждый день в 00:00 по МСК.

## Технологии

| Компонент | Что используется |
|-----------|------------------|
| Язык | Python 3.12 |
| Фреймворк для работы с вики | [Pywikibot](https://www.mediawiki.org/wiki/Manual:Pywikibot) 11.x |
| HTTP-запросы к GitHub | [requests](https://requests.readthedocs.io/) |
| Планировщик | GitHub Actions (cron) |
| Формат данных | JSON |
