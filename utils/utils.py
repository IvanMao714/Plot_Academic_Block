"""
!/usr/bin/env python
 -*- coding: utf-8 -*-
 @CreateTime    : 2024-05-08 15:54
 @Author  : Ivan Mao
 @File    : utils.py
 @Description : 
"""
import os

from element.line import Line


def iterate_letters_based_on_list_length(lst):
    for i in range(len(lst)):
        return chr(ord('A') + i % 26)


# This function loads the environment for the LaTeX document.
# It takes a string argument 'environment' which specifies the environment to be loaded.
# It returns a string which is a LaTeX command to load the specified environment.
def load_environment(environment):
    return r"""
\documentclass[tikz]{standalone}
\usepackage{lib/""" + environment + """}\n"""


# This function loads the style for the LaTeX document.
# It takes a list 'arch' of objects, each of which should have a 'get_style' method.
# It returns a string which is a LaTeX command to set the style of the document.
def load_style(arch):
    return_str = '\\tikzset{\n'
    for c in arch:
        if hasattr(c, 'get_style'):
            return_str += c.get_style() + '\n'
    return_str += '}'
    return return_str


# def calculate_height(number):
#     return (35 * number) / 2


# This function initializes the LaTeX document.
# It returns a string which is a LaTeX command to begin the document and the tikzpicture environment.
def init_doc():
    return f"""\n\\begin{{document}}\n\\begin{{tikzpicture}}[]"""


# This function ends the LaTeX document.
# It returns a string which is a LaTeX command to end the tikzpicture environment and the document.
def end_doc():
    return f"""\n\\end{{tikzpicture}}\n\\end{{document}}"""


# This function generates the LaTeX document.
# It takes a list 'arch' of objects, each of which should have a 'draw' method, and a string 'pathname' which is the path to the file where the document will be written.
# It writes the LaTeX commands to load the environment, set the style, begin the document, draw the objects in 'arch', and end the document to the file at 'pathname'.
def generate_doc(arch, pathname=os.path.join(os.path.join(os.path.dirname(__file__), os.pardir), 'output.tex')):
    with open(pathname, "w") as f:
        f.write(load_environment('basic'))
        f.write(load_style(arch))
        f.write(init_doc())
        for c in arch:
            f.write(c.draw())

        f.write(end_doc())


# If this script is run as the main program, it generates a LaTeX document with a single Signal object.
if __name__ == '__main__':
    generate_doc([Line()])
