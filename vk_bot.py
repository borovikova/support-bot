import os
from dotenv import load_dotenv
import dialogflow_v2 as dialogflow
import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from dialogflow_process_pharse import process_phrase
import logging
import telegram
from logs_handler import TelegramHandler


def echo(event, vk_api, project_id):
    response = process_phrase(project_id, event.user_id, event.text, 'ru-RU')
    if response:
        vk_api.messages.send(
            user_id=event.user_id,
            message=response,
            random_id=random.randint(1, 1000)
        )


if __name__ == "__main__":
    load_dotenv()
    project_id = os.environ["DIALOGFLOW_PROJECT_ID"]
    group_token = os.environ["VK_GROUP_TOKEN"]
    logging_bot_token = os.environ["TELEGRAM_LOGGING_BOT_TOKEN"]
    chat_id = os.environ["TELEGRAM_LOGGING_CHAT_ID"]
    logging_bot = telegram.Bot(logging_bot_token)

    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger()
    logger.setLevel(logging.WARNING)
    logger.addHandler(TelegramHandler(logging_bot, chat_id))

    vk_session = vk_api.VkApi(token=group_token)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)

    while True:
        try:
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                    echo(event, vk_api, project_id)
        except Exception:
            logger.exception("Бот для ВК упал с ошибкой:")
