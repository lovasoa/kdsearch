#!/usr/bin/env python3
"""Search k-dimensional datasets efficiently using KDTrees 
"""

from . import kdtree
from . import statistics

KDTree = kdtree.KDTree
Statistics = statistics.Statistics

__all__ = [
    'KDTree',
    'Statistics'
]

def load_tests(loader, tests, ignore):
    import unittest
    import doctest
    for module in (kdtree, statistics):
        tests.addTests(doctest.DocTestSuite(module))
    return tests
