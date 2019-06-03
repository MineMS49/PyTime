# -*- coding: utf-8 -*-
from time import perf_counter, process_time

class Chronos(object):
    def __init__(self):
        #[(start_total, elapsed_total), (start_processor, elapsed_processor)]
        self.chronos = [(0,0),(0,0)]
        return

    def __enter__(self):
        self.__reset__()
        self.__compute__()
        return

    def __exit__(self,error,value,trace):
        self.__compute__()
        return

    def __compute__(self):
        if (self.chronos[0][0] and self.chronos[1][0]):
            self.chronos[0] = (0,float(perf_counter()-self.chronos[0][0]))
            self.chronos[1] = (0,float(process_time()-self.chronos[1][0]))
        else:
            self.chronos[0] = (float(perf_counter()),0)
            self.chronos[1] = (float(process_time()),0)
        return

    def __reset__(self):
        self.chronos = [(0,0),(0,0)]
        return

    def set(self):
        self.__reset__()
        self.__compute__()
        return True

    def stop(self):
        self.__compute__()
        return True

    def get(self):
        return [self.chronos[0][1],self.chronos[1][1]]
        
    def tprint(self):
        return str("Total : %0.3f\nProcessor : %0.3f"%(self.chronos[0][1], self.chronos[1][1]))
        
