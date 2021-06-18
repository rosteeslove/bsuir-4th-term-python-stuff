"""
This module is for analyzing varseries and whatnot.

Sources:
https://ru.wikipedia.org/wiki/%D0%94%D0%BE%D0%B2%D0%B5%D1%80%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9_%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D0%B2%D0%B0%D0%BB_%D0%B4%D0%BB%D1%8F_%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B3%D0%BE_%D0%BE%D0%B6%D0%B8%D0%B4%D0%B0%D0%BD%D0%B8%D1%8F_%D0%BD%D0%BE%D1%80%D0%BC%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B9_%D0%B2%D1%8B%D0%B1%D0%BE%D1%80%D0%BA%D0%B8
https://ru.wikipedia.org/wiki/%D0%94%D0%BE%D0%B2%D0%B5%D1%80%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9_%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D0%B2%D0%B0%D0%BB_%D0%B4%D0%BB%D1%8F_%D0%B4%D0%B8%D1%81%D0%BF%D0%B5%D1%80%D1%81%D0%B8%D0%B8_%D0%BD%D0%BE%D1%80%D0%BC%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B9_%D0%B2%D1%8B%D0%B1%D0%BE%D1%80%D0%BA%D0%B8

To be used for task 5.
"""


import numpy as np
from scipy import stats


def expected_value(vs):
    """Матожидание по выборке. Точечная оценка."""
    return sum(vs) / len(vs)


def variance(vs):
    """Дисперсия по выборке. Точечная оценка."""
    mu = expected_value(vs)

    return sum([(v-mu)**2 for v in vs]) / (len(vs) - 1)


def confidence_interval(vs, confidence, param, mu=None, var=None):
    """Доверительный интервал."""
    assert 0 <= confidence <= 1

    if param == "матожидание":
        return mu_conint(vs, confidence, var=var)
    elif param == "дисперсия":
        return var_conint(vs, confidence, mu=mu)
    else:
        raise NotImplementedError


def mu_conint(vs, confidence, var=None):
    """Доверительный интервал для матожидания.
    Дисперсия может быть известна/ неизвестна."""
    n = len(vs)
    alpha = 1 - confidence
    mean = expected_value(vs)

    if var:
        shift = np.sqrt(var / n) * stats.norm.ppf(1 - alpha / 2)
    else:
        s_sq = variance(vs)
        shift = np.sqrt(s_sq / n) * stats.t(df=n-1).ppf(1 - alpha / 2)

    return mean - shift, mean + shift


def var_conint(vs, confidence, mu=None):
    """Доверительный интервал для дисперсии.
    Матожидание может быть известно/ неизвестно."""
    n = len(vs)
    alpha = 1 - confidence
    s_sq = variance(vs)

    if mu:
        deviations_squared = [(mu - el)**2 for el in vs]
        ds_sum = sum(deviations_squared)
        return (ds_sum / stats.chi2.ppf(1 - alpha / 2, df=n),
                ds_sum / stats.chi2.ppf(alpha/2, df=n))
    else:
        return (s_sq*(n-1) / stats.chi2.ppf(1 - alpha / 2, df=n-1),
                s_sq*(n-1) / stats.chi2.ppf(alpha/2, df=n-1))
