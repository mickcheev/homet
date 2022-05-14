from datetime import date

from notes.models import Note
from notes.entities import NewNote, EditNote
from users.models import User


def create_note(note: NewNote, user: User):
    return Note.create(title=note.title, content=note.content, author=user)


def update_note(note: EditNote):
    db_note: Note = Note.get(Note.id == note.id)
    db_note.title = note.new_title
    db_note.content = note.new_content
    db_note.last_change_date = date.today()
    db_note.save()
