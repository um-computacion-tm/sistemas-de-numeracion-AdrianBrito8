import unittest

def bin_to_dec(bin_str):
    decimal = 0
    for digit in bin_str:
        decimal = decimal*2 + int(digit)
    return decimal

def dec_to_bin(decimal):
    if decimal == 0:
        return "0"
    bin_str = ""
    while decimal > 0:
        remainder = decimal % 2
        bin_str = str(remainder) + bin_str
        decimal //= 2
    return bin_str

def hex_to_dec(hex_str):
    decimal = 0
    for digit in hex_str:
        if digit.isdigit():
            decimal = decimal*16 + int(digit)
        else:
            decimal = decimal*16 + ord(digit.upper()) - 55
    return decimal

def dec_to_hex(decimal):
    if decimal == 0:
        return "0"
    hex_str = ""
    while decimal > 0:
        remainder = decimal % 16
        if remainder < 10:
            hex_str = str(remainder) + hex_str
        else:
            hex_str = chr(remainder + 55) + hex_str
        decimal //= 16
    return hex_str

def oct_to_dec(oct_str):
    decimal = 0
    for digit in oct_str:
        decimal = decimal*8 + int(digit)
    return decimal

def dec_to_oct(decimal):
    if decimal == 0:
        return "0"
    oct_str = ""
    while decimal > 0:
        remainder = decimal % 8
        oct_str = str(remainder) + oct_str
        decimal //= 8
    return oct_str

# class TestNumeracion(unittest.TestCase):
#     def bin_to_dec(self):
#         self.assertEqual(bin_to_dec('01011100'), 92)

#     def dec_to_bin(self):
#         self.assertEqual(dec_to_bin(97), '01100001')

# class TestNumeracion(unittest.TestCase):
#     def test_bin_to_dec(self):
#         self.assertEqual(bin_to_dec('01011100'), 92)

#     def test_dec_to_bin(self):
#         self.assertEqual(dec_to_bin(97), '1100001')

#     def test_hex_to_dec(self):
#         self.assertEqual(hex_to_dec('1F'), 31)

#     def test_dec_to_hex(self):
#         self.assertEqual(dec_to_hex(255), 'FF')

#     def test_oct_to_dec(self):
#         self.assertEqual(oct_to_dec('77'), 63)

#     def test_dec_to_oct(self):
#         self.assertEqual(dec_to_oct(63), '77')


# if __name__ == '__main__':
#     unittest.main()
