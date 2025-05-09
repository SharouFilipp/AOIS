from prettytable import PrettyTable
from global_perem import *
from typing import List, Dict

def table_true(variables_amount: int) -> None:
    table = PrettyTable()
    table.field_names = list(all_values.keys())
    for i in range(2**variables_amount):
        row = [all_values[col][i] for col in table.field_names]
        table.add_row(row)
    print(table)

def get_key(value: List) -> str:
    for element in all_values:
        if all_values[element] == value:
            return element

def get_name_to_base(*args: str) -> None:
    if len(args) == 2:
        stroka = '!'+ get_key(args[1])
    else:
        stroka = get_key(args[2]) + args[0] + get_key(args[1])
    return stroka

def get_result_of_table_true() -> List:
    last_key = list(all_values.keys())[-1]  
    result_value = all_values[last_key]
    return result_value

def list_of_variables() -> Dict:
    for element in all_values:
        if element in VARIABLES:
            variable_values[element] = all_values[element]

def convert_from_2_to_10(binary_code: str) -> int:
    result = 0
    for bit in range(len(binary_code)):
        result += int(binary_code[bit]) * (2 ** (len(binary_code) - 1 - bit))
    return result

def number_cdnf(variables_amount: Dict) -> List:
    result_value = get_result_of_table_true()
    list_of_variables()
    result = []
    for i in range(2**variables_amount):
        line= ''
        if result_value[i] == '1':
            for element in variable_values:
                line += variable_values[element][i]
            number = convert_from_2_to_10(line)
            result.append(number)
    return result
    

def number_cknf(variables_amount: Dict) -> List:
    result_value = get_result_of_table_true()
    list_of_variables()
    result = []
    for i in range(2**variables_amount):
        line= ''
        if result_value[i] == '0':
            for element in variable_values:
                line += variable_values[element][i]
            number = convert_from_2_to_10(line)
            result.append(number)
    return result