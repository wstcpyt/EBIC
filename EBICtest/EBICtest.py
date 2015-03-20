__author__ = 'yutongpang'
import sys
sys.path.append('/Users/yutongpang/PycharmProjects/EBIC')
import unittest
from EBICanalysis.rawfileprocess import Rawfile
import numpy as np
from array import array
from sys import byteorder as system_endian

class EBICrawfileprocessTest(unittest.TestCase):
    def setUp(self):
        self.rawfile = Rawfile()
        self._rawfile_testpath = 'test_raw.dat'

    def test_read_raw_binary_file_count(self):
        self.create_16_bit_tempfile_in_system_endian()
        self.assertEqual(9, self.rawfile.get_file_stat_count(self._rawfile_testpath))

    def test_read_raw_binary_file_data_in_system_endian(self):
        self.create_16_bit_tempfile_in_system_endian()
        self.compare_data(self._rawfile_testpath, system_endian)

    def test_read_raw_binary_file_data_in_antisystem_endian(self):
        self.create_16_bit_tempfile_in_antisystem_endian()
        self.compare_data(self._rawfile_testpath, 'antisystem_endian')

    def compare_data(self, filename, endian):
        expected_result = array('h', [1, 2, 3, 3, 4, 5, 6, 7, 8])
        result = self.rawfile.get_file_data(filename, endian)
        self.assertEqual(expected_result,result)

    def create_16_bit_tempfile_in_system_endian(self):
        array_16_bit = self.create_16_bit_array()
        return array_16_bit.tofile(self._rawfile_testpath)

    def create_16_bit_tempfile_in_antisystem_endian(self):
        array_16_bit = self.create_16_bit_array().byteswap(True)
        return array_16_bit.tofile(self._rawfile_testpath)

    def create_16_bit_array(self):
        original_array = np.array([[1, 2, 3], [3, 4, 5], [6, 7, 8]])
        return original_array.astype('int16')

if __name__ == '__main__':
    unittest.main()