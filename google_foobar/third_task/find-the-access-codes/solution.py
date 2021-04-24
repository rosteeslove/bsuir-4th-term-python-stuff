"""
This module contains solution function.
"""


def brute(some_list):
    """
    O(n^3) time complexity.
    """
    list_len = len(some_list)
    num_of_lucky_triples = 0
    for i in range(list_len):
        for j in range(i+1, list_len):
            if some_list[j] % some_list[i] != 0:
                continue
            for k in range(j+1, list_len):
                if some_list[k] % some_list[j] == 0:
                    num_of_lucky_triples += 1

    return num_of_lucky_triples


def foo_one(some_list):
    """
    O(n^2) time complexity.
    """
    list_len = len(some_list)

    indices = [[] for elem in some_list]
    for i in range(list_len-1, 0, -1):
        for j in range(0, i):
            if some_list[i] % some_list[j] == 0:
                indices[i] += [j]

    result = 0
    for i in range(list_len-1, 1, -1):
        for index in indices[i]:
            result += len(indices[index])

    return result


def solution(some_list):
    return foo_one(some_list)
