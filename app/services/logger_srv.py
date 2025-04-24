import logging


class AppLogger:
    def __init__(
            self,
            name: str = "app",
            log_level="INFO",
            log_format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
         ):
        self.log_level_mapping = {
            "INFO": logging.INFO,
            "DEBUG": logging.DEBUG,
            "ERROR": logging.ERROR,
            "WARNING": logging.WARNING
        }

        self.logger = logging.getLogger(name)
        self.logger.setLevel(self.log_level_mapping[log_level])

        # Avoid duplicate handlers
        formatter = logging.Formatter(log_format)

        # Always add console handler
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)

    def get_logger(self):
        return self.logger
