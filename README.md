# KDSearch

Efficient K-dimensional queries in python using KDTrees with pandas and numpy.

[![Build Status](https://travis-ci.org/lovasoa/kdsearch.svg?branch=master)](https://travis-ci.org/lovasoa/kdsearch)

## Requirements

 - python 3.5+
 - numpy
 - pandas

## Installation

To install this package for the current user:

```
pip3 install --user kdsearch
```

## example
```python
import pandas
from kdsearch import KDTree

# We create a dataset with three points (1,3), (2,3) and (3,4)
df = pandas.DataFrame({"x": [1,2,3], "y":[3,3,4], "target": [0,1,1]})
tree = KDTree(df, ('x','y'), 'target')
# <KDTree of dimension 2>

# Query all points with x between 0 and 10 and y between 0 and 3 (inclusive)

tree.query({"x":[0,10], "y":[0,3]})
# Statistics(sum=1, length=2)

tree.query({"x":[0,10], "y":[0,10]})
# Statistics(sum=2, length=3)

tree.query({"x":[5,10], "y":[5,10]})
# Statistics(sum=0, length=0)
```
