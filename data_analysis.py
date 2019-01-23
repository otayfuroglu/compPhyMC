
# -*- coding:utf-8 -*-

import random, math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def heat_capacity(temperature, variance):
 result = 1.5 + variance/temperature**2
 return result


def calc_heat_cap_MC(df_energys, start):
    n_atoms = 50.0
    temperature = 1.4275 #kB
    #print df_energys["Energy"][500:]

    var_sample = np.var(df_energys["Energy"][start:])/n_atoms

    return heat_capacity(temperature, var_sample)

def print_heat_cap(df_energys_metropolis, df_energys_markovchain):
    print "Heat capacity from metropolis_MC: %2.3f" % calc_heat_cap_MC(df_energys_metropolis, 1000)
    print "Heat capacity from markov_chain_MC: %2.3f" % calc_heat_cap_MC(df_energys_markovchain, 100)




df_energys_metropolis = pd.read_csv("data/metropolis_MC/motropolis_energy.csv")
df_energys_markovchain = pd.read_csv("data/markov_chain_MC/markov_chain_energy.csv")


def save_graph_fig(file_name, xdata, ydata):
    plt.subplot()
    plt.plot(xdata, ydata, 'r-')
    plt.ylim(-2, 10)
    plt.xlabel(" ($\sigma$)")
    plt.ylabel("Enerji ($\epsilon$)")
    plt.savefig(file_name)

def vis_metropolis_MC_graph_e(df_energys):
    y = df_energys["Energy"]
    zoom = 15*10**3 # zoom adjust to 15 000
    plt.figure(1)
    x = np.linspace(0, zoom, zoom)
    x *= 15*10**(-3)
    n_atoms = 50

    plt.ylim(-2, 5)
    #plt.xlim(0, 25)
    plt.xlabel(r'adim sayisi x $10^5$')
    plt.ylabel(r'$\frac{U}{N}$', fontsize=20)
    plt.plot(x, y[0:zoom] / n_atoms, label="potential")
    plt.savefig('data/metropolis_MC/energy_MMC_50_zoom.png')
    #plt.show()

def vis_metropolis_MC_frame_e(df_energys):
    y = df_energys["Energy"]
    zoom = 15*10**3 # zoom adjust to 15 000
    plt.figure(1)
    x = np.linspace(0, zoom, zoom)
    x *= 15*10**(-3)
    n_atoms = 50

    for i in range(zoom):
        if i % 10 == 0:
            plt.ylim(-2, 5)
            plt.xlim(-2, 25)
            plt.xlabel(r'adim sayisi x $10^5$')
            plt.ylabel(r'$\frac{U}{N}$', fontsize=20)
            plt.plot(x[:i], y[0:i] / n_atoms, label="potential", color="blue")
            plt.savefig('data/metropolis_MC/energy_graph/energy_graph_%s' %i)
            #plt.show()

        if i == 5000: break

def vis_markov_MC_graph_e(df_energys):
    y = df_energys["Energy"]
    zoom = 5*10**3 # zoom adjust to 15 000
    plt.figure(2)
    x = np.linspace(0, zoom, zoom)
    x *= 5*10**(-3)
    n_atoms = 50

    plt.ylim(-2, 5)
    #plt.xlim(0, 5)
    plt.xlabel(r'adim sayisi x $10^3$')
    plt.ylabel(r'$\frac{U}{N}$', fontsize=20)
    plt.plot(x, y[0:zoom] / n_atoms, label="potential")
    plt.savefig('data/markov_chain_MC/energy_MCMC_50_zoom.png')
    #plt.show()

def vis_markov_MC_frame_e(df_energys):
    y = df_energys["Energy"]
    zoom = 5 * 10 ** 3  # zoom adjust to 15 000
    plt.figure(2)
    x = np.linspace(0, zoom, zoom)
    x *= 5*10**(-3)
    n_atoms = 50
    #print x[:10]
    for i in range(zoom):

        if i % 10 == 0:
            plt.ylim(-2, 5)
            plt.xlim(-1, 25)
            plt.xlabel(r'adim sayisi x $10^3$')
            plt.ylabel(r'$\frac{U}{N}$', fontsize=20)
            plt.plot(x[0:i], y[0:i] / n_atoms, label="potential", color="blue")
            plt.savefig('data/markov_chain_MC/energy_graph/energy_graph_%s' %i)
            #plt.show()

def vis_markov_mertopolis_MC_graph_e(df_energys_metropois, df_energys_markov):
    y1 = df_energys_metropois["Energy"]
    y2 = df_energys_markov["Energy"]

    zoom = 15*10**3 # zoom adjust to 15 000
    plt.figure(3)
    x = np.linspace(0, zoom, zoom)
    x *= 15*10**(-3)
    n_atoms = 50


    plt.ylim(-2, 2)
    #plt.xlim(0, 50)
    plt.xlabel(r'adim sayisi x $10^3$')
    plt.ylabel(r'$\frac{U}{N}$', fontsize=20)
    plt.plot(x, y1[0:zoom] / n_atoms)
    plt.plot(x, y2[0:zoom] / n_atoms)
    plt.legend(["Metropolis MC", "Marcov Chain MC"])
    plt.savefig('data/energy_MCMC_50_zoom.png')
    #plt.show()

#vis_metropolis_MC_graph_e(df_energys_metropolis)
#vis_markov_MC_graph_e(df_energys_markovchain)
#vis_markov_mertopolis_MC_graph_e(df_energys_metropolis, df_energys_markovchain)

#print sum(df_energys_metropolis["Energy"][10000:])/len(df_energys_metropolis)
#print sum(df_energys_markovchain["Energy"][3000:])/len(df_energys_markovchain)

#print_heat_cap(df_energys_metropolis, df_energys_markovchain)

#vis_markov_MC_frame_e(df_energys_markovchain)
vis_metropolis_MC_frame_e(df_energys_metropolis)