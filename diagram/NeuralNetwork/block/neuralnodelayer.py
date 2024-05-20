"""
!/usr/bin/env python
 -*- coding: utf-8 -*-
 @CreateTime    : 2024-05-13 22:32
 @Author  : Ivan Mao
 @File    : neuralnetwork.py
 @Description : This file contains the NeuralNodeLayer class which is used to represent a layer of nodes in a neural network diagram.
"""


class NeuralNodeLayer:
    """
    The NeuralNodeLayer class represents a layer of nodes in a neural network diagram.
    Each instance of this class represents a layer of nodes, with each node having a specific type and number.
    """

    def __init__(self, node_type, node_number, horizon=None, front_layer=None):
        """
        Initializes a new instance of the NeuralNodeLayer class.

        :param node_type: The type of nodes in this layer.
        :param node_number: The number of nodes in this layer.
        :param horizon: The horizon of this layer. Default is None.
        :param front_layer: The layer in front of this layer. Default is None.
        """
        self.node_type = node_type
        self.node_number = node_number
        self.front_layer = front_layer
        self.horizon = horizon
        if self.front_layer is None:
            self.distance = 0
        else:
            self.distance = self.front_layer.distance + 80

    def get_style(self):
        """
        Returns the style of the nodes in this layer as a string.

        :return: A string representing the style of the nodes in this layer.
        """
        return self.node_type.get_style()

    def calculate_height(self):
        """
        Calculates and returns the height of this layer.

        :return: The height of this layer.
        :raises ValueError: If the horizon is None.
        """
        if self.horizon is not None:
            if self.node_number % 2 != 0:
                return (self.node_number // 2) * 35 + self.horizon
            else:
                return (self.node_number // 2) * 35 + self.horizon - 17.5
        else:
            raise ValueError('The horizon is None that is not allowed.')

    def draw(self):
        """
        Returns a string that represents the nodes in this layer in a format that can be used to draw them.

        :return: A string that represents the nodes in this layer in a format that can be used to draw them.
        """
        if self.front_layer is None:
            return_str = f'\n\t\\foreach \y in {{1,...,{self.node_number}}}\n\t\t'
            return_str += self.node_type.draw()
            if self.horizon is None:
                return_str += f'({self.node_type.name}\y) at (0,-\\y*35pt) {{${self.node_type.formula}_\y$}};'
            else:
                return_str += f'({self.node_type.name}\y) at (0,{self.calculate_height()}pt-\\y*35pt) {{${self.node_type.formula}_\y$}};'
        else:
            return_str = f'\n\t\\foreach \y in {{1,...,{self.node_number}}}\n\t\t'
            return_str += self.node_type.draw()
            if self.horizon is None:
                return_str += f'({self.node_type.name}\y) at ({self.distance}pt,-\\y*35pt) {{${self.node_type.formula}_\y$}};'
            else:
                return_str += f'({self.node_type.name}\y) at ({self.distance}pt,{self.calculate_height()}pt-\\y*35pt) {{${self.node_type.formula}_\y$}};'

        return return_str
