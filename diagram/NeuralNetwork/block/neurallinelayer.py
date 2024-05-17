"""
!/usr/bin/env python
 -*- coding: utf-8 -*-
 @CreateTime    : 2024-05-16 17:02
 @Author  : Ivan Mao
 @File    : neurallinelayer.py
 @Description : 
"""
from block.NeuralUnit.element.neural_line import NeuralLine
from diagram.NeuralNetwork.block.neuralnodelayer import NeuralNodeLayer
from diagram.NeuralNetwork.element.neural_node import NeuralNetworkNode
from utils import generate_doc


class NeuralLineLayer:
    def __init__(self, front_layer, behind_layer):
        self.front_layer = front_layer
        self.behind_layer = behind_layer

    def get_style(self):
        return self.__class__.__name__ + f"""/.style={{arrows={{-latex}},draw=black,line width=1.5pt,rounded corners=4pt}},"""

    def draw(self):
        return f'\\foreach \\dest in {{1,...,{self.behind_layer.node_number}}}\n' \
               f'        \\foreach \\source in {{1,...,{self.front_layer.node_number}}}\n' \
               f'            \\draw[{self.__class__.__name__}] ({self.behind_layer.node_type.name}\\dest) edge ({self.front_layer.node_type.name}\\source);\n'


if __name__ == '__main__':
    n_1 = NeuralNodeLayer(NeuralNetworkNode('I', 'green', 'black', 20, '3'), 3, 'Input', 0, None)
    n_2 = NeuralNodeLayer(NeuralNetworkNode('O', 'green', 'black', 20, '3'), 2, 'Output', 0, n_1)
    l_1 = NeuralLineLayer(NeuralLine('in', '->', '1.5pt', 'line'), n_1, n_2)
    generate_doc([n_1, n_2, l_1])