from utils import *

# Конвертация числа с плавающей точкой
def convert_to_floating_point(number: float) -> str:
    integer_part_binary_code = ''
    sing_number = '0' if number > 0 else '1'
    integer_part = int(number)
    fraction_part_binary_code = '' 
    fraction_part = number - integer_part
    while integer_part > 0:
        integer_part_binary_code += str(integer_part % 2)
        integer_part //= 2
    integer_part_binary_code = integer_part_binary_code[::-1]
    while fraction_part != 0:
        fraction_part_binary_code += str(fraction_part * 2)[0]
        fraction_part *= 2
        fraction_part -= int(fraction_part)
    binary_code_point = integer_part_binary_code +'.'+ fraction_part_binary_code
    index_point = binary_code_point.find('.')
    index_first_1 = binary_code_point.find('1')
    mantissa = binary_code_point[1:index_point] + binary_code_point[index_point + 1:]
    stepen = index_point - (index_first_1 + 1)
    exponenta = convert_to_unmarked_code(stepen + ZERO_POINT)
    float_binary_code = sing_number + '.' + exponenta + '.' + mantissa[:MANTISSA_AMT] + '0' * (MANTISSA_AMT - len(mantissa))
    return float_binary_code

# Безнаковое число: 0 - 255 число из 10 -> 2
def convert_to_unmarked_code(number: int) -> str:
    number = abs(number)
    binary_code = ''
    while number > 0:
        binary_code += str(number % 2)
        number //= 2
    binary_code += '0' * (TOTAL_BITS - len(binary_code)) 
    binary_code = binary_code[::-1]
    return binary_code[-8:]

# Обратный код
def convert_to_reverse_code(number: int) -> str:
    binary_code_reverse = ''
    if number > 0:
        binary_code_reverse = convert_to_direct_code(number)
    else:
        binary_code = convert_to_direct_code(number)
        binary_code_reverse = binary_code[0]
        for x in binary_code[1:]:
            binary_code_reverse += '1' if x == '0' else '0'
    return binary_code_reverse

# 2 код -> 10 код
def convert_from_2_to_10(binary_code: str) -> int:
    result = 0
    number = ''
    if binary_code[0] == '0':
        for i in range(len(binary_code)):
            result += int(binary_code[i]) * (2 ** (len(binary_code) - 1 - i))
    else:
        for element in binary_code[0:]:
            number += '1' if element == '0' else '0'
        number = summa_extra_code(number, BINARY_NUMBER_1)
        for i in range(len(number)):
            result += int(number[i]) * (2 ** (len(number) - 1 - i))
        result = result * (-1)
    return result

# Ковертация дробной части бинарного кода
def convert_fraction_part(number: str) -> float:
    print(number)
    fraction_part = 0.0
    for index in range(len(number)):
        fraction_part += float(number[index]) * (2 ** (-(index + 1)))
    return fraction_part

# Конвертация из плавающей точки в float
def convert_to_10_from_floating_point(number: str) -> float:
    exponenta = convert_from_2_to_10('0'+ number[2:10])
    print(exponenta)
    binary_code = float("1." + number[11:]) * (10 ** (abs(exponenta) - 127))
    print(binary_code)
    binary_code = str(binary_code)
    if binary_code.find("."):
        decimal_part_binary_code = '0' + binary_code[:binary_code.find(".")]
        integer_part = convert_from_2_to_10(decimal_part_binary_code)
        fraction_part_binary_code = binary_code[binary_code.find('.') + 1:]
        fraction_part = convert_fraction_part(fraction_part_binary_code)
        return integer_part + fraction_part
    else:
        return convert_from_2_to_10(binary_code)
    
def convertation_to_float(binary_code_point: str) -> float:
    index_point = binary_code_point.find('.')
    index_first_1 = binary_code_point.find('1')
    mantissa = binary_code_point[index_first_1+1:index_point] + binary_code_point[index_point + 1:]
    print(mantissa)
    stepen = index_point - (index_first_1 + 1)
    exponenta = convert_to_unmarked_code(stepen + ZERO_POINT)
    float_binary_code = '0' + '.' + exponenta + '.' + mantissa[:MANTISSA_AMT] + '0' * (MANTISSA_AMT - len(mantissa))
    return float_binary_code
    