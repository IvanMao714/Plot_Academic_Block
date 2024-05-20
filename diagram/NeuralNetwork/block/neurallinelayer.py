"""
!/usr/bin/env python
 -*- coding: utf-8 -*-
 @CreateTime    : 2024-05-16 17:02
 @Author  : Ivan Mao
 @File    : neurallinelayer.py
 @Description : This file contains the NeuralLineLayer class which is used to represent a layer of connections (lines) in a neural network diagram.
"""

from block.NeuralUnit.element.neural_line import NeuralLine
from diagram.NeuralNetwork.block.neuralnodelayer import NeuralNodeLayer
from diagram.NeuralNetwork.element.neural_node import NeuralNetworkNode
from utils import generate_doc


class NeuralLineLayer:
    """
    The NeuralLineLayer class represents a layer of connections (lines) in a neural network diagram.
    Each instance of this class connects a 'front' layer of nodes to a 'behind' layer of nodes.
    """

    def __init__(self, front_layer, behind_layer):
        """
        Initializes a new instance of the NeuralLineLayer class.

        :param front_layer: The layer of nodes that the lines in this layer will start from.
        :param behind_layer: The layer of nodes that the lines in this layer will end at.
        """
        self.front_layer = front_layer
        self.behind_layer = behind_layer

    def get_style(self):
        """
        Returns the style of the lines in this layer as a string.

        :return: A string representing the style of the lines in this layer.
        """
        return self.__class__.__name__ + f"""/.style={{arrows={{latex-}},draw=black,line width=1.5pt,rounded corners=4pt}},"""

    def draw(self):
        """
        Returns a string that represents the lines in this layer in a format that can be used to draw them.

        :return: A string that represents the lines in this layer in a format that can be used to draw them.
        """
        return f'\\foreach \\dest in {{1,...,{self.behind_layer.node_number}}}\n' \
               f'        \\foreach \\source in {{1,...,{self.front_layer.node_number}}}\n' \
               f'            \\draw[{self.__class__.__name__}] ({self.behind_layer.node_type.name}\\dest) edge ({self.front_layer.node_type.name}\\source);\n'


if __name__ == '__main__':
    # Create a layer of input nodes
    n_1 = NeuralNodeLayer(NeuralNetworkNode('I', 'green', 'black', 20, '3'), 3, 'Input', 0, None)
    # Create a layer of output nodes
    n_2 = NeuralNodeLayer(NeuralNetworkNode('O', 'green', 'black', 20, '3'), 2, 'Output', 0, n_1)
    # Create a layer of lines that connect the input nodes to the output nodes
    l_1 = NeuralLineLayer(NeuralLine('in', '->', '1.5pt', 'line'), n_1, n_2)
    # Generate a document that represents the neural network
    generate_doc([n_1, n_2, l_1])
