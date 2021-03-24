"""
The optimal solution.
"""


VER_LEVEL_NUM = 3


def version_key(ver):
    """
    Return version key to compare versions by.
    """
    ver_nums = ver.split('.')
    ver_len = len(ver_nums)
    assert ver_len <= VER_LEVEL_NUM

    return (tuple([int(v) for v in ver_nums]
                  + [0]*(VER_LEVEL_NUM - ver_len))
            + (ver_len,))