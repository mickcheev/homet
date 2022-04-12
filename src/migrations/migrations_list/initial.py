from migrations.base_migration import BaseMigration


sql_changes = """
    CREATE TABLE MigrationVersion (
        version int PRIMARY KEY
    );
    
    INSERT INTO MigrationVersion VALUES (0);
    
"""

migration = BaseMigration(
    number=1,
    changes =sql_changes 
        )

