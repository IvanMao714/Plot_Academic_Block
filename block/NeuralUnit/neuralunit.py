"""
!/usr/bin/env python
 -*- coding: utf-8 -*-
 @CreateTime    : 2024-05-12 0:50
 @Author  : Ivan Mao
 @File    : neuralunit.py
 @Description : 
"""
from typing import List

from block.NeuralUnit.element.neural_line import NeuralLine
from block.NeuralUnit.element.neural_node import NeuralNode
from block.NeuralUnit.element.neural_tittle import NeuralTittle
from utils import generate_doc


class NeuralUnit:
    def __init__(self, neural_node, neural_line, neural_tittle):
        self.neural_node = neural_node
        self.neural_line = neural_line
        self.neural_tittle = neural_tittle

    def add_node(self, node):
        if type(self.neural_node) is List:
            self.neural_node.append(node)
        else:
            self.neural_node = [self.neural_node]
            self.neural_node.append(node)

    def add_line(self, line):
        if type(self.neural_line) is List:
            self.neural_line.append(line)
        else:
            self.neural_line = [self.neural_line]
            self.neural_line.append(line)

    def add_tittle(self, tittle):
        self.neural_tittle = tittle

    def get_style(self):
        # if (type(self.neural_line) and type(self.neural_node)) is List:
        #     return ''.join([node.get_style() for node in self.neural_node]) + ''.join(
        #         [line.get_style() for line in self.neural_line])
        if type(self.neural_line) is List:
            return self.neural_node.get_style() + '\n'.join([line.get_style() for line in self.neural_line]) + self.neural_tittle.get_style()
        # elif type(self.neural_node) is List:
        #     return ''.join([node.get_style() for node in self.neural_node]) + self.neural_line.get_style()
        return self.neural_node.get_style() + '\n' + self.neural_line.get_style() + self.neural_tittle.get_style()

    def draw(self):
        # if (type(self.neural_line) and type(self.neural_node)) is List:
        #     return ''.join([node.draw() for node in self.neural_node]) + ''.join(
        #         [line.draw() for line in self.neural_line])
        if type(self.neural_line) is List:
            for line in self.neural_line:
                self.neural_node.add_pin(line)
        else:
            self.neural_node.add_pin(self.neural_line)
        # elif type(self.neural_node) is List:
        #     return ''.join([node.draw() for node in self.neural_node]) + self.neural_line.draw()
        return self.neural_node.draw() + self.neural_tittle.draw()


if __name__ == '__main__':
    nu = NeuralUnit(NeuralNode(0, 0, 'A', 'x1'), NeuralLine('in', 'x_1', 'left', '35pt'), NeuralTittle('200pt', '40pt of A','centered', '2', 'x1'))
    # n = NeuralNode(0, 0, 'A', 'x1')
    # n.add_pin(NeuralLine('in', '->', 'left', '35pt'))
    # n.add_pin(NeuralLine('in', '->', 'right', '35pt'))
    generate_doc([nu])
