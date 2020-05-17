from matplotlib import pyplot as plt
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')

def sshahrzads_discretization_function(a, b, c, d, e):
    # TODO: create a function that returns discrete values of a
    #       quadratic function that is defined by the parameters
    #       ax^2 + bx + c for the interval x=[-10, 10]
    values = []
    
    for x in range (-10, 10, 1):
        y = a*x**4 + b*x**3 + c*x**2 + d*x + e
        
        values.append(y) # INSERT YOUR CODE HERE
        
    return values

if __name__ == '__main__':
    parser.add_argument('-a', required=True, type=int, nargs=1, help='The first parameter of the abcd formula')
    parser.add_argument('-b', type=int, nargs=1, help='The second parameter of the abcd formula')
    parser.add_argument('-c', type=int, nargs=1, help='The third parameter of the abcd formula')
    parser.add_argument('-d', type=int, nargs=1, help='the fourth parameter of the abcd formula')
    parser.add_argument('-e', type=int, nargs=1, help='the fifth parameter of the abcd formula')
    args = parser.parse_args()
    
    values = sshahrzads_discretization_function(args.a[0], args.b[0], args.c[0], args.d[0], args.e[0])

    plt.plot(range(-10, 10), values)
    plt.show()
