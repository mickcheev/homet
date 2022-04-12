from migrations.base_migration import BaseMigration


sql_changes = """
    CREATE TABLE User(
        name TEXT,
        second_name TEXT,
        password TEXT,
        email TEXT PRIMARY KEY,
        join_date TEXT,
        telegram TEXT

    );
    
    INSERT INTO MigrationVersion VALUES (0);
    
"""

migration = BaseMigration(
    number=2,
    changes =sql_changes 
        )

