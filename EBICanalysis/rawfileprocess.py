__author__ = 'yutongpang'
from os import stat
from array import array
from sys import byteorder as system_endian


class Rawfile():
    def get_file_data(self, filename, endian):
        with open(filename, 'rb') as file:
            result = array('h')
            result.fromfile(file,self.get_file_stat_count(filename))
            result = self.process_data_based_on_endian(result, endian)
        return result

    @staticmethod
    def process_data_based_on_endian(array, endian):
        if endian != system_endian:
            array.byteswap()
        return array

    @staticmethod
    def get_file_stat_count(filename):
        file_size_count = int(stat(filename).st_size / 2)
        return file_size_count