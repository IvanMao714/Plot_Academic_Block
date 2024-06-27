"""
!/usr/bin/env python
-*- coding: utf-8 -*-
@CreateTime    : 2024-05-25 01:23
@Author        : FengD
@File          : rectangle
@Description   :
"""
from utils import generate_doc


class Rectangle:
    def __init__(self, s_position=(0, 0), e_position=(5, -5), fill='black!25!white', shift=(0, 0)):
        self.s_position = s_position
        self.e_position = e_position
        self.fill = fill
        self.shift = shift

    def draw(self):
        return f"""\\draw[shift={{{self.shift}}}, fill={self.fill}] {self.s_position} rectangle {self.e_position};\n"""

    def get_style(self):
        return self.__class__.__name__ + f"""/.style={{fill={self.fill}}}"""


if __name__ == '__main__':
    r1 = Rectangle((0, 0), (1, -1), 'red!25!white', (0, 0))
    r2 = Rectangle((1, 0), (2, -1), 'yellow!25!white', (0, 0))
    r3 = Rectangle((0, -1), (1, -2), 'blue!25!white', (0, 0))
    r4 = Rectangle((1, -1), (2, -2), 'green!25!white', (0, 0))
    generate_doc([r1, r2, r3, r4])
