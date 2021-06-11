"""
This module is to be used when forming histogram data and
plotting histograms and linear interpolations for them
(frequency polygons).
"""


import copy
import matplotlib.pyplot as plt


def equalbin(vs, group_num, normalize='частоты'):
    """Return data needed for type 1 histogram
    as a list of tuples each being:
    (a bin's left bound, a bin's occurrences count)
    
    Each bin's interval has its left bound included
    and right excluded, e.g. [0, 1), [1, 2), [3, 4), ...

    Re the normalize parameter:
     - use 'частоты' for each bin's height to be
    the number of occurences of random values
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
    if normalize == 'частоты':
        pass
    elif normalize == 'частости':
        for interval in hdata[:-1]:
            interval[1] /= n
    elif normalize == 'плотность':
        for interval in hdata[:-1]:
            interval[1] /= h*n

    hdata[-1][1] = hdata[-2][1]
    return hdata


def equalvar(a, b, vs, group_num, normalize=True):
    """Return data needed for type 2 histogram
    as a list of tuples each being:
    (a bin's left bound, a bin's occurrences count)
    
    Each bin's interval has its left bound included
    and right excluded, e.g. [0, 1), [1, 2), [3, 4), ...
    """
    bin_capacity = len(vs) // group_num + (1 if len(vs) % group_num != 0 else 0)

    hdata = [[a, 0]]
    for i in range(len(vs)):
        hdata[-1][1] += 1
        last_bin_empty = False

        # if the last bin is full:
        if hdata[-1][1] == bin_capacity:
            # calculate its right bound:
            if i == len(vs) - 1:
                right_bound = b
            else:
                right_bound = (vs[i] + vs[i+1]) / 2

            # add a new empty bin:
            hdata.append([right_bound, 0])
            last_bin_empty = True

    if last_bin_empty:
        del hdata[-1]

    if normalize:
        square = 0
        for i in range(len(hdata) - 1):
            # calculating local density and updating square:
            hdata[i][1] = hdata[i][1] / (hdata[i+1][0] - hdata[i][0])
            square += hdata[i][1] * (hdata[i+1][0] - hdata[i][0])
        
        hdata[-1][1] = hdata[-1][1] / (b - hdata[-1][0])
        square += hdata[-1][1] * (b - hdata[-1][0])

        for hd in hdata:
            hd[1] /= square
    else:
        for hd in hdata:
            hd[1] /= len(vs)

    hdata.append([b, hdata[-1][1]])
            
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
        ps = [hd[0] for hd in hdata[1:]]
        for i in range(1, len(hdata)-1):
            hdata[i][1] += hdata[i-1][1]
    else:
        ps = [(hdata[i][0] + hdata[i+1][0]) / 2 for i in range(len(hdata) - 1)]

    # plotting polygon:
    plt.scatter(ps,
                [hd[1] for hd in hdata[:-1]])
    plt.plot(ps,
             [hd[1] for hd in hdata[:-1]],
             label=('полигон распределения' if not cumulative
             else 'кумулята'))
