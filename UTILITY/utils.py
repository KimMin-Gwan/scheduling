import tkinter as tk
import numpy as np

class FileInput():
    def __init__(self, file):
        self._file = file
        self._f_list = self._read_File()
        self._con_list = self._conversion_type()
        self._size = len(self._con_list)

    def _read_File(self):
        temp = []
        for idx in self._file:
            temp.append(idx.split())
        return temp

    def getSize(self):
        return len(self._f_list)
    
    def get_original_list(self):
        return self._f_list
    
    def get_conversion_list(self):
        return self._con_list
    
    def _conversion_type(self):
        temp = []
        f_ndarray = np.array(self._f_list)
        temp = f_ndarray[:, 1:].astype(int)
        idx = np.arange(temp.shape[0]).reshape(-1, 1)
        temp = np.hstack((idx, temp))

        return temp.tolist()











