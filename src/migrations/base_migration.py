class BaseMigration:
    def __init__(self, number: int, changes: str):
        self.number = number
        self.changes = changes

    def apply_changes(self, cursor):
        cursor.executescript(self.changes)

