import numpy as np
from scipy.stats import skewcauchy
import matplotlib.pyplot as plt


np.random.seed(300)
rng = np.random.RandomState(300)
parameters = {'a': 0.9740369762791558, 'loc': 15.03607366592095, 'scale': 42.95071842779828}

PERIOD = 30  # dias
N_SIMUL = 1000

def generate():
    x = skewcauchy.rvs(parameters['a'])
    x = (parameters['loc'] + x) * parameters['scale'] 
    return x




def check_pos_interval(intervals:list, value):
    pos = 0
    if value == 1:
        return len(intervals) - 2
    for i in range(len(intervals) - 1):
        if intervals[i] <= value < intervals[i + 1]:
            break
        else: 
            pos += 1
    return pos



def calc_cashback(card, u):
    cash_probs = card['Cashback']['Porcentaje']
    cash_perc = card['Cashback']['Probabilidad']
    interval = [0] + cash_perc
    interval = np.array(interval).cumsum()
    k = check_pos_interval(interval, u)
    return cash_probs[k]

data = [generate() for _ in range(PERIOD)]

def simul_creditcard(limit, card):
    adjust_limit = PERIOD // 30
    limit = max(1, adjust_limit) * limit
    history = np.zeros(PERIOD + 1)
    histpchbk = np.zeros(PERIOD + 1)
    i = 0
    while history.sum() <= limit:
        u = rng.uniform(0,1)
        history[i] = data[i]
        cashback = calc_cashback(card, u)
        histpchbk[i] = history[i] * cashback
        i += 1
        if i == PERIOD:
            break
    return history, histpchbk


def cashback_prom(limit, card):
    h, cb = simul_creditcard(limit, card)
    mh = h.sum()
    mcb = cb.sum()
    cbt = mcb / mh * 100
    cbt = round(cbt, 2)
    return cbt

def cb_mean(limit, card):
    cbs = [cashback_prom(limit, card) for _  in range(N_SIMUL)]
    cbs = np.array(cbs).mean()
    return cbs


