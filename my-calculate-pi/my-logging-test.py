import logging

logging.basicConfig(level=logging.DEBUG, filename="app.log", filemode='w', format='%(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

debug = 'debug'
info = 'info'

logging.debug("This is a debug message %s", debug)
logging.info("This is a info message")
logging.warning("This is a warning message")
logging.error("This is a error message")
logging.critical("This is a critical message")

name = 'Dansong'
logging.info(f'this is a test for {name} ')

## capture stack trace

a = 3
b = 0

try:
    c = a / b
except Exception as e:
    logging.error('Exception', exc_info=True)


# test custom logger
logger.info('my logger info')


