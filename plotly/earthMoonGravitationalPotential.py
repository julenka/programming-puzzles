#!/usr/bin/env python
'''
Plots the gravitational potential of the earth and moon
assumes the earth is at 0,0 and moon is on x-axis.

Inspired by http://www.wired.com/2014/07/contour-plots-with-python-and-plotly/?mbid=social_twitter
and: https://gist.github.com/rhettallain/1aa12b44d59562ce08fc

Practicing plotly
'''

__author__ = 'julenka'

import numpy as np
import plotly.plotly as py
import math
from plotly.graph_objs import *

massEarth = 5.9729e24
massMoon = 7.3477e22
distanceFromEarthToMoon = 384400 # units is km
G = 6.67384e-11

earthOffset = 100000
earthLocation = [earthOffset,earthOffset]
moonLocation = [earthOffset + distanceFromEarthToMoon/2,
                earthOffset + math.sqrt(math.pow(distanceFromEarthToMoon,2) - math.pow(distanceFromEarthToMoon/2, 2))]

# make mesh
step = 10000
x = np.arange(1, 2 * distanceFromEarthToMoon, step)
y = np.arange(1, 2 * distanceFromEarthToMoon, step)
X,Y = np.meshgrid(x,y)


# gravitational potential values
V = X * 0
Vmax = 4e10

for r in range(len(X)):
    for c in range(len(Y)):
        currentLocation = np.array([X[r,c], Y[r,c]])

        distanceToEarth = np.linalg.norm(np.subtract(currentLocation, earthLocation))
        gpFromEarth = G * massEarth / distanceToEarth #V(r) = Gm/r

        distanceToMoon = np.linalg.norm(np.subtract(currentLocation, moonLocation))
        gpFromMoon = G * massEarth / distanceToMoon #V(r) = Gm/r

        totalGp = max(0, min(Vmax, gpFromEarth + gpFromMoon))
        V[r,c] = totalGp

data=[{'x':x, 'y':y, 'z':V, 'type':'contour'}]
plot_url = py.plot(data, filename='earth-moon gravitational potential')