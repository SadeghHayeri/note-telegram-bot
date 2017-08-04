#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from translator import _

def start():
    keyboard = [[InlineKeyboardButton(_('newـnote'), callback_data='/new_note')],
                [InlineKeyboardButton(_('myـnotes'), callback_data='3')]]
    return InlineKeyboardMarkup(keyboard)
