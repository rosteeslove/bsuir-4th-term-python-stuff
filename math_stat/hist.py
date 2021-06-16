"""
This module is to be used when forming histogram data and
plotting histograms and linear interpolations for them
(frequency polygons).
"""


import math
import copy
import matplotlib.pyplot as plt


# условный эпсилон для работы с флоутами в equalvar
EPS = 0.000000001


def equalbin(vs, group_num, mode='частоты'):
    """Return data needed for type 1 histogram
    as a list of tuples each being:
    (a bin's left bound, a bin's occurrences count)
    
    Each bin's interval has its left bound included
    and right excluded, e.g. [0, 1), [1, 2), [3, 4), ...

    Re the mode parameter:
     - use 'частоты' for each bin's height to be
    the number of occurences of random values in it
    from vs varseries;
     - use 'частости' for each bin's height to be
    the probability for the random value to end up in
    a corresponding bin;
     - use 'плотность' to get the histogram
    as defined in bsuir docs, i.e. the one approximating
    the density function;
    """
    n = len(vs)
    m = group_num

    assert n >= 1
    assert m >= 1

    a = min(vs)
    b = max(vs)

    h = (b - a) / m
    hdata = [[a + i*h, 0] for i in range(m + 1)]

    # filling bins:
    index = 0
    for v in vs:
        while index != m-1 and v >= hdata[index+1][0]:
            index += 1
        hdata[index][1] += 1

    # normalizing:
    if mode == 'частоты':
        pass
    elif mode == 'частости':
        for interval in hdata[:-1]:
            interval[1] /= n
    elif mode == 'плотность':
        for interval in hdata[:-1]:
            interval[1] /= h*n

    hdata[-1][1] = hdata[-2][1]
    return hdata


def equalvar(vs, group_num, mode='частоты'):
    """Return data needed for type 2 histogram
    as a list of tuples each being:
    (a bin's left bound, a bin's height)
    
    Each bin's interval has its left bound included
    and right excluded, e.g. [0, 1), [1, 2), [3, 4), ...

    Re the mode parameter:
     - the same stuff as in equalbin.
    """
    n = len(vs)
    m = group_num

    assert n >= 2
    assert m >= 1
    assert n >= m

    a = min(vs)
    b = max(vs)

    bin_capacity = n / m

    # filling hdata:

    hdata = [[0, 0] for _ in range(m+1)]

    def mode1(index, vindex):
        return vindex - sum([hd[1] for hd in hdata[:index]])

    def mode2(index, vindex):
        return vindex / n - sum([hd[1] for hd in hdata[:index]])

    def mode3(index, vindex):
        ai = hdata[index-1][0]
        bi = (vs[vindex-1] + vs[vindex]) / 2
        h = bi - ai
        return 1 / (m*h)

    if mode == 'частоты':
        mode_func = mode1
    elif mode == 'частости':
        mode_func = mode2
    elif mode == 'плотность':
        mode_func = mode3
    else:
        raise Exception

    # working w/ first bin (it's guaranteed that it exists):
    # todo: maybe fix this? nah
    hdata[0][0] = a
    if m == 1:
        hdata[0][1] = 1 / (m*(b-a))

    # working w/ the other m-1 bins if m-1 > 0:
    for i in range(1, m):
        vindex = math.floor(i*bin_capacity + EPS) # ATTENTION HERE
        bi = (vs[vindex-1] + vs[vindex]) / 2
        hdata[i-1][1] = mode_func(i, vindex)
        hdata[i][0] = bi

    if m > 1:
        hdata[-2][1] = mode_func(m, n-1)

    # setting last (pseudo)bin:
    hdata[-1][0] = b
    hdata[-1][1] = hdata[-2][1]

    return hdata


# plotting equalbin histogram using hist
def plot_hist_w_mode(vs, group_num, normalize='частоты', cumulative=False):
    hist_params = {'bins': group_num,
                   'color': 'red',
                   'zorder': -1,
                   'alpha': 0.2,
                   'cumulative': cumulative}

    if normalize == 'частоты':
        plt.hist(vs, **hist_params)
    elif normalize == 'частости':
        plt.hist(vs, **{**hist_params, 'weights': [1/len(vs)]*len(vs)})
    elif normalize == 'плотность':
        plt.hist(vs, **{**hist_params, 'density': 1})


# plotting histogram using step
def plot_orig_histogram(hdata, cumulative=False):
    hdata = copy.deepcopy(hdata)
    if cumulative:
        for i in range(1, len(hdata)-1):
            hdata[i][1] += hdata[i-1][1]
        hdata[-1][1] = hdata[-2][1]

    plt.step([hd[0] for hd in hdata],
             [hd[1] for hd in hdata],
             where='post')


# plotting frequency polygon for histogram data
def plot_polygon(hdata, cumulative=False):
    hdata = copy.deepcopy(hdata)

    if cumulative:
        xs = [hd[0] for hd in hdata]
        ys = [0]*len(xs)
        for (i, hd) in enumerate(hdata[:-1]):
            ys[i+1] = ys[i]+hd[1]
    else:
        xs = [(hdata[i][0] + hdata[i+1][0]) / 2 for i in range(len(hdata) - 1)]
        ys = [hd[1] for hd in hdata[:-1]]

    # plotting polygon:
    plt.scatter(xs, ys)
    plt.plot(xs, ys,
             label=('полигон распределения' if not cumulative
             else 'кумулята'))
