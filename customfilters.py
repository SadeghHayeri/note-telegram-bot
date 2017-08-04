#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import BaseFilter

class ScenarioFilter(BaseFilter):
    def __init__(self, scenarios):
        self.scenarios = scenarios

    def filter(self, message):
        print('check scenario for ', message.from_user.id, self.scenarios.checkUser(message.from_user.id))
        return self.scenarios.checkUser(message.from_user.id)
