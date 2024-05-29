"""
!/usr/bin/env python
 -*- coding: utf-8 -*-
 @CreateTime    : 2024-05-10 5:44
 @Author  : Ivan Mao
 @File    : node.py
 @Description : This module contains the Node class which serves as an abstract base class for other classes in the project.
"""

from abc import ABCMeta, abstractmethod


class Node(metaclass=ABCMeta):
    """
    An abstract base class that other classes can inherit from.

    ...

    Attributes
    ----------
    id_counter : int
        a class variable that is used to generate unique ids for instances of classes that inherit from Node

    Methods
    -------
    generate_id():
        Increments the class variable 'id_counter' and returns its value. This method is used to generate unique ids for instances of classes that inherit from Node.
    get_style():
        An abstract method that must be implemented by any class that inherits from Node. It should return a string representing the style of the instance.
    draw(*args):
        An abstract method that must be implemented by any class that inherits from Node. It should return a string that can be used to draw the instance.
    """

    id_counter = 0

    @classmethod
    def generate_id(cls):
        """
        Increments the class variable 'id_counter' and returns its value.

        This method is used to generate unique ids for instances of classes that inherit from Node.

        Returns
        -------
        int
            the new value of 'id_counter'
        """
        cls.id_counter += 1
        return cls.id_counter

    @abstractmethod
    def get_style(self):
        """
        An abstract method that must be implemented by any class that inherits from Node.

        It should return a string representing the style of the instance.

        Raises
        ------
        NotImplementedError
            If the method is not implemented by the class that inherits from Node.
        """
        pass

    @abstractmethod
    def draw(self, *args):
        """
        An abstract method that must be implemented by any class that inherits from Node.

        It should return a string that can be used to draw the instance.

        Parameters
        ----------
        *args
            Variable length argument list.

        Raises
        ------
        NotImplementedError
            If the method is not implemented by the class that inherits from Node.
        """
        pass
