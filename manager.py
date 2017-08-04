#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models import Note
from models import Permission

class Manager:

    @staticmethod
    def add_note(session, user_id, note_title):
        print('new note: ', user_id, note_title)
        if not session.query(Note.title).filter(Note.title == note_title).first():
            new_note = Note(
                title=note_title,
                last_edit_user=user_id,
            )
            session.add(new_note)
            session.flush()
            new_permission = Permission(
                user=user_id,
                note=new_note.id,
                permission_type=Permission.PT.owner
            )
            session.add(new_permission)
            session.commit()
            return True
        else:
            return False

    @staticmethod
    def get_notes(session, user_id):
        all_permissions = session.query(Permission).filter(Permission.user == user_id).all()
        all_notes = [(session.query(Note.title).filter(Note.id == permission.note).first(),
                    permission.permission_type) for permission in all_permissions]
        return [(note.title, permission_type) for note, permission_type in all_notes]
