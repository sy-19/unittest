import unittest

import sample


class TestSample(unittest.TestCase):

    def test_add_num(self):
        self.assertEqual(10, sample.add_num(6, 4))
        
    def test_sub_num(self):
        self.assertEqual(2, sample.sub_num(6, 4))
        
    def test_mul_num(self):
        self.assertEqual(24, sample.mul_num(6, 4))
        
    def test_div_num(self):
        self.assertEqual(1.5, sample.div_num(6, 4))
        
if __name__ == '__main__':
    unittest.main()
