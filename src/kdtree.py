#!/usr/bin/env python3

import numpy as np

class Statistics:
    """Represents a set of floats, allowing to retrieve its mean, without storing
    all the individual floats
    """

    def __init__(self, sum:float = 0, length:int = 0):
        """
        >>> Statistics()
        Statistics(sum=0, length=0)
        >>> Statistics(sum=3, length=5)
        Statistics(sum=3, length=5)
        """
        self.sum = sum
        self.length = length

    def merge(self, other: 'Statistics'):
        """Merge another Statistics objects into this one


        >>> stats = Statistics(sum=1, length=1)
        >>> stats.merge(Statistics(sum=1, length=2))
        >>> stats
        Statistics(sum=2, length=3)
        """
        self.sum += other.sum
        self.length += other.length

    def mean(self) -> float:
        """Return the mean of the elements represented or 0 if there are no elements.

        >>> Statistics(sum=1, length=2).mean()
        0.5
        >>> Statistics(sum=0, length=0).mean()
        0
        """
        return self.sum / self.length if self.length else 0

    def __len__(self):
        return self.length
    def __repr__(self):
        return "Statistics(sum=%g, length=%d)" % (self.sum, self.length)

    @staticmethod
    def from_array(elems) -> 'Statistics':
        """Compute the statistics of an array of numbers.

        >>> Statistics.from_array([1,2,3])
        Statistics(sum=6, length=3)
        >>> Statistics.from_array([])
        Statistics(sum=0, length=0)
        """
        return Statistics(np.sum(elems), np.size(elems))

class KDTree():
    """Tree structure for fast queries on multi-dimensional data
    """

    def __init__(self, data, dimensions, objective, first_dimension=0):
        """Create a tree
        
        arguments:
        data -- a DataFrame containing the data to store
        dimensions -- the dimensions along which the data will be queried
        objective -- the "objective" dimension. The query will return statistics
                     about the value of this dimension

        >>> import pandas
        >>> # We create a dataset with three points (1,3), (2,3) and (3,4)
        >>> df = pandas.DataFrame({"x": [1,2,3], "y":[3,3,4], "target": [0,1,1]})
        >>> tree = KDTree(df, ('x','y'), 'target')
        >>> tree
        <KDTree of dimension 2>
        """
        first_dimension = first_dimension % len(dimensions)
        dimension = dimensions[first_dimension]
        median = np.median(data[dimension])

        left = data[data[dimension] < median]
        right = data[data[dimension] > median]

        self.dimensions = dimensions
        self.dimension = dimension
        self.median = median
        self.objective = objective

        self.middle_data = data[objective][data[dimension] == median]

        self.left, self.right = None, None
        if len(left) > 0:
            self.left = KDTree(left, dimensions, objective, first_dimension+1)
        if len(right) > 0:
            self.right = KDTree(right, dimensions, objective, first_dimension+1)

    def query(self, query: dict) -> Statistics:
        """Find statistics about the points that are in a specified region in
        the K-dimensional space you defined.

        arguments:
        query -- A dict (or DataFrame), containing as keys the dimension names
                 and as values arrays containing the min and max value for that dimension
                 in the searched region.
 
        >>> import pandas
        >>> # We create a dataset with three points (1,3), (2,3) and (3,4)
        >>> df = pandas.DataFrame({"x": [1,2,3], "y":[3,3,4], "target": [0,1,1]})
        >>> tree = KDTree(df, ('x','y'), 'target')
        >>> # Query all points with x between 0 and 10 and y between 0 and 3 (inclusive)
        >>> tree.query({"x":[0,10], "y":[0,3]})
        Statistics(sum=1, length=2)
        >>> tree.query({"x":[0,10], "y":[0,10]})
        Statistics(sum=2, length=3)
        >>> tree.query({"x":[5,10], "y":[5,10]})
        Statistics(sum=0, length=0)
        """
        query_dim = query[self.dimension]

        if query_dim[0] <= self.median <= query_dim[1]:
            stats = Statistics.from_array(self.middle_data)
        else:
            stats = Statistics()

        if self.left and query_dim[0] < self.median:
            stats.merge(self.left.query(query))
        if self.right and query_dim[1] > self.median:
            stats.merge(self.right.query(query))

        return stats

    def __repr__(self):
        return "<KDTree of dimension %d>" % (len(self.dimensions),)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
