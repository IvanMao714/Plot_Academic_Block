"""
!/usr/bin/env python
 -*- coding: utf-8 -*-
 @CreateTime    : 2024-05-10 6:15
 @Author  : Ivan Mao
 @File    : neural_node.py
 @Description : 
"""
from block.NeuralUnit.element.neural_line import NeuralLine
from element.node import Node
from utils import generate_doc


class NeuralNode(Node):
    """
    The NeuralNode class represents a node in a neural network diagram. It has attributes for color, shape, size, and position.
    """

    def __init__(self, x, y, label, formula, board_color='black', shape='circle', fill_color='green', opacity='20',
                 node_size='38pt', pin=[]):
        self.color = board_color
        self.shape = shape
        self.fill_color = fill_color
        self.opacity = opacity
        self.node_size = node_size
        self.x = x
        self.y = y
        self.label = label
        self.formula = formula

        self.pin = pin

    def get_style(self):
        """
        Returns a string representing the style of the node in LaTeX format.
        """
        return self.label + f"""/.style={{draw={self.color}, {self.shape}, fill={self.fill_color}!{self.opacity}, text centered}},"""

    def add_pin(self, pin):
        self.pin.append(pin.draw())

    def draw(self):
        return_str = f'\\node[{self.label}, text width={self.node_size}, minimum size={self.node_size},'
        for p in self.pin:
            return_str += p
        return_str += f'] ({self.label}) at ({self.x},{self.y}) {{${self.formula}$}};'

        return return_str


if __name__ == '__main__':
    n = NeuralNode(0, 0, 'A', 'x1')
    n.add_pin(NeuralLine('in', '->', 'left', '35pt'))
    n.add_pin(NeuralLine('in', '->', 'right', '35pt'))
    generate_doc([n])
