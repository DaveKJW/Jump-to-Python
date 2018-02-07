from __future__ import division, unicode_literals
from collections import Counter
import math, random
from ch04_linear_algebra import distance, vector_subtract, scalar_multiply

#경사 하강법

def sum_of_squares(v):
    return sum(v_i ** 2 for v_i in v)

