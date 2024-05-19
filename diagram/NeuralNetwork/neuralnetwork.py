"""
!/usr/bin/env python
 -*- coding: utf-8 -*-
 @CreateTime    : 2024-05-16 22:03
 @Author  : Ivan Mao
 @File    : neuralnetwork.py
 @Description : 
"""

from diagram.NeuralNetwork.block.neurallinelayer import NeuralLineLayer
from diagram.NeuralNetwork.block.neuralnodelayer import NeuralNodeLayer
from diagram.NeuralNetwork.element.neural_node import NeuralNetworkNode
from diagram.NeuralNetwork.element.neural_tittle import NeuralNetworkTittle
from utils import generate_doc


# from utils import generate_doc
#
#
class NeuralNetwork:
    def __init__(self, nodes, horizon=None):
        self.nodes = nodes
        self.horizon = horizon

    def generate(self):
        node_list = [NeuralNodeLayer(self.nodes[0]['node_type'], self.nodes[0]['number'], self.horizon, None)]
        for node in self.nodes[1:]:
            node_list.append(NeuralNodeLayer(node['node_type'], node['number'], self.horizon, node_list[-1]))
            node_list.append(NeuralLineLayer(node_list[-1], node_list[-2]))
        for node in self.nodes:
            node_list.append(NeuralNetworkTittle(node['text_position'], node['text_content']))
        # node_list.append(NeuralNetworkTittle(self.nodes[0]['text_position'], self.nodes[0]['text_content']))
        return node_list


if __name__ == '__main__':
    nodes = [
        {'node_type': NeuralNetworkNode('I', 'black', 'green', 20, 'x'), 'number': 3,
         'text_content': 'Input', 'text_position': ["I1", "H1"]},
        {'node_type': NeuralNetworkNode('H', 'black', 'green', 20, 'y'), 'number': 4,
         'text_content': 'Hidden', 'text_position': ["H1", "H1"]},
    ]
    n = NeuralNetwork(nodes)
    generate_doc(n.generate())
