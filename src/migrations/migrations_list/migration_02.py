from migrations.base_migration import BaseMigration


sql_changes = """
    CREATE TABLE User(
        first_name TEXT,
        second_name TEXT,
        password TEXT,
        email TEXT PRIMARY KEY,
        accession_date TEXT,
        telegram_account TEXT

    );

"""
migration = BaseMigration(
    number=2,
    changes =sql_changes 
        )

