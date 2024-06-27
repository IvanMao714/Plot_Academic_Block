"""
!/usr/bin/env python
-*- coding: utf-8 -*-
@CreateTime    : 2024-05-25 02:29
@Author        : FengD
@File          : grid_background
@Description   :
"""
from element.rectangle import Rectangle
from utils import generate_doc


class GridBackground(Rectangle):
    def __init__(self, recs):
        super().__init__()
        self.recs = recs

    def draw(self):
        r_draw = []
        for rec in self.recs:
            if isinstance(rec, Rectangle):
                r_draw.append(rec.draw())
            else:
                return "Error: rec is not Rectangle"
        return ''.join(r_draw)

    def get_style(self):
        return super().get_style()


if __name__ == '__main__':
    rec1 = GridBackground([Rectangle((0, 0), (1, -1), 'red!25!white', (0, 0)),
                           Rectangle((1, 0), (2, -1), 'yellow!25!white', (0, 0)),
                           Rectangle((0, -1), (1, -2), 'blue!25!white', (0, 0)),
                           Rectangle((1, -1), (2, -2), 'green!25!white', (0, 0))])
    generate_doc([rec1])
