__author__ = 'yutongpang'
from os import stat


class Rawfile():
    def get_file_stat_count(self, filename):
        file_size_count = int(stat(filename).st_size / 2)
        return file_size_count