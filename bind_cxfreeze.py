#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""此程序用于三线式调温白菜白光的曲线分析和电阻网络阻值选取。
使用cxFreeze打包成EXE文件
请执行：python.exe bind_cxfreeze.py build 然后在build目录中生成exe文件
在生成exe文件后，可以删除tcl\8.4, tcl\8.5, tcl\8.6等目录以减小体积。
Author: cdhigh
"""

import sys
import os
from cx_Freeze import setup, Executable

pyScriptFile = 'CheapHakkoCurveAnalyser.py'

if sys.platform == "win32":
    base = "Win32GUI"
else:
    base = None

tclPath = os.path.normpath(os.path.join(os.path.dirname(os.__file__), '../tcl/tcl8.6'))

build_exe_options = {'optimize' : 2,
                     'include_files' : [(tclPath,'tcl'),],}

exe = Executable(
    script = pyScriptFile,
    initScript = None,
    base = 'Win32GUI',
    targetName = 'CheapHakkoCurveAnalyser.exe',
    compress = True,
    appendScriptToExe = True,
    appendScriptToLibrary = True,
)

setup( name = 'CheapHakkoCurveAnalyser', 
        version = '0.2',
        description = 'CheapHakkoCurveAnalyser',
        options = {'build_exe': build_exe_options},
        executables = [Executable(pyScriptFile, base = base,
            icon='gui/icon.ico', )])

