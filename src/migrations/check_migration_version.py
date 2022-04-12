def get_migration_version(cursor):

    try:
        cursor.execute('SELECT version FROM MigrationVersion')

    except Exception:
        
        return 0
    
    return cursor.fetchall()[0][0]



