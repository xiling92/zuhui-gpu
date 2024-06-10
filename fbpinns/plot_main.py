#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 17:33:12 2021

@author: bmoseley
"""

# This module imports and calls various plotting functions depending on the dimensionality of the FBPINN / PINN problem

# This module is used during training by main.py

import plot_main_1D
import plot_main_2D
import plot_main_3D
import plot_main_2x2D
import plot_main_3x2D


def plot_FBPINN(*args):
    "Generates FBPINN plots during training"
    
    # figure out dimensionality of problem, use appropriate plotting function
    c = args[9]
    nd = c.P.d[0]
    ndy = len(range(c.P.d[1])[c.P.exact_dim_select]) if hasattr(c.P, "exact_dim_select") else c.P.d[1]
    if ndy == 1:
        if   nd == 1:
            return plot_main_1D.plot_1D_FBPINN(*args)
        elif nd == 2:
            return plot_main_2D.plot_2D_FBPINN(*args)
        elif nd == 3:
            return plot_main_3D.plot_3D_FBPINN(*args)
        else:
            return None
            # TODO: implement higher dimension plotting
    else: # ndy >= 1
        if nd == 2:
            return plot_main_2x2D.plot_2D_FBPINN(*args)
        elif nd == 3:
            return plot_main_3x2D.plot_3D_FBPINN(*args)
        else:
            return None


def plot_PINN(*args):
    "Generates PINN plots during training"
    
    # figure out dimensionality of problem, use appropriate plotting function
    c = args[7]
    nd = c.P.d[0]
    ndy = c.P.d[1]
    if ndy == 1:
        if   nd == 1:
            return plot_main_1D.plot_1D_PINN(*args)
        elif nd == 2:
            return plot_main_2D.plot_2D_PINN(*args)
        elif nd == 3:
            return plot_main_3D.plot_3D_PINN(*args)
        else:
            return None
            # TODO: implement higher dimension plotting
    else: # ndy >= 1
        if nd == 2:
            return plot_main_2x2D.plot_2x2D_PINN(*args)
        elif nd == 3:
            return plot_main_3D.plot_3D_PINN(*args)
        else:
            return None
