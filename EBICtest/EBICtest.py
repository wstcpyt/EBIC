__author__ = 'yutongpang'
import sys
sys.path.append('/Users/yutongpang/PycharmProjects/EBIC')
print(sys.path)
import unittest
from EBICanalysis.rawfileprocess import Rawfile
import numpy as np


class EBICrawfileprocessTest(unittest.TestCase):
    def setUp(self):
        self.rawfile = Rawfile()
        self._rawfile_testpath = 'test_raw.dat'
        self.create_16_bit_tempfile()

    def test_read_raw_binary_file_count(self):
        self.assertEqual(9,self.rawfile.get_file_stat_count(self._rawfile_testpath))

    def create_16_bit_tempfile(self):
        array_16_bit = self.create_16_bit_array()
        return array_16_bit.tofile(self._rawfile_testpath)

    def create_16_bit_array(self):
        original_array = np.array([[1, 2, 3], [3, 4, 5], [6, 7, 8]])
        return original_array.astype('int16')

if __name__ == '__main__':
    unittest.main()