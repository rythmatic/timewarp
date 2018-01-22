#
# Author: Derk van Gulick
#
from time import time

class Timewarp(object):

    def __init__(self, f):
        self.print_args = False
        self.f = f


    def __call__(self, *args, **kwargs):
        t0 = time()
        result = self.f(*args, **kwargs)
        t1 = time()

        fname = self.f.__name__
        if self.print_args:
            print('{} ran in {}s | args: {}'.format(fname, t1 - t0, args))
        else:
            print('{} ran in {}s'.format(fname, t1 - t0))
        return result
        

    def print_args(self, enabled):
        self.print_args = enabled
