# SkinArbiter

# Проект: Telegram-бот для арбитража скинов

## Идея проекта
Создать Telegram-бота для арбитража скинов, который покупает скины на одной площадке (Market.CSGO) и продаёт их на другой (Waxpeer) с целью получения прибыли. Бот будет анализировать предметы (CS:GO, Dota 2, Rust, CS2), учитывать ликвидность, автоматически регулировать профит и уведомлять пользователя о сделках через Telegram.

## Архитектура
Проект разбит на несколько независимых модулей, которые взаимодействуют асинхронно через очереди сообщений:
- **Core Bot Service (Telegram Bot + FastAPI):**
  - Базовый функционал взаимодействия с пользователем (команды, кнопки).
  - Работа с конфигурацией и настройками через Telegram.
- **Trade Executor Service:**
  - Алгоритмы поиска арбитражных возможностей.
  - Обработка сделок через внешние API (Market.CSGO и Waxpeer).
  - Динамическое изменение профита.
- **Item Tracker Service:**
  - Хеширование предметов, хранение истории цен.
  - Анализ трендов, подсчёт стоимости наклеек и брелков (для CS2).
- **Notification Service:**
  - Формирование и отправка уведомлений с подробной аналитикой (фото, цены, профит).
- **Steam Trade Manager Service (Node.js):**
  - Подтверждение трейдов, генерация 2FA-кодов для Steam.
  - Обработка входящих trade offer-ов.

## Технологический стек
- **Язык программирования:** Python (aiogram, FastAPI) и Node.js.
- **База данных:** MongoDB для хранения данных, Redis для кэширования и очередей.
- **Очереди сообщений:** RabbitMQ для асинхронных задач.
- **Контейнеризация и оркестрация:** Docker + Kubernetes.
- **Мониторинг и логирование:** Prometheus + Grafana, ELK Stack (Elasticsearch, Logstash, Kibana).

## Стратегия разработки
Проект разделен на 5 этапов:
1. **Этап 1: Базовый функционал Telegram-бота**
   - Инициализация проекта, создание базовых команд и кнопок.
   - Подключение MongoDB, базовое логирование и контейнеризация.
2. **Этап 2: Расширенная логика и работа с данными**
   - Сохранение и обработка пользовательских настроек.
   - Команды для администрирования (например, `/logs`).
3. **Этап 3: Интеграция с API Market.CSGO и Waxpeer**
   - Получение данных с внешних сервисов, WebSocket-листенеры.
4. **Этап 4: Автоматизация сделок и распределение нагрузки**
   - Реализация автоматической обработки сделок через RabbitMQ.
   - Поддержка нескольких Steam-аккаунтов, резервное копирование.
5. **Этап 5: Steam Trade Manager (Node.js)**
   - Автоматизация подтверждения трейдов в Steam, генерация 2FA-кодов.

## Организация работы
Мы будем использовать Notion для управления задачами в виде канбан-доски с колонками:
- **To Do:** Задачи, которые предстоит выполнить.
- **In Progress:** Задачи, над которыми ведется работа.
- **Review / Testing:** Готовые задачи, требующие проверки.
- **Done:** Завершенные задачи.

Каждая задача будет иметь поля: Название, Описание, Приоритет, Этап, Срок выполнения и ответственного.
