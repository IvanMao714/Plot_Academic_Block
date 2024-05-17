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


class NeuralNetworkNode(Node):

    def __init__(self, name, color, fill_color, opacity, formula='', pin=None):
        if pin is None:
            pin = []
        self.name = name
        self.pin = pin
        self.color = color
        self.fill_color = fill_color
        self.opacity = opacity
        self.formula = formula

    def get_style(self):
        return self.name + f"""/.style={{draw={self.color}, fill={self.fill_color}!{self.opacity}, circle, inner 
        sep=0pt, text width=22pt, align=center, line width=1.0pt}},"""

    def add_pin(self, pin):
        self.pin.append(pin.draw())

    def draw(self):
        return_str = f'\\node[{self.name},'
        for p in self.pin:
            return_str += p
        return_str += f'] '

        return return_str


if __name__ == '__main__':
    n = NeuralNetworkNode('neuron', 'black', 'white', 0.0, 'ReLU')
    generate_doc([n])
