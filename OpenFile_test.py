#!/usr/bin/python3

import unittest
import OpenFile
from pathlib import Path

class TestStringMethods(unittest.TestCase):
    def test_OpenFile(self):
        x = OpenFile.FileOpen("./new.txt")
        self.assertIsInstance(x, Path, "The instance x is not Path")
        with x.open() as f:
            self.assertEqual(f.read(), "hello world\n")

if __name__ == '__main__':
    unittest.main()
