import unittest
from fromiration_table_true import *
from minimization import *
from karno import * 

class Test(unittest.TestCase):

    def test_logic_say_1(self):
        logic_say = 'a&!(b|c)&d&e'
        variables_amount = make_list_posible_values(logic_say)
        priority = make_priority(logic_say)
        result1 = result(make_priority(logic_say))

        line_cknf = cknf(variables_amount)
        cknf1 = number_cdnf(variables_amount)
        minimazation_cknf1 = minimization_cknf(cknf(variables_amount))
        scnf = minimize_scnf(get_result_of_table_true(),variables_amount)
        print(line_cknf)

        line_cdnf = cdnf(variables_amount)
        cdnf1 = number_cknf(variables_amount)
        minimazation_cdnf1 = minimization_cdnf(cdnf(variables_amount))
        sdnf = minimize_sdnf(get_result_of_table_true(),variables_amount)
        print(line_cdnf)

        result_value = get_result_of_table_true()
        number_result = convert_from_2_to_10(("").join(result_value))

        self.assertEqual(variables_amount, 5)
        self.assertEqual(priority, 'abc|!&d&e&')
        

        self.assertEqual(line_cdnf, '(a&!b&!c&d&e)' )
        self.assertEqual(line_cknf, '(a|b|c|d|e)&(a|b|c|d|!e)&(a|b|c|!d|e)&(a|b|c|!d|!e)&(a|b|!c|d|e)&(a|b|!c|d|!e)&(a|b|!c|!d|e)&(a|b|!c|!d|!e)&(a|!b|c|d|e)&(a|!b|c|d|!e)&(a|!b|c|!d|e)&(a|!b|c|!d|!e)&(a|!b|!c|d|e)&(a|!b|!c|d|!e)&(a|!b|!c|!d|e)&(a|!b|!c|!d|!e)&(!a|b|c|d|e)&(!a|b|c|d|!e)&(!a|b|c|!d|e)&(!a|b|!c|d|e)&(!a|b|!c|d|!e)&(!a|b|!c|!d|e)&(!a|b|!c|!d|!e)&(!a|!b|c|d|e)&(!a|!b|c|d|!e)&(!a|!b|c|!d|e)&(!a|!b|c|!d|!e)&(!a|!b|!c|d|e)&(!a|!b|!c|d|!e)&(!a|!b|!c|!d|e)&(!a|!b|!c|!d|!e)' )
        self.assertEqual(cknf1, [19])
        self.assertEqual(cdnf1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])
        self.assertEqual(number_result, 4096)

if __name__ == '__main__':
    unittest.main()