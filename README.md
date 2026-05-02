# Runge-Kutta-Fourth-Order

## Pypi page:
https://pypi.org/project/rk4-solver/0.3.0/

# Description
This Python package implements the Runge-Kutta 4th order (RK4) method for solving systems of ordinary differential equations (ODEs).

It is designed to numerically approximate solutions of coupled differential equations of the form:

x'(t) = f1(x, y)
y'(t) = f2(x, y)
With both being parameters of function RK4.

## Features
RK4 numerical integration for 2D systems
No external dependencies required
Lightweight and fast implementation
Python 3+ required

## Usage

from rk4_solver import rk4

def f1(x, y):
    return x + y

def f2(x, y):
    return x - y

x_vals, y_vals = rk4(f1, f2)
