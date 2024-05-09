"""
!/usr/bin/env python
 -*- coding: utf-8 -*-
 @CreateTime    : 2024-05-08 15:54
 @Author  : Ivan Mao
 @File    : utils.py
 @Description : 
"""
import os

from element.signal import Signal


def load_environment(environment):
    return r""" 
\documentclass[tikz]{standalone}
\usepackage{lib/""" + environment + """}\n"""


def load_style(arch):
    return_str = '\\tikzset{\n'
    for c in arch:
        return_str += c.get_style() + '\n'
    return_str += '}'
    return return_str


def init_doc():
    return r"""
    \begin{document}
    \begin{tikzpicture}[]"""


def end_doc():
    return r"""
    \end{tikzpicture}
    \end{document}"""


def generate_doc(arch, pathname="../file.tex"):
    with open(pathname, "w") as f:
        f.write(load_environment('basic'))
        f.write(load_style(arch))
        f.write(init_doc())
        for c in arch:
            print(c)
            f.write(c.draw(0, 0, 1, 1))

        f.write(end_doc())


if __name__ == '__main__':
    generate_doc([Signal()])
