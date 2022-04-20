from loguru import logger
from migrations import apply_migrations

logger.add('debuging.log', level='DEBUG')


apply_migrations.apply_migrations()
