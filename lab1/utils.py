from constants import *

# Сложение в дополнительном код
def summa_extra_code(binary_code_1: str, binary_code_2: str) -> str:
    digit = '0'
    sum_binary_code = ''
    max_len = max(len(binary_code_1), len(binary_code_2))
    binary_code_1 = binary_code_1.zfill(max_len)[::-1]
    binary_code_2 = binary_code_2.zfill(max_len)[::-1]
    for i in range(max_len):
        if ((binary_code_1[i] == '1' and binary_code_2[i] == '0') or (binary_code_1[i] == '0' and binary_code_2[i] == '1')) and digit == '0':
            sum_binary_code += '1'
        elif ((binary_code_1[i] == '1' and binary_code_2[i] == '0') or (binary_code_1[i] == '0' and binary_code_2[i] == '1')) and digit == '1':
            sum_binary_code += '0'
        elif (binary_code_1[i] == '0' and  binary_code_2[i] == '0') and digit == '1':
            digit = '0'
            sum_binary_code += '1'
        elif (binary_code_1[i] == '0' and  binary_code_2[i] == '0') and digit == '0':
            sum_binary_code += '0'
        elif (binary_code_1[i] == '1' and  binary_code_2[i] == '1') and digit == '0':
            digit = '1'
            sum_binary_code += '0'
        elif (binary_code_1[i] == '1' and  binary_code_2[i] == '1') and digit == '1':
            sum_binary_code += '1'
    sum_binary_code = sum_binary_code[::-1]
    return sum_binary_code

# Дополнительный код -128 - 127 число из 10 -> 2
def convert_to_extra_code(number: int) -> str:
    binary_code_reverse = binary_code_extra =''
    if number > 0:
        binary_code_reverse = convert_to_direct_code(number)
    else:
        binary_code_extra = convert_to_direct_code(number)
        binary_code_reverse = binary_code_extra[0]
        for x in binary_code_extra[1:]:
            binary_code_reverse += '1' if x == '0' else '0'
        binary_code_reverse = summa_extra_code(binary_code_reverse, BINARY_NUMBER_1)
    return binary_code_reverse

# Прямой код -127 - 127 число из 10 -> 2
def convert_to_direct_code(number: int) -> str:
    binary_code = ''
    sing_number = '0' if number > 0 else '1'
    number = abs(number)
    while number > 0:
        binary_code += str(number % 2)
        number //= 2
    binary_code += '0' * (TOTAL_BITS - 1 - len(binary_code)) + sing_number 
    binary_code = binary_code[::-1]
    return binary_code