# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import random
from calc_energy import get_potential_e

def read_yz_coord(file_name, close):
    """xx"""
    coord_xy = []
    with open(file_name) as lines:
        for line in lines:
            coord_xy.append([close*float(line.split()[2]), close*float(line.split()[3])])
    return coord_xy


def get_init_pos(n_atoms, len_box, L):

    """
    the function use for liquid

    for L = 5; len_box = 7.91780
    """
    lattice_constant = len_box / (L + 0.5)
    b = lattice_constant
    x0 = np.ones((3, 2))
    x0 *= b / 2.
    #print x0
    x0[0, :] = 0.
    x0[1, 1] = 0.
    x0[2, 0] = 0.
    #x0[3,0] = 0.

    #print x0
    positions = np.zeros((n_atoms, 2))
    index = 0
    for i in range(L):
        for j in range(L):
            #for k in range(L):
                for chi in range(3):
                    positions[index, 0] = x0[chi, 0] + i*b
                    positions[index, 1] = x0[chi, 1] + j*b
                    #positions[index,2] = x0[chi,2] + k*b
                    index += 1
    positions += b*0.5
    return positions


def get_random_xy_coord(n_atoms, len_box, sigma):
    coords = []
    for i in range(n_atoms):
        coords.append([random.uniform(0, len_box-sigma),
                       random.uniform(0, len_box-sigma)])
    return coords

def get_init_pos_random_opt(opt, n_atoms, len_box, sigma):
    """
    :param n_atoms, len_box:
    :return:
    """

    cutoff_e = len_box
    cutoff_r = len_box / 2.0

    condition = True
    while condition is True:
        coords = get_random_xy_coord(n_atoms, len_box, sigma)
        trial_energy = get_potential_e(cutoff_e, cutoff_r, coords)
        if -opt < trial_energy < opt:
            condition = False

    return coords


L = 10
#n_atoms = 3*(L**2)

#len_box = 7.91780 #BOX_LENGTH = L*LATTICE_CONSTANT + 0.5 * LATTICE_CONSTANT
                  #LATTICE_CONSTANT = 1.43964


# fl = open("2d_coord.xyz", "w")
# fl.write("%d \n" % (len(get_init_pos(n_atoms, len_box, L))))
# fl.write("\n")
# for line in get_init_pos(n_atoms, len_box, L):
#     fl.write("He\t%s\t%s\n"%(line[0], line[1]))
# fl.close()

def vis_pop():
    sigma = 0.5
    n_atoms = 50
    len_box = 10
    opt =10

    ax = plt.gca()
    ax.set_ylim(0, len_box)
    ax.set_xlim(0, len_box)
    for (x, y) in read_yz_coord("geom/coord_he.xyz"):
        circle = plt.Circle((x, y), radius=sigma, edgecolor="r", facecolor="r")
        ax.add_patch(circle)
    # plt.savefig(os.path.join(output_dir, '%d.png' % img), transparent=True)
    plt.show()

#vis_pop()

#sigma = 0.1
#n_atoms = 20
#len_box = 20.0
#get_init_pos_random_opt(n_atoms, len_box, sigma)

#print read_yz_coord("geom/coord_he.xyz")