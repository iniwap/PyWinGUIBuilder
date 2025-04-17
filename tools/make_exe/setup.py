from setuptools import setup
from Cython.Build import cythonize

setup(
    name="gui",
    ext_modules=cythonize(
        [
            "../../scripts/*.py",
            # "../../*.py", #不能编译入口文件，否则会找到不文件
        ],
        exclude=[
            "../../scripts/__init__.py",
            # "../../__init__.py",#不能编译入口文件，否则会找到不文件
        ],
        language_level=3,
    ),
)

# python setup.py build_ext --inplace
