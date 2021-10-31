# -*- coding: utf-8 -*-

import py2exe
from distutils.core import setup
from encodings import mbcs

import sys
import os
import imp

import sys
if hasattr(sys,"setdefaultencoding"):
    sys.setdefaultencoding("utf-8")

def main_is_frozen():
    return (hasattr(sys, "frozen") or # new py2exe
            hasattr(sys, "importers") # old py2exe
            or imp.is_frozen("__main__")) # tools/freeze

def get_main_dir():
    if main_is_frozen():
        return os.path.abspath(os.path.dirname(sys.executable))
    return os.path.abspath(os.path.dirname(sys.argv[0]))

py2exe_options = {
    "compressed": 1,
    "optimize": 2,
    "bundle_files": 1,
    "packages": ["encodings"],
    "dll_excludes": ["w9xpopen.exe"],
    "includes" : ["sip","res_rc"]
}

dll_excludes=['w9xpopen.exe']

setup(
    options={"py2exe" : py2exe_options},
    windows=[{"script" : "C21counter.py", "icon_resources": [(1, "mid.ico")]}],
    zipfile="Python.dll",
)