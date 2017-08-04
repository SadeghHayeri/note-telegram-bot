#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from translator import _
from models import Permission

def main_menu(note_exist=True):
    keyboard = [[InlineKeyboardButton(_('newـnote'), callback_data=u'/new_note')]]
    if note_exist:
        keyboard.append([InlineKeyboardButton(_('myـnotes'), callback_data=u'/myـnotes')])
    return InlineKeyboardMarkup(keyboard)

def note_list(notes):
    def per_type(per):
        return {
            Permission.PT.owner: _('owner'),
            Permission.PT.can_edit: _('can_edit'),
            Permission.PT.can_read: _('read_only')
        }[per]

    keyboard = [[InlineKeyboardButton(per_type(note[1]) + note[0], callback_data=u'/note/'+note[0])] for note in notes]
    keyboard.append([InlineKeyboardButton(_('back'), callback_data=u'/main_menu')])
    return InlineKeyboardMarkup(keyboard)
