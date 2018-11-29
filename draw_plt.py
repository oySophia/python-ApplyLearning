#!/usr/bin/python
# coding = utf8

import sys
import string
import numpy as np
import matplotlib.pyplot as plt

def f_fun(d, k, i):
    a = (2.0 * d) / ((2.0 * k - i - 1.0) * i + 2.0 * k * (d - k + 1.0))
    return a

def g_fun(d, k, i):
    a = (2.0 * d - 2.0 * k + i + 1.0) * i * 1.0 / (2.0 * d)
    return a

def main():
    form = ['ro-', 'b--<', 'g-*', 'y--s', 'c->']
    k = 5
    d = [9, 8, 7, 6, 5]
    x = y = [1.0 / k]
    for t in range(5):
        r = [f_fun(d[t], k, i) for i in range(k - 1, -1, -1)]
        a = [((1.0 - g_fun(d[t], k, i) * r[k - i - 1]) * 1.0 / (k - i)) for i in range(k - 1, 0, -1)]
        a.append(1.0 / k)
        x.append(r[0])
        y.append(a[0])
        plt.plot(r, a, form[t], linewidth=2.0, label="$d=" + str(d[t]) + ",n=10,k=5$")
    plt.plot(x, y, linewidth=1.2, color='black')
    plt.plot([1.0], [1.0 / k], 'rs')
    plt.annotate("MDS point", xy=(1.0, 1.0 / k), xycoords='data', xytext=(0.8, 0.25),
                 arrowprops=dict(arrowstyle="->", linewidth=1.2))
    # plt.plot([1.0], [1.0/k], 'rs')
    plt.legend(loc='upper right')
    plt.title("Storage-Communication tradeoff \n n=10,k=5,d=5~9,B=1MB")
    plt.ylabel("Storage per node $\\alpha$")
    plt.xlabel("Bandwidth to repair one node $\\gamma$")
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()