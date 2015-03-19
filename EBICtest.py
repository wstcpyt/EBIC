__author__ = 'yutongpang'
import unittest
from testfixtures import tempdir, compare
from EBICrawfileprocess.rawfileprocess import foo2bar

class EBICrawfileprocessTest(unittest.TestCase):
    @tempdir()
    def test_function(d):
        d.write('test.txt', b'some foo thing')
        foo2bar(d.path, 'test.txt')
        compare(d.read('test.txt'), b'some bar thing')

