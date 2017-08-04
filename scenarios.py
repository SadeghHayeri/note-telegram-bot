#!/usr/bin/env python
# -*- coding: utf-8 -*-

from manager import Manager

class Scenurios:
    def __init__(self, commands, session):
        self.new_note = self.New_Note(commands, session)

    def startScenurio(self, bot, update, kind):
        print('starting a scenario!')
        if kind == 'new_note':
            self.new_note.start(bot, update)

    def handler(self, bot, update):
        user_id = update.message.from_user.id
        if self.new_note.checkUser(user_id):
            self.new_note.handler(bot, update)

    def checkUser(self, id):
        if self.new_note.checkUser(id):
            return True
        return False


    class New_Note:
        def __init__(self, commands, session):
            self.status = {}
            self.commands = commands
            self.session = session

        def checkUser(self, user_id):
            return user_id in self.status

        def start(self, bot, update):
            user_id = update.callback_query.from_user.id
            self.status[user_id] = {'level': 0, 'data': {}}
            self.commands.s_new_note_0(bot, update)

        def handler(self, bot, update):
            user_id = update.message.from_user.id
            {
                0: self.get_title,

            }[self.status[user_id]['level']](bot, update)

        def get_title(self, bot, update):
            user_id = update.message.from_user.id
            note_title = update.message.text
            self.status[user_id]['data']['name'] = note_title

            if Manager.add_note(self.session, user_id, note_title):
                self.status[user_id]['data']['level'] = 1
                self.commands.main_menu(bot, update)
                self.end(user_id)
            else:
                self.commands.s_new_note_1(bot, update)

        def end(self, user_id):
            del self.status[user_id]
