__author__ = 'yutongpang'
from os import stat
from array import array
from sys import byteorder as system_endian
import numpy as np


class Rawfilearray():
    def __init__(self, filename, endian):
        self.filename = filename
        self.endian = endian

    def get_file_original_data(self):
        with open(self.filename, 'rb') as file:
            result = array('h')
            result.fromfile(file,self.get_file_stat_count())
            result = self.__process_data_based_on_endian(result)
        return result

    def get_file_data_in_reshape_matrix(self, col_length, row_length, initial_index_count_from_0):
        original_array = self.get_file_original_data()
        return self.__reshape_array_to_square_matrix(original_array, col_length, row_length, initial_index_count_from_0)

    @staticmethod
    def __reshape_array_to_square_matrix(original_array, row_length, col_length, initial_index_count_from_0):
        orignial_nparray = np.array(original_array)[initial_index_count_from_0:col_length*row_length]
        return orignial_nparray.reshape(row_length, col_length)

    def __process_data_based_on_endian(self, array_data):
        if self.endian != system_endian:
            array_data.byteswap()
        return array_data

    def get_file_stat_count(self):
        file_size_count = int(stat(self.filename).st_size / 2)
        return file_size_count