"""
!/usr/bin/env python
 -*- coding: utf-8 -*-
 @CreateTime    : 2024-05-12 0:50
 @Author  : Ivan Mao
 @File    : neuralunit.py
 @Description : This module defines the NeuralUnit class which represents a unit in a neural network.
                It consists of nodes, lines and titles.
"""

from block.NeuralUnit.element.neural_line import NeuralLine
from block.NeuralUnit.element.neural_node import NeuralNode
from block.NeuralUnit.element.neural_tittle import NeuralTittle
from utils import generate_doc


class NeuralUnit:
    """
    The NeuralUnit class represents a unit in a neural network.
    It consists of nodes, lines and titles.
    """

    def __init__(self, neural_node, neural_line, neural_tittle):
        """
        Initializes a NeuralUnit with a node, line and title.
        """
        self.neural_node = neural_node
        self.neural_line = neural_line
        self.neural_tittle = neural_tittle

    def add_node(self, node):
        """
        Adds a node to the NeuralUnit. If the current node is not a list, it converts it to a list before adding.
        """
        if type(self.neural_node) is list:
            self.neural_node.append(node)
        else:
            self.neural_node = [self.neural_node]
            self.neural_node.append(node)

    def add_line(self, line):
        """
        Adds a line to the NeuralUnit. If the current line is not a list, it converts it to a list before adding.
        """
        if type(line) is list:
            for l in line:
                self.neural_line.append(l)
        else:
            self.neural_line.append(line)

    def add_tittle(self, tittle):
        """
        Sets the title of the NeuralUnit.
        """
        self.neural_tittle = tittle

    def get_style(self):
        """
        Returns the style of the NeuralUnit as a string. The style is a combination of the styles of the node, line and title.
        """

        if type(self.neural_line) is list:
            return_str = self.neural_node.get_style() + '\n'
            for line in self.neural_line:
                return_str += line.get_style() + '\n'
            return return_str + self.neural_tittle.get_style()
        return self.neural_node.get_style() + '\n' + self.neural_line.get_style() + self.neural_tittle.get_style()

    def draw(self):
        """
        Draws the NeuralUnit by adding pins to the node and returning the drawn node and title.
        """
        if type(self.neural_line) is list:
            for line in self.neural_line:
                self.neural_node.add_pin(line)
        else:
            self.neural_node.add_pin(self.neural_line)
        return self.neural_node.draw() + self.neural_tittle.draw()


if __name__ == '__main__':
    """
    Creates a NeuralUnit and generates a document with it.
    """
    line_list = [NeuralLine('in', '\\frac{\partial L}{\partial y_1}', 'left', '35pt'),
                 NeuralLine('out', '\\frac{\partial L}{\partial x_1}=\\frac{\partial L}{\partial y_1}\\frac{\partial y_1}{\partial x_1}','above right', '35pt'),
                 NeuralLine('out', '\\frac{\partial L}{\partial x_2}=\\frac{\partial L}{\partial y_1}\\frac{\partial y_1}{\partial x_2}', 'below right', '35pt')]
    nu = NeuralUnit(NeuralNode(0, 0, 'A', '\diff f'), line_list,
                    NeuralTittle('200pt', '4pt of A', 'centered', '2', 'Node Unit'))
    generate_doc([nu])
