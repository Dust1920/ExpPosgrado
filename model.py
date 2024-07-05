import numpy as np
from scipy.stats import skewcauchy
import matplotlib.pyplot as plt

np.random.seed(300)

parameters = {'a': 0.9740369762791558, 'loc': 15.03607366592095, 'scale': 42.95071842779828}



def generate():
    x = skewcauchy.rvs(parameters['a'])
    x = (parameters['loc'] + x) * parameters['scale'] 
    return x

def select_cashback(card: dict):
    options = card.keys()
    props = [card[o][0] for o in options]
    props = [0] + props
    acum_props = np.array(props).cumsum()
    return acum_props

cost_1 = 3000
card_1 = {
    0:[1, 0.02]
}
cost_2 = 300
card_2 = {
    0: [0.5, 0],
    1: [0.25, 0.04],
    2: [0.2, 0.05],
    3: [0.05, 0.06]
}




print(select_cashback(card_2))

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

data = [generate() for _ in range(30)]

def exp_month(limit):
    max_days = 30
    data = np.zeros(max_days)
    i = 0
    while data.sum() <= limit:
        data[i] = generate()
        i += 1
        if i == 30:
            break
    return data
compras = exp_month(50000)
acum_compras = compras.cumsum()

def calc_cashback(exps, cashrule):
    cashback = np.zeros(len(exps))
    for i, e in enumerate(exps):
        u = np.random.uniform(0,1)
        if u < 0.5:
            cashback[i] = 1
    return cashback
    

plt.plot(compras)
plt.plot(acum_compras)
plt.show()
