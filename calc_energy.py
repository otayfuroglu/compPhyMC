# -*- coding:utf-8 -*-
import math
import matplotlib.pyplot as plt
import time

from dynamic_vis import DynamicGraph, DynamicFig, save_graph_fig, save_disk_fig

#L = [[0.25, 0.25], [0.75, 0.25], [0.25, 0.75], [0.75, 0.75], [0.75, 0.3],
#     [0.5, 0.75], [0.75, 0.7]]

def get_distance(x, y, L):
    distances = []
    for i, j in L:
        distances.append(math.sqrt((x - i) ** 2 + (y - j) ** 2))
    return sorted(distances)


def l_j_potantial(r):
    return 4.0*((1/r)**12 - (1/r)**6)

def get_potential_e(cutoff_e, cutoff_r, L):

    """indirgenmiş birimler kullanıldı;
        Uznluk birimi; σ
        Enerjinin birimi; ɛ
        Kütle birimi; m

        This method requires to apply an energy correction
        during the calculation of the potential energy.
    """

    total_potantial_e = 0.0

    i = 0
    for x, y in L:
        i += 1
        distances = [distance for distance in get_distance(x, y, L[i:])
                     if distance < cutoff_e and distance != 0]
        for r in distances:
            total_potantial_e += l_j_potantial(r) - l_j_potantial(cutoff_r) # indirgenmiş birimler kullandığımızdan düzeltme ekldik
    return total_potantial_e


def run_example_LJ():
    epsilon = 1.0  # kcal/mol
    sigma = 0.4
    cutoff_e = 10
    #get_potential_e(epsilon, sigma, cutoff_e, L)

    a = 0.25
    n_steps = 100

    len_box = 10.0
    cutoff_r = len_box/2.0

    graph_pot = DynamicGraph()
    dynamic_fig = DynamicFig()


    energy = []
    distence = []

    i = 0
    for step in range(1, n_steps):
        distence.append(a)
        pos_1 = [[0.2, 0.5], [a, 0.5]]
        a += 0.03



        y = get_potential_e(cutoff_e, cutoff_r, pos_1)

        energy.append(y)
        #
        # dynamic_fig.set_fig(1)
        # dynamic_fig.set_x(-2.5, f_limit=5)
        # dynamic_fig.set_y(-2.5, f_limit=5)
        # dynamic_fig.dynamic_fig(sigma, pos_1, step, n_steps)
        #
        #
        # # dinamik olarak pot_E grafiğini göster
        # graph_pot.set_fig(2)
        # graph_pot.set_y(1)
        # graph_pot.set_x(10)
        # graph_pot.graph(x=step, y=y, n_steps=n_steps)


        save_graph_fig("data/calculate_energy/graph/l_j_energy_graph_%s" %i, distence, energy)
        #save_disk_fig("data/calculate_energy/l_j_dual_disks_%s" %i, sigma, pos_1, -2.5, 5)
        i += 1

    #plt.show()



#run_example_LJ()

"""
237442.016602
42.948871851
-0.890965287583
-0.224207724386
-0.0615234375
-0.0208215955593
-0.00828341911546
-0.00372182085151
"""