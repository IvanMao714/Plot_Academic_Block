"""
!/usr/bin/env python
 -*- coding: utf-8 -*-
 @CreateTime    : 2024-05-12 0:53
 @Author  : Ivan Mao
 @File    : tittle.py
 @Description : 
"""
from abc import ABC

from element.node import Node


class Tittle(Node):
    def __init__(self, text_width, text_position, text_align='centered', name='', formula=''):
        self.text_width = text_width
        self.text_position = text_position
        self.text_align = text_align
        self.name = self.generate_id() if name == '' else name
        self.formula = formula

    def get_style(self):
        return self.__class__.__name__ + f"""/.style={{text width={self.text_width}, text {self.text_align}}},"""

    def draw(self):
        return f'\n\t\\node[{self.__class__.__name__}, text width={self.text_width}, above of={self.text_position}] ({self.name}) {{{self.formula}}};'


