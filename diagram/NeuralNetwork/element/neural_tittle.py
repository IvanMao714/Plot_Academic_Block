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


class NeuralNetworkTittle(Node):
    def __init__(self, text_position, formula='', name='', text_align='centered', text_width='4em'):
        self.text_width = text_width
        self.text_position = text_position
        self.text_align = text_align
        self.name = self.generate_id() if name == '' else name
        self.formula = formula

    def get_style(self):
        return self.__class__.__name__ + f"""/.style={{text width={self.text_width}, text {self.text_align}}},"""

    def draw(self):
        return f'\n\t\\node[{self.__class__.__name__}, above of={self.text_position[0]}]  at ({self.text_position[0]} |- {self.text_position[1]}) {{{self.formula}}};'
