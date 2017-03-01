import numpy as np

class Statistics:
    """Represents a set of floats, allowing to retrieve its mean, without storing
    all the individual floats"""
    def __init__(self, sum:float = 0, length:int = 0):
        self.sum = sum
        self.length = length
    def add(elem: float):
        self.sum += elem
        self.length += 1
    def merge(self, other: 'Statistics'):
        return Statistics(self.sum + other.sum, self.length + other.length)
    def mean(self) -> float:
        return self.sum / self.length
    def __len__(self):
        return self.length
    @staticmethod
    def from_array(elems) -> 'Statistics':
        return Statistics(np.sum(elems), np.size(elems))


class Box:
    """Represents an n-dimensional box"""
    def __init__(self, df):
        self.limits = pd.DataFrame({"emin":np.min(df), "emax":np.max(df)})
    def intersect(self, other: 'Box') -> bool:
        b1, b2 = self.limits, other.limits
        return np.all((b1["max"] >= b2["min"]) & (b1["min"] <= b2["max"]))

class KDTree():
    """Tree structure for fast querying multi-dimensional data"""
    def __init__(self, data, dimensions, objective, first_dimension=0):
        """Create a tree
        
        arguments:
        data -- a dict (or DataFrame) containing the data to store
        dimensions -- the dimensions along which the data will be queried
        objective -- the "objective" dimension. The query will return statistics
                     about the value of this dimension
        """
        first_dimension = first_dimension % len(dimensions)
        dimension = dimensions[first_dimension]
        median = np.median(data[dimension])
        split_cond = data[dimension] < median
        left, right = data[split_cond], data[~split_cond]

        self.dimension = dimension
        self.median = median
        self.stats = Statistics.from_array(data[objective])
        self.box = Box(data[dimensions])
        if len(right) > 0:
            self.left = KDTree(left, dimensions, objective, first_dimension+1)
            self.right = KDTree(right, dimensions, objective, first_dimension+1)
        else:
            self.left, self.right = None, None

    def query(self, q: Box) -> Statistics:
        if self.box.intersect(q):
            if self.left == None:
                return self.stats
            else:
                return self.left.query(q).merge(self.right.query(q))
        else:
            return Statistics()


