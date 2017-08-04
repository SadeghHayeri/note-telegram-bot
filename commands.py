#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models import User
from sqlalchemy.orm import sessionmaker
import logging
import keyboards
from sqlalchemy import create_engine
from translator import _

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

        # Enable logging
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    # /start
    def start(self, bot, update):
        if not self.session.query(User.id).filter(User.id == update.message.from_user.id).first():
            new_user = User(
                id=update.message.from_user.id,
                username=update.message.from_user.username,
                first_name=update.message.from_user.first_name,
                last_name=update.message.from_user.last_name,
                language=update.message.from_user.language_code
            )
            self.session.add(new_user)
            self.session.commit()
        update.message.reply_text(_('welcome_message'), reply_markup=keyboards.start())


    def button(self, bot, update):
        query = update.callback_query

        bot.edit_message_text(text="Selected option: %s" % query.data,
                                reply_markup=keyboards.start(),
                                chat_id=query.message.chat_id,
                                message_id=query.message.message_id)

    # /help
    def help(self, bot, update):
        update.message.reply_text('Help!')

    # other messages
    def echo(self, bot, update):
        update.message.reply_text(update.message.text)

    #
    def error(self, bot, update, error):
        self.logger.warn('Update "%s" caused error "%s"' % (update, error))
