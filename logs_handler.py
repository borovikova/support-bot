import telegram
import logging


class TelegramHandler(logging.Handler):
    def __init__(self, bot, chat_id):
        logging.Handler.__init__(self)
        self.logging_bot = bot
        self.chat_id = chat_id

    def emit(self, record):
        log_entry = self.format(record)
        self.logging_bot.send_message(self.chat_id, log_entry)
