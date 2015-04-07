__author__ = 'yutongpang'
import sys
sys.path.append('/Users/yutongpang/PycharmProjects/EBIC')
import unittest
from EBICanalysis.rawfileprocess import Rawfilearray
import numpy as np
from array import array
from sys import byteorder as system_endian
from unittest.mock import patch
import numpy.testing as npt


class RawfileprocessTest(unittest.TestCase):
    def setUp(self):
        self.rawfile = Rawfilearray('test_raw.dat', system_endian)
        self._rawfile_testpath = 'test_raw.dat'
        self.create_16_bit_tempfile_in_system_endian()
        self.original_array = self.rawfile.get_file_original_data()

    def test_read_raw_binary_file_count(self):
        self.assertEqual(9, self.rawfile.get_file_stat_count())

    def test_read_raw_binary_file_data_in_system_endian(self):
        self.compare_data()

    def test_read_raw_binary_file_data_in_antisystem_endian(self):
        self.rawfile = Rawfilearray('test_raw.dat', 'antiendian')
        self.create_16_bit_tempfile_in_antisystem_endian()
        self.compare_data()

    @patch.object(Rawfilearray, 'get_file_original_data')
    def test_read_file_data_in_square_matrix(self, mock_get_file_original_data):
        mock_get_file_original_data.return_value = array('h', [1, 2, 3, 4, 5, 6, 7, 8, 9])
        expected_result = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        result = self.rawfile.get_file_data_in_reshape_matrix(3, 3, 0)
        mock_get_file_original_data.assert_called_with()
        npt.assert_array_equal(expected_result, result)

    @patch.object(Rawfilearray, 'get_file_original_data')
    def test_read_file_data_in_square_matrix_with_truncated_array(self, mock_get_file_original_data):
        expected_result = np.array([[1, 2], [3, 4]])
        mock_get_file_original_data.return_value = array('h', [1, 2, 3, 4, 5, 6, 7, 8, 9])
        result = self.rawfile.get_file_data_in_reshape_matrix(2, 2, 0)
        mock_get_file_original_data.assert_called_with()
        npt.assert_array_equal(expected_result, result)

    def compare_data(self):
        expected_result = array('h', [1, 2, 3, 4, 5, 6, 7, 8, 9])
        result = self.rawfile.get_file_original_data()
        self.assertEqual(expected_result,result)

    def create_16_bit_tempfile_in_system_endian(self):
        array_16_bit = self.create_16_bit_array()
        return array_16_bit.tofile(self._rawfile_testpath)

    def create_16_bit_tempfile_in_antisystem_endian(self):
        array_16_bit = self.create_16_bit_array().byteswap(True)
        return array_16_bit.tofile(self._rawfile_testpath)

    def create_16_bit_array(self):
        original_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        return original_array.astype('int16')

if __name__ == '__main__':
    unittest.main()