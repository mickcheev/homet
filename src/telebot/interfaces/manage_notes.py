from notes.services.manage_notes import create_note
from notes.entities import NewNote


def make_note(text: str, user):
    note = NewNote(title=text.split('\n')[0], content=text)
    create_note(note, user)
