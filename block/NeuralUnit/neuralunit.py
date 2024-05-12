"""
!/usr/bin/env python
 -*- coding: utf-8 -*-
 @CreateTime    : 2024-05-12 0:50
 @Author  : Ivan Mao
 @File    : neuralunit.py
 @Description : 
"""
from typing import List


class NeuralUnit:
    def __init__(self, neural_node, neural_line):
        self.neural_node = neural_node
        self.neural_line = neural_line

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

    def get_style(self):
        if (type(self.neural_line) and type(self.neural_node)) is List:
            return ''.join([node.get_style() for node in self.neural_node]) + ''.join(
                [line.get_style() for line in self.neural_line])
        elif type(self.neural_line) is List:
            return self.neural_node.get_style() + ''.join([line.get_style() for line in self.neural_line])
        elif type(self.neural_node) is List:
            return ''.join([node.get_style() for node in self.neural_node]) + self.neural_line.get_style()
        return self.neural_node.get_style() + self.neural_line.get_style()

    def draw(self):
        if (type(self.neural_line) and type(self.neural_node)) is List:
            return ''.join([node.draw() for node in self.neural_node]) + ''.join(
                [line.draw() for line in self.neural_line])
        elif type(self.neural_line) is List:
            return self.neural_node.draw() + ''.join([line.draw() for line in self.neural_line])
        elif type(self.neural_node) is List:
            return ''.join([node.draw() for node in self.neural_node]) + self.neural_line.draw()
        return self.neural_node.draw() + self.neural_line.draw()
