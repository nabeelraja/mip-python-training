import logging
from logging.config import fileConfig
from src.config.config import PROJECT_DIR

print(PROJECT_DIR)

fileConfig(PROJECT_DIR + 'logging_config.ini')
logger = logging.getLogger()
logger.debug('Hello World!!')
