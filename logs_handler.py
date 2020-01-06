import telegram
import logging

  class MyLogsHandler(logging.Handler):
    def emit(self, record):
        log_entry = self.format(record)
        logging_bot.send_message(chat_id, log_entry)