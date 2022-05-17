from loguru import logger
from migrations import make_db_tables
from fastapi import FastAPI

logger.add('debuging.log', level='DEBUG')

make_db_tables.create_database()


app = FastAPI()

from server import main
