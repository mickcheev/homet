from loguru import logger
from migrations import make_db_tables

logger.add('debuging.log', level='DEBUG')

make_db_tables.create_database()
