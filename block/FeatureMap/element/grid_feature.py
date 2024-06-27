"""
!/usr/bin/env python
-*- coding: utf-8 -*-
@CreateTime    : 2024-05-20 23:44
@Author        : FengD
@File          : feature_grid
@Description   :
"""

from element.grid import Grid
from utils import generate_doc


class Features(Grid):
    def __init__(self, features, size='Large', e_position=(5, -5)):
        super().__init__(e_position=e_position)
        self.fpr = self.e_position[0]
        self.features = features
        self.size = size

    def draw(self):
        return super().draw() + f"""foreach[count=~] \l in {{{", ".join(map(str, self.features))}}} {{({{0.5+mod(~-1,{self.fpr}}}, {{-0.5-div(~-1,{self.fpr}}}) node {{\{self.size} \l}}}};"""


if __name__ == '__main__':
    f = Features([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])
    generate_doc([f])


