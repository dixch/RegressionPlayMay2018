#! python3

'''
Demonstrates polynomial functions, and how these compare to the x-transform when fitting linear regression objects

'''




import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# generate linear data
x = list(range(-20,20,1))
y = x*1
df = pd.DataFrame(np.column_stack([x, y]), columns=['x', 'y'])


def plot_powers_y(df):
    '''takes a df with x and y; multiplies y out by 6 exponents'''

    fig = plt.subplots()

    for n in range(1, 7):
        df['y**%d' % n] = df['y'] ** n
        plt.subplot(2, 3, n)
        plt.plot(df['x'], df['y**%d' % n], 'b.')
        plt.title('y = x** %d' % n)
    plt.show()

def plot_powers_x(df):
    '''takes a df with x and y; multiplies x out by 6 exponents
    Plots the original linear values of y but now with transformed x values'''

    fig = plt.subplots()

    for n in range(1, 7):
        df['x**%d' % n] = df['x'] ** n # Is there a way to remove whitespace around %d?
        plt.subplot(2, 3, n)
        plt.plot(df['x**%d' % n], df['y'], 'r.')
        plt.title('x = y**%d' % n)
    plt.show()

def plot_roots(df):
    '''takes a df with x and y; multiplies y out by 6 exponents'''

    fig = plt.subplots()

    for n in range(1, 7):
        df['y**1/%d' % n] = df['y'] ** (1/n)
        plt.subplot(2, 3, n)
        plt.plot(df['x'], df['y**1/%d' % n], 'y.')
        plt.title('y = x**1/%d' % n)
    plt.show()


plot_powers_y(df)
plot_powers_x(df)
plot_roots(df)
