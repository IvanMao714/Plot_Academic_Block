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

    def __init__(self, color='black', arrow_type='->', width='1.5pt', line_type='line', x1=0, y1=0, x2=1, y2=1):
        """
        Initialize a Signal object with the given color, arrow type, width, and line type. Defaults are provided for all parameters.
        """
        self.color = color
        self.arrow_type = arrow_type
        self.width = width
        self.line_type = line_type
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    id_counter = 0

    @classmethod
    def generate_id(cls):
        cls.id_counter += 1
        return cls.id_counter

    def get_style(self):
        """
        Returns a string representing the style of the signal in LaTeX format.
        """
        return self.__class__.__name__ + f"""/.style={{draw={self.color}, {self.arrow_type}, {self.line_type} width={self.width}}},"""

    def draw(self):
        """
        Public method that calls the private __draw method with the given arguments.
        """
        return f'\n\draw[{self.__class__.__name__}] ({self.x1},{self.y1}) -- ({self.x2},{self.y2});'
