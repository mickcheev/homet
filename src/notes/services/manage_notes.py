from datetime import date

from notes.models import Note
from notes.entities import NewNote, EditNote, GetNote
from users.models import User


def create_note(note: NewNote, user: User):
    return Note.create(title=note.title, content=note.content, author=user)


def update_note(note: EditNote):
    db_note: Note = Note.get(Note.id == note.id)
    db_note.title = note.new_title
    db_note.content = note.new_content
    db_note.last_change_date = date.today()
    db_note.save()


def db_to_entity(note: Note):
    return GetNote(title=note.title, content=note.content, created=str(note.creation_date),
                   last_changed=str(note.last_change_date), id=note.id)


def get_notes_list(user: User):
    result = []
    for note_obj in list(Note.select().where(Note.author == user)):
        result.append(db_to_entity(note_obj))

    return result
