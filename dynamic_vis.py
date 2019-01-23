# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import time

class DynamicFig:

    def __init__(self):
        pass

    def set_fig(self, n_fig):
        plt.figure(n_fig)
        self.ax = plt.gca()

    def set_x(self, s_limit, f_limit):
        self.ax.set_xlim(s_limit, f_limit)

    def set_y(self, s_limit, f_limit):
        self.ax.set_ylim(s_limit, f_limit)

    def dynamic_fig(self, sigma, previous_conf, step, n_steps):

        for (x, y) in previous_conf:
            circle = plt.Circle((x, y), radius=sigma, edgecolor="r", facecolor="r")
            self.ax.add_patch(circle)
        # plt.savefig(os.path.join(output_dir, '%d.png' % img), transparent=True)
        plt.pause(1e-19)
        #time.sleep(0.001)

        if step < n_steps:
            self.ax.clear()

class DynamicGraph:

    def __init__(self):
        self.xdata = []
        self.ydata = []

    def set_fig(self, n_fig):
        plt.figure(n_fig)
        self.ax2 = plt.gca()

    def set_x(self, limit):
        self.ax2.set_xlim(0, limit)

    def set_y(self, limit):
        self.ax2.set_ylim(-limit, limit)

    def set_auto_scale(self):
        self.ax2.autoscale()

    def set_clear(self):
        self.ax2.clear()

    def save_graph(self, file_name):
        plt.savefig(file_name)

    def graph(self, x, y, n_steps):
        self.ax2.set_xlim(0, n_steps)
        line, = self.ax2.plot(self.xdata, self.ydata, 'r-')

        self.xdata.append(x)
        self.ydata.append(y)

        line.set_xdata(self.xdata)
        line.set_ydata(self.ydata)
        #
        plt.draw()
        #plt.pause(1e-19) #diğer dynamic graph da olduğu için burda kullnamıyoruz
        #time.sleep(0.1)

def save_disk_fig(file_name, sigma, previous_conf, s_len_box, len_box):
    ax = plt.gca()
    ax.set_ylim(s_len_box, len_box)
    ax.set_xlim(s_len_box, len_box)
    for (x, y) in previous_conf:
        circle = plt.Circle((x, y), radius=sigma, edgecolor="r", facecolor="r")
        ax.add_patch(circle)
    plt.savefig(file_name)
    ax.clear()

def save_graph_fig(file_name, xdata, ydata):
    plt.subplot()
    plt.plot(xdata, ydata, 'r-')
    plt.ylim(-10, 10)
    #plt.xlim(0, 25)
    plt.xlabel("Mesafe ($\sigma$)")
    plt.ylabel("Enerji ($\epsilon$)")
    plt.savefig(file_name)
