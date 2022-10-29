import logging
import logging.handlers
import sys


class LogManager:
    """
    The LogManager helps to manage the log
    """

    def __init__(self):
        self.log_level = logging.INFO

        self.logger = logging.getLogger()
        self.logger.setLevel(self.log_level)

        self.string_log_format = '%(asctime)s %(levelname)s - %(message)s'

        self.console_handler = logging.StreamHandler(sys.stdout)  # logging.handlers.SysLogHandler(sys.stdout)
        self.console_handler.setLevel(logging.INFO)
        self.console_handler.setFormatter(logging.Formatter(self.string_log_format))

        self.logger.addHandler(self.console_handler)


log = LogManager()
