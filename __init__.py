# -*- coding: utf-8 -*-
from time import perf_counter, process_time



class Chronos():
    def __init__(self):
        #[(start_total, elapsed_total), (start_processor, elapsed_processor)]
        self.NULL_TUPLE = (0, 0)
        self.timer = [self.NULL_TUPLE, self.NULL_TUPLE]
        return

    def __enter__(self):
        self.__reset__()
        self.__compute__()
        return self.timer

    def __exit__(self, error, value, trace):
        self.__compute__()
        if (error and value and trace):
            self.__reset__()
        return

    def __compute__(self):
        if (self.timer[0][0] and self.timer[1][0]):
            self.timer[0] = (self.timer[0][0], float(perf_counter()-self.timer[0][0]))
            self.timer[1] = (self.timer[1][0], float(process_time()-self.timer[1][0]))
        else:
            self.timer[0] = (float(perf_counter()), self.timer[0][1])
            self.timer[1] = (float(process_time()), self.timer[1][1])
        return

    def __reset__(self):
        self.timer = [self.NULL_TUPLE, self.NULL_TUPLE]
        return

    def start(self):
        self.__reset__()
        self.__compute__()
        return True

    def stop(self):
        self.__compute__()
        return True

    def get(self):
        return [self.timer[0][1],self.timer[1][1]]

    def __repr__(self):
        return '\
Chronos(\n\
    {\n\
        "elapsed_time":{\n\
            "start_timestamp":%f,\n\
            "result_time":%f\n\
        },\n\
        "processing_time":{\n\
            "start_proc_time":%f,\n\
            "result_time":%f\n\
        }\n\
    }\n\
)'%(*self.timer[0], *self.timer[1])

    def __str__(self):
        return str("Elapsed time : %0.3f\nProcessing time : %0.3f"%(self.timer[0][1], self.timer[1][1]))

    def __float__(self):
        return float("%0.3f"%(self.timer[0][1]))
