from migrations.base_migration import BaseMigration


sql_changes = """
    CREATE TABLE Note(
        id INTEGER,
        title TEXT,
        creation_date DATE,
        last_change_date DATE,
        content TEXT,
        permission INTEGER
    );

"""

migration = BaseMigration(
    number=3,
    changes =sql_changes 
        )

