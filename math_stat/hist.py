"""
This module is to be used when forming histogram data and
plotting histograms.

To be used for tasks 4 and 5.
"""


import matplotlib.pyplot as plt
import base


def equalbin(a, b, vs, group_num, normalize='nope'):
    """Return data needed for type 1 histogram
    as a list of tuples each being:
    (a bin's left bound, a bin's occurrences count)
    
    Each bin's interval has its left bound included
    and right excluded, e.g. [0, 1), [1, 2), [3, 4), ...

    Re the normalize parameter:
     - use 'nope' to get the number of occurences of random values
    from vs varseries
     - use 'simple' 
    """
    group_width = (b - a) / group_num
    hdata = [[a + i*group_width, 0] for i in range(group_num + 1)]


    index = 0
    for v in vs:
        if index == group_num-1 or v < hdata[index+1][0]:
            hdata[index][1] += 1
        else:
            index += 1
            hdata[index][1] += 1

    if normalize == 'simple':
        for interval in hdata[:-1]:
            interval[1] /= len(vs)
    elif normalize == 'for f(y)':
        square = 0
        for interval in hdata[:-1]:
            square += group_width*interval[1]

        for interval in hdata[:-1]:
            interval[1] /= square

    hdata[-1][1] = hdata[-2][1]

    return hdata


# (copied from second_and_third.ipynb with slight modifications)
def plot_histogram_alpha_and_polygon_and_fy(a, b, get_rv, n, group_num, normalize='nope'):
    vs = base.generate_varseries(get_rv, n)

    hdata = equalbin(a, b, vs, group_num, normalize=normalize)
    ps = [(hdata[i][0] + hdata[i+1][0]) / 2 for i in range(len(hdata) - 1)]

    # plotting histogram using step:
    plt.step([hd[0] for hd in hdata],
             [hd[1] for hd in hdata],
             where='post')
    
    # plotting polygon:
    plt.scatter(ps,
                [hd[1] for hd in hdata[:-1]])
    plt.plot(ps,
             [hd[1] for hd in hdata[:-1]],
             label='полигон распределения')

    # plotting histogram using hist:
    hist_params = {'bins': group_num,
                   'color': 'red',
                   'zorder': -1,
                   'alpha': 0.2}

    if normalize == 'nope':
        plt.hist(vs, **hist_params)
    elif normalize == 'simple':
        plt.hist(vs, **{**hist_params, 'weights': [1/len(vs)]*len(vs)})
    elif normalize == 'for f(y)':
        plt.hist(vs, **{**hist_params, 'density': 1})

    #plt.legend()
    #plt.xlabel("")
    #plt.show()


def equalvar(a, b, vs, group_num, normalize=True):
    """Return data needed for type 2 histogram
    as a list of tuples each being:
    (a bin's left bound, a bin's occurrences count)
    
    Each bin's interval has its left bound included
    and right excluded, e.g. [0, 1), [1, 2), [3, 4), ...

    Примечание: работает только для НСВ с почти-лишь-только-один-раз-встречающимися
    элементами вариационного ряда (здесь вар-ряд = выборка из-за *высокой степени
    уникальности* элементов выборки, т.е. элементы списка 'vs' могут повторяться,
    но это очень маловероятно, если число b-a неотрицательного порядка/
    однозначного отрицательного порядка - порядок условно от -9 до 10+)
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


# (copied from second_and_third.ipynb with slight modifications)
def plot_histogram_beta_and_polygon_and_fy(a, b, get_rv, n, group_num):
    vs = base.generate_varseries(get_rv, n)
    hdata = equalvar(a, b, vs, group_num)
    ps = [(hdata[i][0] + hdata[i+1][0]) / 2 for i in range(len(hdata) - 1)]

    # plotting histogram:
    plt.step([hd[0] for hd in hdata],
             [hd[1] for hd in hdata],
             where='post')
    
    # plotting polygon:
    plt.scatter(ps,
                [hd[1] for hd in hdata[:-1]])
    plt.plot(ps,
             [hd[1] for hd in hdata[:-1]],
             label='полигон распределения')

    #plt.legend()
    #plt.show()