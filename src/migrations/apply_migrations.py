import sqlite3

from functools import cmp_to_key

from loguru import logger

import config

from migrations.check_migration_version import get_migration_version
from migrations.migrations_list import initial, migration_02, migration_03

migration_list = [initial.migration, migration_02.migration,
        migration_03.migration]

conn = sqlite3.connect(config.DB_PATH)
cursor = conn.cursor()


def cmp(first, second):
    """
    Comporator function. Takes two
    migration objects and returns the newest
    """
    return first.number<second.number


def update_migration_index():
    """
    Updates index of
    last migration in the database 
    """
    now_version = get_migration_version(cursor)
    cursor.execute(f"""Update MigrationVersion SET version={now_version+1}
                     WHERE version={now_version}""")

    conn.commit()

def apply_migrations():
    migration_list.sort(key=cmp_to_key(cmp))
    
    last_migration_number = get_migration_version(cursor)
    
    if last_migration_number == migration_list[-1].number: return

    for migration in migration_list[last_migration_number:]:
        print(migration.number)
        migration.apply_changes(cursor)
        conn.commit()

        logger.info("Migration applyed")

        update_migration_index()

