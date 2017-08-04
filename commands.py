#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models import User
from sqlalchemy.orm import sessionmaker
import logging
import keyboards
from sqlalchemy import create_engine
from translator import _
from scenarios import Scenurios
from manager import Manager

from YamJam import yamjam
db_CFG = yamjam()['sharenote']['database']

class Commands:

    def __init__(self):
        # Create database session connection
        Session = sessionmaker()
        engine = create_engine('postgresql://%s:%s@%s:%d/%s' % (db_CFG['user'],
                                                                db_CFG['password'],
                                                                db_CFG['host'],
                                                                db_CFG['port'],
                                                                db_CFG['name']))
        Session.configure(bind=engine)
        self.session = Session()

        # Create scenarios manager
        self.scenarios = Scenurios(self, self.session)

        # Enable logging
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def getSenarios(self):
        return self.scenarios

    # /start
    def main_menu(self, bot, update):
        from_user = update.message.from_user if update.message else update.callback_query.from_user
        if not self.session.query(User.id).filter(User.id == from_user.id).first():
            new_user = User(
                id=from_user.id,
                username=from_user.username,
                first_name=from_user.first_name,
                last_name=from_user.last_name,
                language=from_user.language_code
            )
            self.session.add(new_user)
            self.session.commit()

        note_exist = False if len(Manager.get_notes(self.session, from_user.id)) == 0  else True
        if update.message:
            update.message.reply_text(text=_('welcome_message'),
                                        reply_markup=keyboards.main_menu(note_exist=note_exist))
        else:
            query = update.callback_query
            bot.edit_message_text(text=_('welcome_message'),
                                    chat_id=query.message.chat_id,
                                    message_id=query.message.message_id,
                                    reply_markup=keyboards.main_menu(note_exist=note_exist))

###########
    def s_new_note_0(self, bot, update):
        query = update.callback_query
        bot.edit_message_text(text=_('get_title'),
                                chat_id=query.message.chat_id,
                                message_id=query.message.message_id)

    def s_new_note_1(self, bot, update):
        update.message.reply_text(text=_('get_title_with_error_title'))
###########

    def show_notes(self, bot, update):
        query = update.callback_query
        print('show notes for user:', query.from_user.id)
        notes = Manager.get_notes(self.session, query.from_user.id)
        bot.edit_message_text(text=_('your_notes'),
                                chat_id=query.message.chat_id,
                                message_id=query.message.message_id,
                                reply_markup=keyboards.note_list(notes))

    # all buttons click
    def button_handler(self, bot, update):
        query = update.callback_query

        if self.scenarios.checkUser(query.from_user.id):
            self.scenarios.handler(bot, update)
        else:
            print('click on: ', query.data)
            if '/new_note' in query.data:
                self.scenarios.startScenurio(bot, update, 'new_note')
            elif u'/my\u0640notes' in query.data:
                self.show_notes(bot, update)
            elif '/main_menu' in query.data:
                self.main_menu(bot, update)

    # /help
    def help(self, bot, update):
        update.message.reply_text('Help!')

    # other messages
    def echo(self, bot, update):
        update.message.reply_text(update.message.text)

    #
    def error(self, bot, update, error):
        self.logger.warn('Update "%s" caused error "%s"' % (update, error))
