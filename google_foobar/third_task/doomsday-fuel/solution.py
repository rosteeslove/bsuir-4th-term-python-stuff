def non_empty(list_, index_list):
    non_empties = []
    for index in index_list:
        if list_[index] != 0:
            non_empties.append(index)
    return non_empties


def naive_solution(m):
    n = len(m)
    probs = [1] + [0]*(n-1)
    indexes_of_nonterminal_stages = []

    for (i, row) in enumerate(m):
        for el in row:
            if el != 0:
                indexes_of_nonterminal_stages.append(i)
                break

    while (indexes := non_empty(probs, indexes_of_nonterminal_stages)):
        for index in indexes:
            sum_ = 0
            for el in m[index]:
                sum_ += el

            for (i, el) in enumerate(m[index]):
                probs[i] += probs[index] * (el / sum_)

            probs[index] = 0

    return probs


def solution(m):
    return naive_solution(m)

arr = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
print(naive_solution(arr))
