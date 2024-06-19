import numpy as np

def generate():
    x = np.random.normal(0,1)
    return x

def select_cashback(card:dict):
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


