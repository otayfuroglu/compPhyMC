# -*- coding:utf-8 -*-

import random, math
import matplotlib.pyplot as plt
import time
import numpy as np
import pandas as pd

from init_pos import get_init_pos_random_opt, read_yz_coord
from project import calc_energy as e
from displace_atom import displace_disk_markov
from dynamic_vis import DynamicFig, DynamicGraph, save_disk_fig,save_graph_fig


def markov_chain_MC_sim():

    total_step = 15000
    step = 0
    sigma = 0.7  # yarı çap
    len_step = sigma + 0.5

    cutoff_e = 5.0
    len_box = 20.0

    cutoff_r = len_box / 2.0

    previous_conf = read_yz_coord("../geom/coord_he.xyz", 0.9)


    list_pot_energy = []


    dynamic_fig = DynamicFig()
    #graph_pot = DynamicGraph()


    while step < total_step:

        step += 1
        displace_disk_markov(sigma, len_box, previous_conf, len_step) # konfigürsyonu rastgele değiştiriyoruz

        pot_energy = e.get_potential_e(cutoff_e, cutoff_r, previous_conf)
        list_pot_energy.append(pot_energy)

        if step % 100 == 0:
            print "step", step
            print sum(list_pot_energy) / step
            dynamic_fig.set_fig(1)
            dynamic_fig.set_x(0, f_limit=len_box)
            dynamic_fig.set_y(0, f_limit=len_box)
            dynamic_fig.dynamic_fig(sigma, previous_conf, step, n_steps=total_step)

            #save_disk_fig("data/markov_chain_MC/pos/pos_%s" % step, sigma, previous_conf, 0, len_box)

            #dinamik olarak pot_E grafiğini göster
            # graph_pot.set_fig(2)
            # #graph_pot.set_y(20)
            # graph_pot.set_auto_scale()
            # graph_pot.graph(x=step, y=sum(list_pot_energy) / step, n_steps=total_step)
            # graph_pot.save_graph("data/markov_chain_MC/energy_graph/energy_graph_%s" %step)


    df_energy = pd.DataFrame(data=list_pot_energy, columns=["Energy"])
    df_energy.to_csv("data/markov_chain_MC/markov_chain_energy.csv")

markov_chain_MC_sim()
#plt.show()