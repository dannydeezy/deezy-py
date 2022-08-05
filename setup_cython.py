# -*- coding: utf-8 -*-
# @Author: lnorb.com
# @Date:   2022-08-05 12:52:10
# @Last Modified by:   lnorb.com
# @Last Modified time: 2022-08-05 13:15:34

from setuptools import setup, Extension
from setuptools import setup
from Cython.Build import cythonize
from pathlib import Path

mods = [x for x in Path(".").glob("deezy/*.py")]

for m in mods:
    cythonize(m.as_posix())

setup(
    ext_modules=[
        Extension(f"deezy.{x.stem}", [x.with_suffix(".c").as_posix()]) for x in mods
    ]
)
