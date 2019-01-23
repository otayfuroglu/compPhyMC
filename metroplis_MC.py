# -*- coding:utf-8 -*-

import random, math
import matplotlib.pyplot as plt
import time
import numpy as np
import pandas as pd

from init_pos import get_init_pos_random_opt, read_yz_coord
from project import calc_energy as e
from displace_atom import displace_disk_random
from dynamic_vis import DynamicFig, DynamicGraph, save_disk_fig



def monte_carlo_sim():

    # epsilon = 0.997  # kcal/mol
    # const_kB = 0.001987204 #kcal/mol boltzman constant

    total_step = 15000
    step = 0
    n_accept = 0
    n_reject = 0

    temperature = 1.4275 #kB
    beta = 1 / temperature
    sigma = 0.65  # yarı çap
    len_step = sigma + 0.1

    cutoff_e = 5.0

    len_box = 20.0

    cutoff_r = len_box / 2.0

    #previous_conf = get_init_pos_random_opt(10, n_atoms, len_box, sigma)
    previous_conf = read_yz_coord("../geom/coord_he.xyz", 0.9)
    print previous_conf
    n_atoms = len(previous_conf)


    pot_energy_i = e.get_potential_e(cutoff_e, cutoff_r, previous_conf)
    print pot_energy_i


    dynamic_fig = DynamicFig()
    graph_pot = DynamicGraph()

    accept_reject_ratio = []
    list_pot_energy = []
    positions = []

    while step < total_step:
        print "step", step

        trial_disk_ind = np.random.random_integers(0, n_atoms-1)
        trial_disk = previous_conf[trial_disk_ind]
        trial_move = np.array([2 * np.random.ranf() - 1., 2 * np.random.ranf() - 1.]) * len_step

        displace_disk_random(len_box, trial_disk, trial_move) # bir diskin rastgele değiştiriyoruz

        print "-------------------------", len(previous_conf)

        delta_e = e.get_potential_e(cutoff_e, cutoff_r, previous_conf) - pot_energy_i

        if delta_e < 0:

            step += 1
            n_accept += 1
            pot_energy_i = e.get_potential_e(cutoff_e, cutoff_r, previous_conf)
            list_pot_energy.append(pot_energy_i)

            print pot_energy_i


        elif np.random.random() < np.exp(-beta * delta_e):
            step += 1
            n_accept += 1
            pot_energy_i = e.get_potential_e(cutoff_e, cutoff_r, previous_conf)
            list_pot_energy.append(pot_energy_i)

        else:
            displace_disk_random(len_box, trial_disk, -trial_move)  # haraket ettirilen diski terar yerini alıyoruz
            n_reject += 1

        if step % 10 == 0:
            # dinamik olarak pot_E grafiğini göster
            graph_pot.set_fig(2)
            graph_pot.set_y(30)
            #graph_pot.set_auto_scale()
            graph_pot.graph(x=step, y=pot_energy_i, n_steps=total_step)

        if step % 100 == 0:

            # dinamik olarak diskleri göster
            dynamic_fig.set_fig(1)
            dynamic_fig.set_x(-sigma, f_limit=len_box + sigma)
            dynamic_fig.set_y(-sigma, f_limit=len_box + sigma)
            dynamic_fig.dynamic_fig(sigma,  previous_conf, step, n_steps=total_step)



            #save_disk_fig("../data/metropolis_MC/pos/pos_%s" % step, sigma, previous_conf, -sigma, len_box + sigma)
            ratio = 100 * n_accept / (n_reject + n_accept)
            accept_reject_ratio.append(ratio)

            positions.append(previous_conf)


        print "accepted --> %2.2f" % (100 * n_accept / (n_reject + n_accept))



    # df_energy = pd.DataFrame(data=list_pot_energy, columns=["Energy"])
    # df_energy.to_csv("data/metropolis_MC/motropolis_energy.csv")
    #
    # df_ratio = pd.DataFrame(data=accept_reject_ratio, columns=["% Ratio"])
    # df_ratio.to_csv("data/metropolis_MC/accept_reject_ratio.csv")

    #df_positions = pd.DataFrame(data=positions, columns=["Position"])
    #df_positions.to_csv("data/metropolis_MC/metropolis_position.txt")






monte_carlo_sim()
#plt.show()