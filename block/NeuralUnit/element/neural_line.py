"""
!/usr/bin/env python
 -*- coding: utf-8 -*-
 @CreateTime    : 2024-05-10 5:32
 @Author  : Ivan Mao
 @File    : neural_line.py
 @Description : 
"""
from element.line import Line


# @DeprecationWarning
class NeuralLine(Line):

    def __init__(self, direction, formula, position, pindist='1.5cm'):

        super().__init__()
        if direction == 'in':
            self.direction_str = '{latex-}'
        elif direction == 'out':
            self.direction_str = '{-latex}'
        else:
            raise ValueError('direction must be in or out')
        self.formula = formula
        self.position = position
        self.pindist = pindist

    def draw(self):
        return """pin={[pin edge=""" + self.direction_str + f""", pin distance={self.pindist}]""" + self.position + """:{$""" + self.formula + """$}},
                """
