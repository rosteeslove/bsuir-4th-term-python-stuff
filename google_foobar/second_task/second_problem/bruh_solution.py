"""
This 2 minute solution should work in most* cases.

* like really in almost all of them.
"""


from functools import reduce
from itertools import izip_longest


VERSION_LEVEL_NUM = 3 # for the number of version points so to say
MAX_VERSION_NUM = 1000 # still an overkill


def version_pseudonum(version_num_str):
    """
    Return version's pseudo number.  The point is to achieve
    the following:

    'Newer version's pseudo number is bigger than the older version's.'
    """
    return reduce(lambda a, b: MAX_VERSION_NUM*a + b,
                  [sum(v) for v in
                      izip_longest(VERSION_LEVEL_NUM*[0],
                                   [int(n) for n in
                                       version_num_str.split('.')],
                                   fillvalue=0)]) + len(version_num_str)