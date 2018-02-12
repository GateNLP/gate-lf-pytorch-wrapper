import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))


def read(fname):
    return open(os.path.join(here, fname)).read()


readme = read('README.md')

setup(
    name="gatelfpytorch",
    version="0.1",
    description="Library to build and use pytorch NN models for GATE Learning Framework",
    author="Johann Petrak",
    author_email="johann.petrak@gmail.com",
    # url="http://packages.python.org/an_example_pypi_project",
    license="Apache 2.0",
    # keywords="",
    packages=['gatelfpytorch'],
    long_description=readme,
    py_modules=['gatelfpytorch', 'torch', 'pkg_resources'],
    # scripts=['some.py'],
    # entry_points = {'console_scripts': ['some=some:main']},
    tests_require=['nose'],
    test_suite='nose.collector',
    classifiers=[],
)
