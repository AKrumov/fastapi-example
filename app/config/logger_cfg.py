from app.services.logger_srv import AppLogger
from app.config.settings_cfg import Settings

config = Settings().log
logger = AppLogger(log_level=config['level'], log_format=config['format']).get_logger()
