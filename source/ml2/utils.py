import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np
import argparse

def knn_illustration_dataset():
    np.random.seed(42)
    n = 10
    k1 = np.random.randn(n, 2)
    k1[:, 0] += 1
    k1[:, 1] -= 1

    k2 = np.random.randn(n, 2)
    k2[:, 0] += 1
    k2[:, 1] += 1

    k3 = np.random.randn(n, 2)
    k3[:, 0] -= 2
    k3[:, 1] += 2

    k4 = np.random.randn(n, 2)
    k4[:, 0] -= 2
    k4[:, 1] -= 1

    kx  = np.array([-1, -1])

    x = np.concatenate([k1, k2, k3, k4])
    y = np.zeros(n * 4, dtype=np.int32)
    y[:n] = 0
    y[n:n*2] = 1
    y[2*n:n*3] = 2
    y[n*3:] = 3
    dists = [np.sqrt(np.sum((kx - x[i]) ** 2)) for i in range(n*4)]
    # Yaqin qo'shnilari
    
    mark_table = table = """|$x_1$|$x_2$|$x_1$|$x_2$|$x_1$|$x_2$|$x_1$|$x_2$|
|---|---|---|---|---|---|---|---|
"""
    for i in range(n):
        mark_table += f"|{k1[i, 0]:.2f}|{k1[i, 1]:.2f}" + \
         f"|{k2[i, 0]:.2f}|{k2[i, 1]:.2f}" + \
         f"|{k3[i, 0]:.2f}|{k3[i, 1]:.2f}" + \
         f"|{k4[i, 0]:.2f}|{k4[i, 1]:.2f}|\n"
    
    mark_dist_table = """|Sinf|1|2|3|4|5|6|7|8|9|10|
|---|---|---|---|---|---|---|---|---|---|---|\n""" +\
    "|1-sinf|" + "|".join([f"{val:.2f}" for val in dists[:n]]) + "|\n" + \
    "|2-sinf|" + "|".join([f"{val:.2f}" for val in dists[n:2*n]]) + "|\n" + \
    "|3-sinf|" + "|".join([f"{val:.2f}" for val in dists[2*n:3*n]]) + "|\n" + \
    "|4-sinf|" + "|".join([f"{val:.2f}" for val in dists[3*n:]]) + "|"
    
    argsort_dists = np.array(dists).argsort()
    mark_dist_sort_table = """|#|$(x^{(*)}, x^{(i)})$|Sinfi|
|---|----|----|\n""" + \
    "\n".join([f"|{i+1}|{dists[k]:.2f}|{y[k]+1}-sinf|" for i, k in enumerate(argsort_dists)])

    return (x,
            y,
            kx, dists, 
            mark_table, mark_dist_table,
            mark_dist_sort_table)

def draw_knn_illustration(ks=[],
                          save=False):
    k1, k2, k3, k4, kx, dists, _ = knn_illustration_dataset()
    sort_dists = sorted(dists)

    s = 30
    n = k1.shape[0]

    plt.scatter(k1[:, 0],
                k1[:, 1],
                s=s,
                c='black',
                marker='*',
                label="1-sinf")
    plt.scatter(k2[:, 0],
                k2[:, 1],
                s=s,
                c='green',
                marker='+',
                label="2-sinf")
    plt.scatter(k3[:, 0],
                k3[:, 1],
                s=s,
                c='blue',
                marker='v',
                label="3-sinf")
    plt.scatter(k4[:, 0],
                k4[:, 1],
                s=s,
                c='yellow',
                marker='o',
                label="4-sinf")
    
    plt.scatter(kx[0],
                kx[1],
                s=s+20,
                c='red',
                marker='x',
                label="Yangi")
    plt.legend()
    plt.xlabel("$x_1$")
    plt.ylabel("$x_2$")
    
    if ks:
        for k in ks:
            if k < n * 4:
                circle = Circle(kx,
                                radius=sort_dists[k],
                                alpha=0.3)
                gca = plt.gca()
                gca.add_patch(circle)

    if save:
        plt.savefig("./images/knn_illustration.svg")


def p_norm_illustration():
    # Values of p to visualize
    p_values = [0.2, 0.4, 0.5, 1, 2, 10, 1000]
    colors = ['yellow', 'red', 'orange', 'green', 'blue', 'purple', 'black']

    # Create grid of x and y
    x = np.linspace(-1.5, 1.5, 400)
    y = np.linspace(-1.5, 1.5, 400)
    X, Y = np.meshgrid(x, y)

    plt.figure(figsize=(7, 7))
    for i, p in enumerate(p_values):
        Z = np.power(np.abs(X), p) + np.power(np.abs(Y), p)
        plt.contour(X, Y, Z, 
                    levels=[1], 
                    colors=[colors[i]], 
                    linewidths=2, 
                    label=f'$p = {p}$')

    # Fix legend by creating custom lines
    from matplotlib.lines import Line2D
    custom_lines = [Line2D([0], [0], color=c, lw=2) for c in colors]
    plt.legend(custom_lines, [f'p = {p}' for p in p_values])

    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.gca().set_aspect('equal')
    plt.title("2 o'lchovli fazoda birlik p-normalar to'plami")
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig('./images/p-norm.svg')
    

if __name__ == '__main__':
    # draw_knn_illustration()
    # draw_knn_illustration(ks=[1, 4, 15])
    p_norm_illustration()