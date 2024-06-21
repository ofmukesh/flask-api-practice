import logging

# default handler
default_logger = logging.getLogger('app_logger')
default_logger.setLevel(logging.INFO)
default_handler = logging.FileHandler('app.log')
default_formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
default_handler.setFormatter(default_formatter)
default_logger.addHandler(default_handler)

# ------------------------------------------------------------------------------------------------------------------

# default handler
api_logger = logging.getLogger('api_logger')
api_logger.setLevel(logging.INFO)
api_handler = logging.FileHandler('api.log')
api_formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
api_handler.setFormatter(api_formatter)
api_logger.addHandler(api_handler)
