"""
!/usr/bin/env python
 -*- coding: utf-8 -*-
 @CreateTime    : 2024-05-10 6:15
 @Author  : Ivan Mao
 @File    : neural_node.py
 @Description : 
"""
from element.node import Node
from utils import generate_doc


class NeuralNode(Node):
    """
    The NeuralNode class represents a node in a neural network diagram. It has attributes for color, shape, size, and position.
    """

    def __init__(self, board_color='black', shape='circle', fill_color='green', opacity='20', node_size='38pt', pin=[]):
        self.color = board_color
        self.shape = shape
        self.fill_color = fill_color
        self.opacity = opacity
        self.node_size = node_size

        self.pin = pin

    def get_style(self):
        """
        Returns a string representing the style of the node in LaTeX format.
        """
        return self.__class__.__name__ + f"""/.style={{draw={self.color}, {self.shape}, fill={self.fill_color}!{self.opacity}, text centered}},"""

    def add_pin(self, pin):
        self.pin.append(pin)

    def draw(self, x, y, label, formula='$f(x)$'):
        return_str = f'\\node[{self.__class__.__name__}, text width={self.node_size}, minimum size={self.node_size},'
        for p in self.pin:
            return_str += p
        return_str += f'] ({label}) at ({x},{y}) {{{formula}}};'

        return return_str

if __name__ == '__main__':
    n = NeuralNode()
    generate_doc([n], '../../../neural_node.tex')

