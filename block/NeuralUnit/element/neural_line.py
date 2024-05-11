"""
!/usr/bin/env python
 -*- coding: utf-8 -*-
 @CreateTime    : 2024-05-10 5:32
 @Author  : Ivan Mao
 @File    : neural_line.py
 @Description : 
"""
from element.line import Line


class NeuralLine(Line):
    """
    The NeuralSignal class is a subclass of Signal. It represents a signal in a neural network diagram with additional attributes for direction, formula, and position.
    """

    def __init__(self):
        """
        Initialize a NeuralSignal object with the given direction, formula, and position. The direction must be either 'in' or 'out'.
        """
        super().__init__()
        # if direction == 'in':
        #     self.direction_str = '{-latex}'
        # elif direction == 'out':
        #     self.direction_str = '{latex-}'
        # else:
        #     raise ValueError('direction must be in or out')
        # self.formula = formula
        # self.position = position

    def draw(self,direction, formula, position):
        """
        Returns a string representing a LaTeX command to draw the neural signal with the given direction, formula, and position.
        """
        if direction == 'in':
            direction_str = '{-latex}'
        elif direction == 'out':
            direction_str = '{latex-}'
        else:
            raise ValueError('direction must be in or out')
        return """
                pin={[pin edge=""" + direction_str + """, pin distance=\pindist]""" + position + """:""" + formula + """}
                """
