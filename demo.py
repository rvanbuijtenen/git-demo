from matplotlib import pyplot as plt
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')

def sshahrzads_discretization_function(a, b, c):
    # TODO: create a function that returns discrete values of a
    #       quadratic function that is defined by the parameters
    #       ax^2 + bx + c for the interval x=[-10, 10]
    values = []

    # INSERT YOUR CODE HERE
    return values

if __name__ == '__main__':
    parser.add_argument('-a', required=True, type=int, nargs=1, help='The first parameter of the abc formula')
    parser.add_argument('-b', type=int, nargs=1, help='The second parameter of the abc formula')
    parser.add_argument('-c', type=int, nargs=1, help='The third parameter of the abc formula')
    args = parser.parse_args()
    values = sshahrzads_discretization_function(args.a[0], args.b[0], args.c[0])

    plt.plot(range(-10, 10), values)
    plt.show()
