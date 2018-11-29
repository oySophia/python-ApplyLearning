#!/usr/bin/python
# coding = utf8

import sys
import string
import numpy as np
import matplotlib.pyplot as plt


def main():
    form = ['ro-', 'b--<', 'g-*', 'y--s', 'c->']
    # x = np.arrange(1, 20, 2)
    # y = np.arrange(0, 10, 1)
    x = [12, 14, 16]
    y1 = [0.61, 0.59, 0.50]
    y2 = [0.62, 0.54, 0.49]
    y3 = [1.17, 1.12, 0.94]
    # b = x
    plt.plot(x, y1, 'ro-', linewidth=1.2, label="sparse_mat with 0.01")
    plt.plot(x, y2, 'r--*', linewidth=1.2, label="sparse_mat with 0.1")
    plt.plot(x, y3, 'b--s', linewidth=1.2, label="non-sparse mat")
    plt.legend(loc='upper right')
    # plt.title("Storage-Communication tradeoff \n n=10,k=5,d=5~9,B=1MB")
    plt.ylabel('''the excution time(s)''')
    plt.xlabel("the np-value")
    plt.xlim(12, 16)
    plt.ylim(0, 2.4)
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    main()
