""""""


# from bruh_solution import version_pseudonum
from normal_solution import version_key


def solution(l):
    return sorted(l, key=version_key)


print(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))