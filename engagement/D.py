__author__ = 'julenka'
import numpy as np
import matplotlib.pyplot as plt

a = [7.304545, 1.118182]
b = [7.868182, 6.318182]
c = [2.213636, 3.909091]
d = [5.659182, 4.009182]

miles_per_hour = 761.207
miles_per_second = miles_per_hour / 3600

# candidate points x goes 0 to 11, y goes 0 to 8
# spacing is 0.1
x = np.arange(0, 11, 0.1)
y = np.arange(0, 8, 0.1)
points = []

for xc in x:
    for yc in y:
        points.append([xc, yc])
np_points = np.array(points)

# for every candidate point, compute distance to a - d
a_dst = np.linalg.norm(np_points - a, axis = 1)
b_dst = np.linalg.norm(np_points - b, axis = 1)
c_dst = np.linalg.norm(np_points - c, axis = 1)
d_dst = np.linalg.norm(np_points - d, axis = 1)

# for every point, compute time to get to point
a_seconds = a_dst / miles_per_second
print a_dst[0], a_seconds[0]
b_seconds = b_dst / miles_per_second
c_seconds = c_dst / miles_per_second
d_seconds = d_dst / miles_per_second

# for every point, compute difference of b,a c,a d,a D2
b_deltas = b_seconds - a_seconds
c_deltas = c_seconds - a_seconds
d_deltas = d_seconds - a_seconds

test_deltas = np.vstack((b_deltas, c_deltas, d_deltas)).T

# compute time difference of b,a c,a d,a from data D
import datetime
def parse(s):
    '''
    :param s: string to parse
    :return: number seconds since epoch
    '''
    t = datetime.datetime.strptime(s, "%H:%M:%S.%f")
    return t

lines = open("thunder.txt").readlines()[10:]
# dist(b,a), dist(c,a), dist(d,a)
observed_deltas = []
for line in lines:
    _,a,b,c,d = line.split()
    a_time = parse(a)
    b_time = parse(b)
    c_time = parse(c)
    d_time = parse(d)

    b_delta = (b_time - a_time).total_seconds()
    c_delta = (c_time - a_time).total_seconds()
    d_delta = (d_time - a_time).total_seconds()

    observed_deltas.append([b_delta, c_delta, d_delta])
observed_deltas = np.array(observed_deltas)
print observed_deltas[:10]
print test_deltas[:1000]

thunder_points = []
for observation in observed_deltas:
    distances = np.linalg.norm(observation - test_deltas, axis=1)
    min_i = np.argmin(distances)
    print min(distances), min_i, np_points[min_i]
    thunder_points.append(np_points[min_i])

thunder_points = np.array(thunder_points)

steps = [4,6,4,5,4,6,5,5,5,7,5]
i = 0
for step in steps:
    letter = thunder_points[i:i+step]
    i = i + step
    xs = letter[:,0]
    ys = letter[:,1]
    plt.axis([0,11,8,0])
    plt.plot(xs, ys, '-o')
    ax=plt.gca()
    ax.set_autoscale_on(False)
    plt.show()

# take abs(delta of D, D2) for every point
# find minimum point
