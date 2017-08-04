#!/usr/bin/env python
# -*- coding: utf-8 -*-

def _(en_text, lan='fa'):

    return '-'+en_text+'-'

    return {
        'newـnote': ['New Note', 'نوشته‌ی جدید'],
        'myـnotes': ['My Notes', 'نوشته‌های من'],


    }.get(en_text, ['TRANSLATOR ERROR','ارور مترجم'])[{
        'en': 0,
        'fa': 1
    }.get(lan)]
