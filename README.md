# Боты для службы поддержки пользователей в ВКонтакте и Телеграме

Боты используют Dialogflow для ответов на наиболее распространенные вопросы пользователей.

### Heroku

Код готов к деплою на сервисе [Heroku](heroku.com). Для этого нужно форкнуть этот репозиторий, зарегистрироваться на Heroku и на [странице приложений](https://dashboard.heroku.com/apps) создать новое.

![Кнопка создания нового приложения на Heroku](https://drive.google.com/uc?export=view&id=1ICYYnV57_xX0MBQOL1kfcMEeQ1TxZSc2 "Кнопка создания нового приложения на Heroku")

На странице приложения на вкладке `Deploy` нужно связать аккаунты GitHub и Heroku и задеплоить код из основной ветки.

![Деплой с GitHub](https://drive.google.com/uc?export=view&id=1sWeIS-HcnmHqiEZcPaCiWqgrFdd7pOQM "Деплой с GitHub")

Сервис автоматически установит зависимости из файла `requirements.txt` и считает тип приложения из `Procfile`. Также на вкладке `Resourses` нужно выделить ресурсы для работы ботов.

![Выделение ресурсов для бота](https://drive.google.com/uc?export=view&id=1cz7E68HbYAcbv6n3ZXC3xfIKUH5MCmIB "Выделение ресурсов для бота")

### Настройка переменных окружения

Поскольку код предназначен для работы на сервисе Heroku, в нем используется команда для получения переменных окружения вида `os.environ`. Сами переменные при этом должны находиться в `Config Vars` настройках (`Settings`) приложения на сервисе Heroku.

![Редактирование переменных окружения для приложения на Heroku](https://drive.google.com/uc?export=view&id=1fiNHjoEXQtbCd8zG10IXBLVojSyVszfP "Редактирование переменных окружения для приложения на Heroku")

Использование ключа сервисного аккаунта Google требует установки билдпака. Он устанавливается также на вкладке `Settings` в разделе `Buildpacks`. Адрес билдпака: https://github.com/gerywahyunugraha/heroku-google-application-credentials-buildpack

![Добавление билдпака](https://drive.google.com/uc?export=view&id=1BhV7Mc6iEjtfLdpVeewsaFq4GrilcM-X "Добавление билдпака")

Для работы понадобятся следующие переменные:

```
VK_GROUP_TOKEN=ключ API группы ВКонтакте
TELEGRAM_BOT_TOKEN=токен бота, который будет отвечать пользователям
TELEGRAM_LOGGING_BOT_TOKEN=токен бота, который будет сообщать об ошибках
TELEGRAM_LOGGING_CHAT_ID=чат, в который будут отправляться сообщения об ошибках
DIALOGFLOW_PROJECT_ID=идентификатор проекта в Dialogflow
GOOGLE_APPLICATION_CREDENTIALS=google-credentials.json # эту переменную не нужно менять
GOOGLE_CREDENTIALS=содержимое файла с ключами доступа сервисного аккаунта 
```

### Боты

#### Создание группы ВКонтакте

Бот для ВК отвечает на сообщения, отправленные в группу ВК. Группы в ВК создаются в разделе "Сообщества" [на вкладке "Управление"](https://vk.com/groups?tab=admin)

![Создание группы в ВК](https://drive.google.com/uc?export=view&id=1I3OQiRED4qcxST_Xnm4tT3RubNDmJChh "Создание группы в ВК")

У созданной группы есть меню, в котором нужно выбрать вкладку "Управление"

![Меню управления группы в ВК](https://drive.google.com/uc?export=view&id=1o451zAkHtuD4kJ4NkvLOizlSKhoeMdP- "Меню управления группы в ВК")

После этого в меню "Настройки" нужно выбрать пункт "Работа с API" и создать ключ. Он выглядит примерно так: `6c7ebd785aefe71960e075356477c5e6419deaf5380a1168scd473ddda8f861c97d4f496f09a3ea6eb261` Этот ключ нужно записать в переменную `VK_GROUP_TOKEN`. 

![Настройки группы в ВК](https://drive.google.com/uc?export=view&id=1SFXuUGZsc-triLmAmdwP9gzCyjW8zLwm "Настройки группы в ВК")

#### Создание бота в Телеграм

Для работы понадобятся два бота в Телеграмме: один для ответов пользователям, второй - для отправки ошибок, если первый сломается.

Чтобы создать бота, отправьте пользователю `@BotFather` в Telegram команды `/start` затем `/newbot`. Вы получите API токен для доступа к боту, он выглядит примерно так: `95132391:wP3db3301vnrob33BZdb33KwP3db3F1I`, программа ожидает получить токен основного бота в переменной `TELEGRAM_BOT_TOKEN` и токен бота, который будет сообщать об ошибках, в переменной `TELEGRAM_LOGGING_BOT_TOKEN`.

Чтобы боты смогли отправлять сообщения пользователю, понадобится ID чата, его можно получить, написав `@userinfobot`. ID чата выглядит примерно так: `287621132`, его нужно положить в переменную `TELEGRAM_CHAT_ID`.

### Dialogflow

#### Создание проекта

Проект для работы с API Dialogflow нужно создавать в [консоли Google Cloud Platform](https://console.cloud.google.com). При создании проекта потребуется указать его название (ID), его нужно записать в переменную `DIALOGFLOW_PROJECT_ID`. Подробно о создании проекта для Dialogflow см. [в документации Google Cloud Platform](https://cloud.google.com/dialogflow/docs/quick/setup).

Также для созданного проекта нужно [создать сервисный аккаунт](https://console.cloud.google.com/apis/credentials/serviceaccountkey).

![Создание сервисного аккаунта](https://drive.google.com/uc?export=view&id=1dnJHrCWqbX_wObCThwlDTzJvLgXKRKpk "Создание сервисного аккаунта")

Аккаунту нужно выдать права на редактирование (они нужны для добавления вариантов вопросов-ответов по API). 

![Права сервисного аккаунта](https://drive.google.com/uc?export=view&id=13k-Q2nOIGfnOyk9AsHrRzfisC6xYrN-d "Права сервисного аккаунта")

При создании аккаунта можно (и нужно) сгенерировать для него ключ доступа к API.

![Создание ключа для сервисного аккаунта](https://drive.google.com/uc?export=view&id=1VKnQcjfc2lAtmyqzIS44giO0tmiKN6Ru "Создание ключа для сервисного аккаунта")

Ключ нужен в формате JSON.

![Выбор формата ключа для сервисного аккаунта](https://drive.google.com/uc?export=view&id=1gPHZ1ntKStb0LzZE5OAjUeVYLCaGxsON "Выбор формата ключа для сервисного аккаунта")

Подробно о сервисных проектах см. [в документации Google Cloud Platform](https://cloud.google.com/docs/authentication/getting-started).

При создании проекта 

#### Обучение нейросети

#### Создание сервисного аккаунта для работы с API Dialogflow







# Notification bot for checking reviews on a student's tasks on dvmn.org

The bot uses long polling [API on dvmn.org](https://dvmn.org/api/docs/) to check if a student's work was reviewed.

### Deploy to Heroku

The code is ready to be deployed to [Heroku](heroku.com) service. Fork this repository then register on Heroku and create a new app on the [apps page](https://dashboard.heroku.com/apps).

![Create new app button](https://drive.google.com/uc?export=view&id=1ICYYnV57_xX0MBQOL1kfcMEeQ1TxZSc2 "Create new app button")

Open the application's page and connect your GitHub and Heroku accounts on the `Deploy` tab. Then deploy the main brunch.

![Deploy from GitHub](https://drive.google.com/uc?export=view&id=1sWeIS-HcnmHqiEZcPaCiWqgrFdd7pOQM "Deploy from GitHub")

The service will automatically install the dependencies from the `requirements.txt` file and read the application's type from the `Procfile`. On the `Resources` tab allocate resources for the bot.

![Allocating resources for the bot](https://drive.google.com/uc?export=view&id=1cz7E68HbYAcbv6n3ZXC3xfIKUH5MCmIB "ВAllocating resources for the bot")

### Creating bots and configuring environmental variables

As the code is meant to be used on a Heroku server, the command `os.environ` is used for getting the environmental variables. The variables themselves must be specified in `Config Vars` on the  `Settings` tab of the Heroku application.

![Editing environmental variables](https://drive.google.com/uc?export=view&id=1fiNHjoEXQtbCd8zG10IXBLVojSyVszfP "Editing environmental variables")

You will need two Telegram bots: one for the notifications from dvmn.org and one for error messages in the something goes wrong with the first one.

To create a new bot and get it's ID send to `@BotFather` in Telegram `/start` then `/newbot`. API token for a bot looks like this: `95132391:wP3db3301vnrob33BZdb33KwP3db3F1I`. Call the variable for the main bot's API token `TELEGRAM_BOT_TOKEN` and for the bot for error messages - `TELEGRAM_LOGGING_BOT_TOKEN`.

Provide the user's chat ID so that the bots could send messages to the user. To get the chat ID write to `@userinfobot`. A chat ID looks like this `287621132`, name the variable `TELEGRAM_CHAT_ID`.

To get an API key from dvmn.org, register on the site and copy the key from the [documentation page](https://dvmn.org/api/docs/). The key looks like this `36d45dcbc798a20c0d351b16b490146352583a197`. Name it `DVMN_API_TOKEN`.
