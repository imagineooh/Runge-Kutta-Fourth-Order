# Runge-Kutta-Fourth-Order

## Pypi page:
https://pypi.org/project/rk4-solver/0.3.0/

# Description
This package implements Runge-Kutta 4th order (RK4) method for solving systems of ordinary differential equations (ODEs).

It is designed to numerically approximate solutions of coupled differential equations of the form:

x'(t) = f1(x, y)
y'(t) = f2(x, y)

With both x' and y' functions being parameters of function RK4.

To understand better how RK4 works, I reccomend looking at this page:
https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods

## Features
- RK4 numerical integration for 2D systems
- No external dependencies required
- Lightweight and fast implementation
- Python 3+ required

## Usage

from rk4_solver import rk4

def f1(x, y):
    return x + y

def f2(x, y):
    return x - y

x_vals, y_vals = rk4(f1, f2)

# Licence
This project is licenced under an MIT licence

## Future updates
I plan on:
- Implementing more Runge Kutta Methods
- Find a time efficient way to add more dimensions to the original code
