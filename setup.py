#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
将 *.pyx 通过cython编译为 *.pyd
在同一个目录下执行命令即可：
python.exe setup.py build_ext --inplace
"""

from distutils.core import setup
from Cython.Build import cythonize

setup(
    name = 'bestchoices_n_v2t',
    ext_modules = cythonize("*.pyx")
)
