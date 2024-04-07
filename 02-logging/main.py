import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
    filename='example.log', 
    encoding='utf-8',
    level=logging.DEBUG,
    format='%(asctime)s; %(levelname)s; %(message)s', 
    datefmt='%m/%d/%Y %I:%M:%S %p'
)


logger.debug('This message should go to the log file')
logger.info('So should this')
logger.warning('And this, too')
logger.error('And non-ASCII stuff, too, like Øresund and Malmö')