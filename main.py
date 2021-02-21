import numpy as np
import matplotlib.pyplot as plt

def seq_gen(c):
    z = 0+0j
    while True:
        yield z
        z = z**2 + c


def is_divergent(rec_rel):
    gen, c = rec_rel, 0
    last_z = next(gen)
    while c < 10000:
        z = next(gen)
        if np.abs(z) > 5:
            return True    #probably diverging, saying 5 bc then its def outside Mandelbrot
        elif np.abs(z - last_z) < (10**-3):
            return False   #probably converging
        last_z = z
        c += 1
    return False
    #if it's abs is still within 2 after 500 iterations, it's probably repeating or converging within a finite space


def in_mandelbrot(c):
    return not is_divergent(seq_gen(c))


def cart(step, theta):
    return (step*np.sin(theta)) * 1j + (step*np.cos(theta))


def gen_set():
    coord, theta, c, steps, step, arr = 0+0j, 0, 0, 20000, 0.01, []
    while in_mandelbrot(coord):
        coord += step * 1j
    coord -= step * 1j
    while c < steps:
        while in_mandelbrot(coord + cart(step, theta)):
            theta += 0.05
        while not in_mandelbrot(coord + cart(step, theta)):
            theta -= 0.05
        coord = coord + cart(step, theta)
        arr.append(coord)
        c += 1
        print(c)
    return arr


def load():
    a = np.genfromtxt('mandelbrot outline.csv', np.clongdouble)
    plt.fill(np.real(a), np.imag(a))
    plt.axis('equal')
    plt.show()


if __name__ == '__main__':
    load()
    """a = gen_set(0.001)
    print(a)
    np.savetxt('mandelbrot outline.csv', np.array(a))
    plt.fill(np.real(a), np.imag(a))
    plt.axis('equal')
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.show()"""
