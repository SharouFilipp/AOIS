from utils import *
from binary_code_convertation import *

# Умножение дополнительный код
def multiplication_extra_code(binary_code_1: str, binary_code_2: str) -> str:
    list_binary_numbers_to_sum = []
    multiplication_binary_code = ''
    for index_2 in range(len(binary_code_2) - 1,-1,-1):
        component = ''
        for index_1 in range(len(binary_code_1) - 1,-1,-1):
            component += '1' if binary_code_2[index_2] == '1' == binary_code_1[index_1] else '0'
        component = component[::-1]
        component += '0' * (TOTAL_BITS - index_2 - 1)
        list_binary_numbers_to_sum.append(component)     
    for index_2 in range(len(list_binary_numbers_to_sum)):
        multiplication_binary_code = summa_extra_code(multiplication_binary_code,list_binary_numbers_to_sum[index_2])
    return multiplication_binary_code[-TOTAL_BITS::]

# Вычитание
def substraction_2_numbers(binary_code_1: str, binary_code_2: str)  -> str:
    number = convert_from_2_to_10('0'+binary_code_2) 

    negative_binary_code_2 = convert_to_extra_code(number * -1)
    return summa_extra_code(binary_code_1, negative_binary_code_2)


# Сумма с плавающей точкой
def summa_floating_point(binary_code1: str, binary_code2: str) -> str:
    exponent1_binary, mantissa1_binary =  binary_code1[2:10], binary_code1[11:]
    exponent2_binary, mantissa2_binary =  binary_code2[2:10], binary_code2[11:]
    exponent1 = convert_from_2_to_10('0' + exponent1_binary)
    exponent2 = convert_from_2_to_10('0' + exponent2_binary)
    
    mantissa1_binary = '1' + mantissa1_binary  
    mantissa2_binary = '1' + mantissa2_binary  
    if exponent1 > exponent2:
        mantissa2_binary =  '0' * (exponent1 - exponent2) + mantissa2_binary
        exponent2 = exponent1
    else:
        mantissa1_binary = '0' * (exponent2 - exponent1) + mantissa1_binary 
        exponent1 = exponent2
    mantissa_sum = summa_extra_code(mantissa1_binary[0:24],mantissa2_binary[0:24])
    
    if len(mantissa_sum) > MANTISSA_AMT :
        mantissa_sum = mantissa_sum[1:] 
        exponent1 += 1  
    result_sign = '0'  
    result_exponent = convert_to_unmarked_code(exponent1)
    result_mantissa = mantissa_sum[1:MANTISSA_AMT + 1] + '0' * (MANTISSA_AMT - len(mantissa_sum) + 1)
    return result_sign + '.' + result_exponent + '.' + result_mantissa


def divide_binary_code(binary_code1: str, binary_code2: str) -> float:
    binary_code1 = binary_code1[binary_code1.find('1'):]
    binary_code2 = binary_code2[binary_code2.find('1'):]
    if binary_code2 == "0":
        raise ValueError("Деление на ноль невозможно.")
    number = 0
    integer_part = ""
    drob_part = ""
    for bit in binary_code1:
        drob_part += bit
        if len(drob_part) > len(binary_code2) or (len(drob_part) == len(binary_code2) and drob_part >= binary_code2):
            integer_part += "1"
            drob_part = substraction_2_numbers(drob_part, binary_code2)
            number = convert_from_2_to_10('0' + drob_part) 
            drob_part = convert_to_unmarked_code(number)
        else:
            integer_part += "0"
        drob_part = drob_part[drob_part.find('1')::]    
    return convertation_to_float(integer_part[1:] +'.'+ drob_part)