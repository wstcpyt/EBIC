__author__ = 'yutongpang'
import os

def foo2bar(dirpath, filename):
  path = os.path.join(dirpath, filename)
  with open(path, 'rb') as input:
      data = input.read()
  data = data.replace(b'foo', b'bar')
  with open(path, 'wb') as output:
      output.write(data)