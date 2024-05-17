"""
!/usr/bin/env python
 -*- coding: utf-8 -*-
 @CreateTime    : 2024-05-13 22:32
 @Author  : Ivan Mao
 @File    : neuralnetwork.py
 @Description : 
"""
from diagram.NeuralNetwork.element.neural_node import NeuralNetworkNode
from utils import generate_doc


class NeuralNodeLayer:
    def __init__(self, node_type, node_number, horizon=None, front_layer=None):
        self.node_type = node_type
        self.node_number = node_number
        self.front_layer = front_layer
        # self.tittle = tittle
        self.horizon = horizon
        # self.height = calculate_height(self.node_number)
        if self.front_layer is None:
            self.distance = 0
        else:
            self.distance = self.front_layer.distance + 80

    def get_style(self):
        return self.node_type.get_style()

    # def get_height(self):
    #     return self.height
    def calculate_height(self):
        if self.horizon is not None:
            if self.node_number % 2 != 0:
                return (self.node_number//2) * 35 + self.horizon
            else:
                return (self.node_number//2) * 35 + self.horizon - 17.5
        else:
            raise ValueError('The horizon is None that is not allowed.')
    def draw(self):
        if self.front_layer is None:
            return_str = f'\n\t\\foreach \y in {{1,...,{self.node_number}}}\n\t\t'
            return_str += self.node_type.draw()
            if self.horizon is None:
                return_str += f'({self.node_type.name}\y) at (0,-\\y*35pt) {{${self.node_type.formula}_\y$}};'
            else:
                return_str += f'({self.node_type.name}\y) at (0,{self.calculate_height()}pt-\\y*35pt) {{${self.node_type.formula}_\y$}};'
            # return_str += f'\n\t\\node[above of={self.node_type.name}1] {{${self.tittle}$}};'
        else:
            return_str = f'\n\t\\foreach \y in {{1,...,{self.node_number}}}\n\t\t'
            return_str += self.node_type.draw()
            if self.horizon is None:
                return_str += f'({self.node_type.name}\y) at ({self.distance}pt,-\\y*35pt) {{${self.node_type.formula}_\y$}};'
            else:
                return_str += f'({self.node_type.name}\y) at ({self.distance}pt,{self.calculate_height()}pt-\\y*35pt) {{${self.node_type.formula}_\y$}};'
            # return_str += f'\n\t\\node[above of={self.node_type.name}1] {{${self.tittle}$}};'

        return return_str

