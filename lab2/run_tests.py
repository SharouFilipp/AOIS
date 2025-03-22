import unittest
from fromiration_table_true import *

class Test(unittest.TestCase):

    def test_logic_say_1(self):
        logic_say = 'a&!(b|c)'
        variables_amount = make_list_posible_values(logic_say)
        priority = make_priority(logic_say)
        result1 = result(make_priority(logic_say))

        line_cknf = cknf(variables_amount)
        cdnf1 = number_cdnf(variables_amount)

        line_cdnf = cdnf(variables_amount)
        cknf1 = number_cknf(variables_amount)
        
        result_value = get_result_of_table_true()
        number_result = convert_from_2_to_10(("").join(result_value))

        self.assertEqual(variables_amount, 3)
        self.assertEqual(priority, 'abc|!&')
        self.assertEqual(result1, ['0', '0', '0', '0', '1', '0', '0', '0'])
        
        self.assertEqual(line_cdnf, '(a&!b&!c)' )
        self.assertEqual(line_cknf, '(a|b|c)&(a|b|!c)&(a|!b|c)&(a|!b|!c)&(!a|b|!c)&(!a|!b|c)&(!a|!b|!c)' )
        self.assertEqual(cdnf1, [4])
        self.assertEqual(cknf1, [0, 1, 2, 3, 5, 6, 7])
        self.assertEqual(number_result, 8)

    def test_logic_say_2(self):
        logic_say = 'a->b~c'
        variables_amount = make_list_posible_values(logic_say)
        priority = make_priority(logic_say)
        result1 = result(make_priority(logic_say))

        line_cknf = cknf(variables_amount)
        cdnf1 = number_cdnf(variables_amount)

        line_cdnf = cdnf(variables_amount)
        cknf1 = number_cknf(variables_amount)
        
        result_value = get_result_of_table_true()
        number_result = convert_from_2_to_10(("").join(result_value))

        self.assertEqual(variables_amount, 3)
        self.assertEqual(priority, 'ab>c~')
        self.assertEqual(result1, ['0', '1', '0', '1', '1', '0', '0', '1'])
        

        self.assertEqual(line_cdnf, '(!a&!b&c)|(!a&b&c)|(a&!b&!c)|(a&b&c)' )
        self.assertEqual(line_cknf, '(a|b|c)&(a|!b|c)&(!a|b|!c)&(!a|!b|c)' )
        self.assertEqual(cdnf1, [1, 3, 4, 7])
        self.assertEqual(cknf1, [0, 2, 5, 6])
        self.assertEqual(number_result, 89)

if __name__ == '__main__':
    unittest.main()