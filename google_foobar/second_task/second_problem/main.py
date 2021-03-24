"""

"""


from bruh_solution import version_pseudonum


def solution(l):
    return sorted(l, key=version_pseudonum)

print(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))