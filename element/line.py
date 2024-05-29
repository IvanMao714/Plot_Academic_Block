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
    A class used to represent a Line in a diagram.

    ...

    Attributes
    ----------
    color : str
        a formatted string to determine the color of the line (default is 'black')
    arrow_type : str
        a formatted string to determine the type of the arrow (default is '->')
    width : str
        a formatted string to determine the width of the line (default is '1.5pt')
    line_type : str
        a formatted string to determine the type of the line (default is 'line')
    x1, y1, x2, y2 : int
        integers representing the coordinates of the line (default is (0,0) to (1,1))

    Methods
    -------
    generate_id():
        Generates a unique id for each line by incrementing a class variable 'id_counter'.
    get_style():
        Returns a string representing the style of the line.
    draw():
        Returns a string that can be used to draw the line in a diagram.
    """

    def __init__(self, color='black', arrow_type='->', width='1.5pt', line_type='line', x1=0, y1=0, x2=1, y2=1):
        """
        Constructs all the necessary attributes for the Line object.

        Parameters
        ----------
            color : str
                a formatted string to determine the color of the line (default is 'black')
            arrow_type : str
                a formatted string to determine the type of the arrow (default is '->')
            width : str
                a formatted string to determine the width of the line (default is '1.5pt')
            line_type : str
                a formatted string to determine the type of the line (default is 'line')
            x1, y1, x2, y2 : int
                integers representing the coordinates of the line (default is (0,0) to (1,1))
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
        """
        Generates a unique id for each line by incrementing a class variable 'id_counter'.

        Returns
        -------
        int
            a unique id for the line
        """
        cls.id_counter += 1
        return cls.id_counter

    def get_style(self):
        """
        Returns a string representing the style of the line.

        Returns
        -------
        str
            a string representing the style of the line
        """
        return self.__class__.__name__ + f"""/.style={{draw={self.color}, {self.arrow_type}, {self.line_type} width={self.width}}},"""

    def draw(self):
        """
        Returns a string that can be used to draw the line in a diagram.

        Returns
        -------
        str
            a string that can be used to draw the line in a diagram
        """
        return f'\n\draw[{self.__class__.__name__}] ({self.x1},{self.y1}) -- ({self.x2},{self.y2});'
