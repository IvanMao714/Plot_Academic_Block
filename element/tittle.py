"""
!/usr/bin/env python
 -*- coding: utf-8 -*-
 @CreateTime    : 2024-05-12 0:53
 @Author  : Ivan Mao
 @File    : tittle.py
 @Description : This module contains the Tittle class which inherits from the Node class and represents a title in a diagram.
"""

from abc import ABC
from element.node import Node


class Tittle(Node):
    """
    A class used to represent a Tittle in a diagram.

    ...

    Attributes
    ----------
    text_width : str
        a formatted string to determine the width of the text (default is '')
    text_position : str
        a formatted string to determine the position of the text (default is '')
    text_align : str
        a formatted string to determine the alignment of the text (default is 'centered')
    name : str
        a formatted string to determine the name of the tittle (default is '')
    formula : str
        a formatted string to determine the formula of the tittle (default is '')

    Methods
    -------
    get_style():
        Returns a string representing the style of the tittle.
    draw():
        Returns a string that can be used to draw the tittle in a diagram.
    """

    def __init__(self, text_width, text_position, text_align='centered', name='', formula=''):
        """
        Constructs all the necessary attributes for the Tittle object.

        Parameters
        ----------
            text_width : str
                a formatted string to determine the width of the text (default is '')
            text_position : str
                a formatted string to determine the position of the text (default is '')
            text_align : str
                a formatted string to determine the alignment of the text (default is 'centered')
            name : str
                a formatted string to determine the name of the tittle (default is '')
            formula : str
                a formatted string to determine the formula of the tittle (default is '')
        """
        self.text_width = text_width
        self.text_position = text_position
        self.text_align = text_align
        self.name = self.generate_id() if name == '' else name
        self.formula = formula

    def get_style(self):
        """
        Returns a string representing the style of the tittle.

        Returns
        -------
        str
            a string representing the style of the tittle
        """
        return self.__class__.__name__ + f"""/.style={{text width={self.text_width}, text {self.text_align}}},"""

    def draw(self):
        """
        Returns a string that can be used to draw the tittle in a diagram.

        Returns
        -------
        str
            a string that can be used to draw the tittle in a diagram
        """
        return f'\n\t\\node[{self.__class__.__name__}, text width={self.text_width}, above of={self.text_position}] ({self.name}) {{{self.formula}}};'
