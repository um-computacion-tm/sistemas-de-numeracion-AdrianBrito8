import unittest
from sist_numeracion import dec_to_bin, dec_to_hex, dec_to_oct, bin_to_dec ,hex_to_dec, oct_to_dec

class TestNumeracion(unittest.TestCase):
    def test_bin_to_dec(self):
        self.assertEqual(bin_to_dec('01011100'), 92)

    def test_dec_to_bin(self):
        self.assertEqual(dec_to_bin(97), '1100001')

    def test_hex_to_dec(self):
        self.assertEqual(hex_to_dec('1F'), 31)

    def test_dec_to_hex(self):
        self.assertEqual(dec_to_hex(255), 'FF')

    def test_oct_to_dec(self):
        self.assertEqual(oct_to_dec('77'), 63)

    def test_dec_to_oct(self):
        self.assertEqual(dec_to_oct(63), '77')


if __name__ == '__main__':
    unittest.main()