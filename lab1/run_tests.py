import unittest

from arithmetic_operation_binary_code import *

class TestFloatingPointConversion(unittest.TestCase):

    def test_floating_point_convert(self):
        self.assertEqual(convert_to_floating_point(1.5), '0.01111111.10000000000000000000000')
        self.assertEqual(convert_to_floating_point(2.5), '0.10000000.01000000000000000000000')

        self.assertEqual(convert_to_10_from_floating_point("0.01111111.10000000000000000000000"), 1.5)
        self.assertEqual(convert_to_10_from_floating_point("0.10000000.01000000000000000000000"), 2.5)

        number_1 = convertation_from_meduim_value_to_float_standart("10.101")
        number_2 = convertation_from_meduim_value_to_float_standart("111.1")
        self.assertEqual(number_1, "0.10000000.01010000000000000000000")
        self.assertEqual(number_2, "0.10000001.11100000000000000000000")

    def test_sum_floating_point(self):
        number_1 = convert_to_floating_point(12.0)
        number_2 = convert_to_floating_point(23.23)
        self.assertEqual(summa_floating_point(number_1, number_2), '0.10000100.01100111010111000010100')

        number_3 = convert_to_floating_point(13.9)
        number_4 = convert_to_floating_point(1.2)
        self.assertEqual(summa_floating_point(number_3, number_4), '0.10000011.11000110011001100110010')
    
    def test_dividing_floating_part(self):
        number_1 = convert_to_unmarked_code(13)
        number_2 = convert_to_unmarked_code(4)
        self.assertEqual(divide_binary_code(number_1, number_2), '00000011.01000')

        number_3 = convert_to_unmarked_code(199)
        number_4 = convert_to_unmarked_code(3)
        self.assertEqual(divide_binary_code(number_3, number_4), '01011111.11111')

        self.assertEqual(convert_from_fixed_point_to_10('00000001.10001'), 1.53125)
        self.assertEqual(convert_from_fixed_point_to_10('00000000.00101'), 0.15625)
        
    def test_convert_from_2_to_10(self):
        self.assertEqual(convert_from_2_to_10('11111010'), -6)
        self.assertEqual(convert_from_2_to_10('00001111'), 15)

    def test_convert_to_reverse_code(self):
        self.assertEqual(convert_to_reverse_code(4), '00000100')
        self.assertEqual(convert_to_reverse_code(-9), '11110110')

    def test_convert_to_extra_code(self):
        self.assertEqual(convert_to_extra_code(2), '00000010')
        self.assertEqual(convert_to_extra_code(-2), '11111110')

    def test_summa_extra_code(self):
        self.assertEqual(summa_extra_code('00000001', '00000001'), '00000010')
        self.assertEqual(summa_extra_code('11111111', '00000001'), '00000000')

    def test_multiplication_extra_code(self):
        self.assertEqual(multiplication_extra_code('00000001', '00000010'), '00000010')
        self.assertEqual(multiplication_extra_code('00000010', '00000010'), '00000100')

    def test_substraction_2_numbers(self):
        self.assertEqual(substraction_2_numbers('00000010', '00000001'), '00000001')
        self.assertEqual(substraction_2_numbers('00000001', '00000010'), '11111111')

    def test_convert_to_direct_code(self):
        self.assertEqual(convert_to_direct_code(5), '00000101')
        self.assertEqual(convert_to_direct_code(-5), '10000101')


if __name__ == '__main__':
    unittest.main()