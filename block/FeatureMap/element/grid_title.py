"""
!/usr/bin/env python
-*- coding: utf-8 -*-
@CreateTime    : 2024-05-21 01:04
@Author        : FengD
@File          : grid_title
@Description   :
"""

from element.tittle import Tittle


class GridTitle(Tittle):
    def __init__(self, text_width, text_position, text_align='center', name='', formula='', yshift = 0, xshift = 0):
        super().__init__(text_width, text_position, text_align, name, formula)
        self.yshift = yshift
        self.xshift = xshift

    def get_style(self):
        return super().get_style() + f"yshift = {self.yshift}, xshift={self.xshift}, right of = {self.text_position}"

    def draw(self):
        return f'\n\t\\node[{self.__class__.__name__},align={self.text_align}, text width={self.text_width}pt, yshift = {self.yshift}pt, xshift={self.xshift}, right of={self.text_position}] ({self.name}) {{{self.formula}}};'
