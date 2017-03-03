#!/usr/bin/env python3
import numpy

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
        return Statistics(numpy.sum(elems), numpy.size(elems))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
