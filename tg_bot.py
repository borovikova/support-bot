import os
import telegram
from dotenv import load_dotenv
from telegram.ext import Updater, Dispatcher, CommandHandler, MessageHandler, Filters
from dialogflow_process_pharse import process_phrase
import logging
from functools import partial
from logs_handler import TelegramHandler

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text="Здравствуйте!")


def echo(bot, update, project_id):
    chat_id = update.message.chat_id
    text = update.message.text
    response = process_phrase(project_id, chat_id, text, 'ru-RU')
    if response:
        bot.send_message(chat_id=chat_id, text=response)


if __name__ == "__main__":
    load_dotenv()
    project_id = os.environ["DIALOGFLOW_PROJECT_ID"]
    bot_token = os.environ["TELEGRAM_BOT_TOKEN"]
    logging_bot_token = os.environ["TELEGRAM_LOGGING_BOT_TOKEN"]
    chat_id = os.environ["TELEGRAM_LOGGING_CHAT_ID"]
    logging_bot = telegram.Bot(logging_bot_token)

    logger = logging.getLogger()
    logger.setLevel(logging.WARNING)
    logger.addHandler(TelegramHandler(logging_bot, chat_id))

    echo_partial = partial(
        echo,
        project_id=project_id
    )
    try:
        updater = Updater(token=bot_token)
        dispatcher = updater.dispatcher
        start_handler = CommandHandler('start', start)
        dispatcher.add_handler(start_handler)
        echo_handler = MessageHandler(Filters.text, echo_partial)
        dispatcher.add_handler(echo_handler)
        updater.start_polling()
    except Exception:
        logger.exception("Бот для ТГ упал с ошибкой:")
