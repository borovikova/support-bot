# Боты для службы поддержки пользователей в ВКонтакте и Телеграме

Боты используют Dialogflow для ответов на наиболее распространенные вопросы пользователей.

![Работа бота для Телеграм](https://user-images.githubusercontent.com/26801826/72070939-fd33fc00-32ea-11ea-9c7d-de78a6e95feb.gif)

Чтобы попробовать бота в работе, напишите ему в Телеграме: @borovik_support_bot


![Работа бота для ВКонтакте](https://user-images.githubusercontent.com/26801826/72071057-366c6c00-32eb-11ea-87ea-27fb7ddca3c1.gif)

Чтобы попробовать бота в работе, напишите в группу: https://vk.com/public190554417

## Боты

### Создание группы ВКонтакте

Бот для ВК отвечает на сообщения, отправленные в группу ВК. Группы в ВК создаются в разделе "Сообщества" [на вкладке "Управление"](https://vk.com/groups?tab=admin)

![Создание группы в ВК](https://user-images.githubusercontent.com/26801826/72070778-9ca4bf00-32ea-11ea-984e-61120f1e627d.png)

У созданной группы есть меню, в котором также нужно выбрать вкладку "Управление"

![Меню управления группы в ВК](https://user-images.githubusercontent.com/26801826/72071494-3620a080-32ec-11ea-97ac-4bd082c03083.png)

После этого в меню "Настройки" нужно выбрать пункт "Работа с API" и создать ключ. Он выглядит примерно так: `6c7ebd785aefe71960e075356477c5e6419deaf5380a1168scd473ddda8f861c97d4f496f09a3ea6eb261` Этот ключ нужно будет записать в переменную `VK_GROUP_TOKEN`. 

![Настройки группы в ВК](https://user-images.githubusercontent.com/26801826/72071533-4c2e6100-32ec-11ea-9805-014e029873d6.png)

### Создание бота в Телеграм

Также понадобятся два бота в Телеграме: один для ответов пользователям, второй - для отправки ошибок, если первый сломается.

Чтобы создать бота, отправьте пользователю `@BotFather` в Telegram команды `/start` затем `/newbot`. Вы получите API токен для доступа к боту, он выглядит примерно так: `95132391:wP3db3301vnrob33BZdb33KwP3db3F1I`, программа ожидает получить токен основного бота в переменной `TELEGRAM_BOT_TOKEN` и токен бота, который будет сообщать об ошибках, в переменной `TELEGRAM_LOGGING_BOT_TOKEN`.

Чтобы боты смогли отправлять сообщения пользователю, понадобится ID чата, его можно получить, написав `@userinfobot`. ID чата выглядит примерно так: `287621132`, его нужно будет положить в переменную `TELEGRAM_CHAT_ID`.

## Dialogflow

### Создание проекта

Проект для работы с API Dialogflow нужно создавать в [консоли Google Cloud Platform](https://console.cloud.google.com). При создании проекта потребуется указать его название (ID), его нужно записать в переменную `DIALOGFLOW_PROJECT_ID`. Подробно о создании проекта для Dialogflow см. [в документации Google Cloud Platform](https://cloud.google.com/dialogflow/docs/quick/setup).

![Кнопка создания нового проекта](https://user-images.githubusercontent.com/26801826/72072839-0b841700-32ef-11ea-986c-f27644683084.png)

![Окно создания нового проекта](https://user-images.githubusercontent.com/26801826/72072916-29ea1280-32ef-11ea-8c25-0ad5df421844.png)

### Создание сервисного аккаунта для работы с API Dialogflow

Также для созданного проекта нужно [создать сервисный аккаунт](https://console.cloud.google.com/apis/credentials/serviceaccountkey).

![Создание сервисного аккаунта](https://user-images.githubusercontent.com/26801826/72071581-68320280-32ec-11ea-8f32-3901ec6272c4.png)

Аккаунту нужно выдать права на редактирование (они нужны для обучения нейросети по API).

![Права сервисного аккаунта](https://user-images.githubusercontent.com/26801826/72071582-68320280-32ec-11ea-9769-6505ec6d872e.png)

При создании аккаунта нужно сгенерировать для него ключ доступа к API.

![Создание ключа для сервисного аккаунта](https://user-images.githubusercontent.com/26801826/72071583-68320280-32ec-11ea-9b75-a1c927bad07c.png)

Ключ нужен в формате JSON.

![Выбор формата ключа для сервисного аккаунта](https://user-images.githubusercontent.com/26801826/72071585-68320280-32ec-11ea-8b07-027b62149ee3.png)

Подробно о сервисных аккаунтах см. [в документации Google Cloud Platform](https://cloud.google.com/docs/authentication/getting-started).

### Обучение нейросети

Файл `questions.json` содержит ответы на часто задаваемые вопросы и ответы на них. Чтобы обучить нейросеть Dialogflow на этих данных, нужно склонировать репозиторий на локальный компьютер и один раз запустить файл `create_intent.py`.

```
python create_intent.py
```

Для работы скрипту понадобится файл .env с переменными

```
DIALOGFLOW_PROJECT_ID=идентификатор проекта в Dialogflow
GOOGLE_APPLICATION_CREDENTIALS=файл с ключами доступа сервисного аккаунта
```

## Heroku

Код готов к деплою на сервисе [Heroku](heroku.com). Для этого нужно форкнуть этот репозиторий, зарегистрироваться на Heroku и на [странице приложений](https://dashboard.heroku.com/apps) создать новое.

![Кнопка создания нового приложения на Heroku](https://user-images.githubusercontent.com/26801826/72071872-0aea8100-32ed-11ea-9a0e-7c28d584798d.png)

На странице приложения на вкладке `Deploy` нужно связать аккаунты GitHub и Heroku и задеплоить код из основной ветки.

![Деплой с GitHub](https://user-images.githubusercontent.com/26801826/72071871-0a51ea80-32ed-11ea-9d74-f37a1881fe18.png)

Сервис автоматически установит зависимости из файла `requirements.txt` и считает тип приложения из `Procfile`. Также на вкладке `Resourses` нужно выделить ресурсы для работы ботов.

### Настройка переменных окружения

Поскольку код предназначен для работы на сервисе Heroku, в нем используется команда для получения переменных окружения вида `os.environ`. Сами переменные при этом должны находиться в `Config Vars` настройках (`Settings`) приложения на сервисе Heroku.

Использование ключа сервисного аккаунта Google требует установки билдпака. Он устанавливается также на вкладке `Settings` в разделе `Buildpacks`. Адрес билдпака: https://github.com/gerywahyunugraha/heroku-google-application-credentials-buildpack

![Добавление билдпака](https://user-images.githubusercontent.com/26801826/72071759-d4ad0180-32ec-11ea-8bc8-6ec9a408cfd0.png)

Для работы ботов на Heroku понадобятся следующие переменные:
```
VK_GROUP_TOKEN=ключ API группы ВКонтакте
TELEGRAM_BOT_TOKEN=токен бота, который будет отвечать пользователям
TELEGRAM_LOGGING_BOT_TOKEN=токен бота, который будет сообщать об ошибках
TELEGRAM_LOGGING_CHAT_ID=чат, в который будут отправляться сообщения об ошибках
DIALOGFLOW_PROJECT_ID=идентификатор проекта в Dialogflow
GOOGLE_APPLICATION_CREDENTIALS=google-credentials.json # эту переменную не нужно менять
GOOGLE_CREDENTIALS=содержимое файла с ключами доступа сервисного аккаунта 
```