"""
!/usr/bin/env python
 -*- coding: utf-8 -*-
 @CreateTime    : 2024-05-09 3:51
 @Author  : Ivan Mao
 @File    : line.py
 @Description : This module contains the Line class used for creating and drawing line in a diagram.
"""


class Line:
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
        return self.__class__.__name__ + f"""/.style={{draw={self.color}, {self.arrow_type}, {self.line_type} width={self.width}}},"""

    def __draw(self, x1, y1, x2, y2):
        """
        Returns a string representing a LaTeX command to draw the signal from (x1, y1) to (x2, y2).
        """
        return f'\n\draw[{self.__class__.__name__}] ({x1},{y1}) -- ({x2},{y2});'

    def draw(self, *args):
        """
        Public method that calls the private __draw method with the given arguments.
        """
        return self.__draw(*args)


