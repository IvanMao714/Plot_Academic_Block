"""
!/usr/bin/env python
-*- coding: utf-8 -*-
@CreateTime    : 2024-05-20 22:43
@Author        : FengD
@File          : grid.py
@Description   :
"""
from utils import generate_doc


class Grid:
    # s_position: start position, e_position: end position, step: grid step, ultra: grid ultra, literal_color: literal color, grid_color: grid color, bg_color: background color, shift: grid position
    def __init__(self, s_position=(0, 0), e_position=(5, -5), step=1, ultra='thick', literal_color='black',
                 grid_color='black',
                 bg_color='black!25!white', shift=(0, 0)):
        self.s_position = s_position
        self.e_position = e_position
        self.grid_step = step
        self.grid_ultra = ultra
        self.grid_color = grid_color
        self.literal_color = literal_color
        self.bg_color = bg_color
        self.shift = shift

    def draw(self):
        draw = f"""\\draw[step={self.grid_step}, ultra {self.grid_ultra}, color={self.literal_color}, fill={self.bg_color}, draw={self.grid_color}, shift={{self.shift}}] {self.s_position} grid {self.e_position}"""
        return draw

    def get_style(self):
        return self.__class__.__name__ + f"""/.style={{step={self.grid_step}, ultra {self.grid_ultra}, literal_color={self.literal_color}, bg_color={self.bg_color}, grid_color={self.grid_color}, size={self.e_position}}}"""


if __name__ == '__main__':
    g = Grid((0, 0), (5, -5), 1, 'thick', 'black', 'black', 'black!25!white', (0, 0))
    generate_doc([g])
