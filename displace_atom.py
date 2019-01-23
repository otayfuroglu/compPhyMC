# -*- coding:utf-8 -*-

import random

def displace_disk_markov(sigma, len_box, previous_conf, len_step):
    """function will displace two dimantional disk position
    according to markov metropolis
    algorithm"""

    n_trials = 100
    for trial in range(n_trials):

        # dynamic_fig(previous_conf, sigma)

        a = random.choice(previous_conf)
        b = [a[0] + random.uniform(-len_step, len_step), a[1] + random.uniform(-len_step, len_step)]
        #b = [a[0] + len_step * random.uniform(-1, 1), a[1] + random.uniform(-1, 1)] #0.2 * ranf(-1,1)


        min_dist = min((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2 for c in previous_conf if c != a)
        box_cond = min(b[0], b[1]) < sigma or max(b[0], b[1]) > len_box - sigma
        if not (box_cond or min_dist < 4.0 * sigma ** 2):
            a[:] = b
    return previous_conf

def displace_disk_random(len_box, trial_atom, trial_move):
    """diskleri teker tker yer değiştirir"""

    for k in range(2):
        #print trial_atom[k]
        trial_atom[k] += trial_move[k]

    #check_positions
    for k in range(2):
        if trial_atom[k] > len_box:
            trial_atom[k] -= len_box

        elif trial_atom[k] < 0.0:
            trial_atom[k] += len_box

    return trial_atom