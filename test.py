import unittest
from main_ import*
class my_test(unittest.TestCase):
    def test_args(self):
        self.assertEqual(adder(2,2),4)

    def test_kwargs(self):
        self.assertEqual(adder(4, 2), 6)
if __name__=="__main__":
    unittest.main_()