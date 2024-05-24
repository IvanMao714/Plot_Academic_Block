"""
!/usr/bin/env python
-*- coding: utf-8 -*-
@CreateTime    : 2024-05-21 00:29
@Author        : FengD
@File          : featuremap
@Description   :
"""

from block.FeatureMap.element.grid_feature import Features
from block.FeatureMap.element.grid_title import GridTitle
from block.FeatureMap.element.grid_background import GridBackground
from element.rectangle import Rectangle
from utils import generate_doc


class FeatureMap:
    def __init__(self, features, title, background):
        self.features = features
        self.title = title
        self.background = background

    def add_grid(self, grid):
        self.features = grid

    def draw(self):
        return self.background.draw() + self.features.draw() + self.title.draw()

    def get_style(self):
        return self.features.get_style() + self.features.size


if __name__ == '__main__':
    f = FeatureMap(
        Features([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]),
        GridTitle(50, (0, 0), 'centered', 'FeatureMap', 'FeatureMap', 10, 40),
        GridBackground([Rectangle((0, 0), (3, -3), 'red!25!white', (0, 0)),
                        Rectangle((2, 0), (5, -3), 'yellow!25!white', (0, 0)),
                        Rectangle((0, -2), (3, -5), 'blue!25!white', (0, 0)),
                        Rectangle((2, -2), (5, -5), 'green!25!white', (0, 0))]))
    generate_doc([f])
