"""
!/usr/bin/env python
 -*- coding: utf-8 -*-
 @CreateTime    : 2024-05-09 3:51
 @Author  : Ivan Mao
 @File    : signal.py
 @Description : This module contains the Signal and NeuralSignal classes used for creating and drawing signals in a neural network diagram.
"""


class Signal:
    """
    The Signal class represents a signal in a neural network diagram. It has attributes for color, arrow type, width, and line type.
    """

    def __init__(self, color='black', arrow_type='->', width='1.5pt', line_type='line'):
        """
        Initialize a Signal object with the given color, arrow type, width, and line type. Defaults are provided for all parameters.
        """
        self.color = color
        self.arrow_type = arrow_type
        self.width = width
        self.line_type = line_type

    def get_style(self):
        """
        Returns a string representing the style of the signal in LaTeX format.
        """
        return self.__class__.__name__+f"""/.style={{draw={self.color}, {self.arrow_type}, {self.line_type} width={self.width}}},"""

    def __draw(self, x1, y1, x2, y2):
        """
        Returns a string representing a LaTeX command to draw the signal from (x1, y1) to (x2, y2).
        """
        return f'\draw[{self.__class__.__name__}] ({x1},{y1}) -- ({x2},{y2});'

    def draw(self, *args):
        """
        Public method that calls the private __draw method with the given arguments.
        """
        return self.__draw(*args)


class NeuralSignal(Signal):
    """
    The NeuralSignal class is a subclass of Signal. It represents a signal in a neural network diagram with additional attributes for direction, formula, and position.
    """

    def __init__(self, direction, formula, position):
        """
        Initialize a NeuralSignal object with the given direction, formula, and position. The direction must be either 'in' or 'out'.
        """
        super().__init__()
        if direction == 'in':
            self.direction_str = '{-latex}'
        elif direction == 'out':
            self.direction_str = '{latex-}'
        else:
            raise ValueError('direction must be in or out')
        self.formula = formula
        self.position = position

    def draw(self):
        """
        Returns a string representing a LaTeX command to draw the neural signal with the given direction, formula, and position.
        """
        return """
                pin={[pin edge=""" + self.direction_str + """, pin distance=\pindist]""" + self.position + """:""" + self.formula + """}
                """


if __name__ == '__main__':
    """
    If the module is run as a script, it creates a Signal object and a NeuralSignal object and prints their draw methods.
    """
    print(Signal().draw(0, 0, 1, 1))
    print(NeuralSignal('in', 'above: $x$', 'north').get_style())
