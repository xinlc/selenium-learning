import logging

my_format = '%(asctime)s-%(filename)s-%(module)s-%(lineno)d'

logging.basicConfig(
    filename='my.log',
    level=logging.INFO,
    format=my_format
)

#
logging.info('infor')
logging.debug('debug')
logging.warning('warning')
logging.error('error')
logging.critical('critical')
