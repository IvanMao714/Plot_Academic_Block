"""
!/usr/bin/env python
-*- coding: utf-8 -*-
@CreateTime    : 2024-05-25 03:32
@Author        : FengD
@File          : poolingmap
@Description   :
"""
from block.FeatureMap.element.grid_background import GridBackground
from block.FeatureMap.element.grid_feature import Features
from block.FeatureMap.element.grid_title import GridTitle
from block.FeatureMap.featuremap import FeatureMap
from element.line import Line
from element.rectangle import Rectangle
from utils import generate_doc


class PoolingMap:
    def __init__(self, nodes):
        self.nodes = nodes

    def generate(self):
        return self.nodes


if __name__ == '__main__':
    nodes = [
        FeatureMap(
            position=(0, 0),
            background=None,
            features=Features([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]),
            title=GridTitle(50, ''),
        ),
        FeatureMap(
            position=(5, 0),
            background=None,
            features=Features([1, 2, 3, 4], e_position=(2, -2)),
            title=GridTitle(50, 'PoolingMap'),
        ),

        FeatureMap(
            position=(10, 0),
            background= GridBackground([Rectangle((0, 0), (2, -2), 'red!25!white', (0, 0)),
                           Rectangle((2, 0), (4, -2), 'yellow!25!white', (0, 0)),
                           Rectangle((0, -2), (2, -4), 'blue!25!white', (0, 0)),
                           Rectangle((2, -2), (4, -4), 'green!25!white', (0, 0))]),
            features=Features([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], e_position=(4, -4)),
            title=GridTitle(50, ''),
        ),

        Line(
            x1=12.5, y1=0, x2=15, y2=0,
        ),

        FeatureMap(
            position=(17.5, 0),
            background= GridBackground([Rectangle((0, 0), (1, -1), 'red!25!white', (0, 0)),
                           Rectangle((1, 0), (2, -1), 'yellow!25!white', (0, 0)),
                           Rectangle((0, -1), (1, -2), 'blue!25!white', (0, 0)),
                           Rectangle((1, -1), (2, -2), 'green!25!white', (0, 0))]),
            features=Features([1, 2, 3, 4], e_position=(2, -2)),
            title=GridTitle(50, 'Max Pooling'),
        ),


    ]
    p = PoolingMap(nodes)
    generate_doc(p.generate())

