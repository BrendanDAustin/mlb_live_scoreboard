#from RPi.GPIO import LOW, HIGH
import timeit
import pandas as pd
from numpy import array
LOW= False
HIGH = True
class gpio_map:
    def __init__(self):
        self.mux = {'C':20,
               'B':16,
               'A':12,
               'en':7}

        self.bcd_0 = {'en':4,
                 'A':27,
               'B':2,
               'C':3,
               'D':17}
        self.bcd_1 = {'en':9,
               'A':5,
               'B':22,
               'C':10,
               'D':11}

        self.bcd_2 = {'en':19,
                 'A':21,
                 'B':6,
                 'C':13,
                 'D':26}
        self.bases_balls_strikes = 8
        self.outs = 25

        self.pin_set = self.create_tuples()

    def create_tuples(self):
        pin_set = []
        for i in [self.mux.values(),self.bcd_0.values(),self.bcd_1.values(),self.bcd_2.values()]:
            for j in i:
                pin_set.append(j)
        pin_set.insert(self.bases_balls_strikes,-1)
        pin_set.insert(self.outs,-1)
        return pin_set