"""
!/usr/bin/env python
 -*- coding: utf-8 -*-
 @CreateTime    : 2024-05-12 0:53
 @Author  : Ivan Mao
 @File    : neural_tittle.py
 @Description : 
"""
from abc import ABC

from element.node import Node


class NeuralTittle(Node):
    def __init__(self, text_width, text_align, name='',formula=''):
        self.text_width = text_width
        self.text_align = text_align
        self.name = self.generate_id() if name == '' else name
        self.formula = formula

    def get_style(self):
        return self.__class__.__name__ + f"""/.style={{text width={self.text_width}, text {self.text_align}}},"""

    def draw(self):
        return f'\\node[{self.__class__.__name__}, text width={self.text_width}, text {self.text_align}] ({self.name}) {{{self.formula}}};'


