"""
!/usr/bin/env python
 -*- coding: utf-8 -*-
 @CreateTime    : 2024-05-10 5:44
 @Author  : Ivan Mao
 @File    : node.py
 @Description : 
"""
from abc import ABCMeta, abstractmethod


class Node(metaclass=ABCMeta):

    id_counter = 0

    @classmethod
    def generate_id(cls):
        cls.id_counter += 1
        return cls.id_counter

    @abstractmethod
    def get_style(self):
        pass

    @abstractmethod
    def draw(self, *args):
        pass
