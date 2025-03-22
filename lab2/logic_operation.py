from utils import *

# отрицание
def substact(variable1: str) -> List:
    result = []
    for i in range(len(variable1)):
        if variable1[i] == '0':
            result.append('1')
        else:
            result.append('0')    
    return result

# импликация
def implication(variable1, variable2: str) -> List:
    result = []
    for i in range(len(variable1)):
        if (variable2[i] == '1' and variable1[i] == '0' ):
            result.append('0')
        else:
            result.append('1')    
    return result

# конюкция
def konukcia(variable1, variable2 : str) -> List:
    result = [] 
    for i in range(len(variable1)):
        if variable2[i] == variable1[i] == '1':
            result.append('1')
        else:
            result.append('0')    
    return result

# Функция эквивалентности
def ekvivalent(variable1, variable2: str) -> List:
    result = []
    for i in range(len(variable1)):
        if variable2[i] == variable1[i]:
            result.append('1')
        else:
            result.append('0')    
    return result

# дизюнкция
def nekonukcia(variable1, variable2: str) -> List:
    result = []
    for i in range(len(variable1)):
        if variable2[i] == '1'  or variable1[i] == '1':
            result.append('1')
        else:
            result.append('0')    
    return result

# СКНФ
def cknf(variables_amount: Dict) -> str:
    list_of_variables()
    line = ''
    last_key = list(all_values.keys())[-1] 
    result_value = all_values[last_key]
    for i in range(2**variables_amount):
        if result_value[i] == '0':
            counter = 0
            line += '('
            for element in variable_values:
                if all_values[element][i] == '0':
                    line += element
                else:
                    line += ('!' + element)
                if len(variable_values) - 1 > counter:
                    line += '|'
                    counter += 1
            line += ')&'
    return line[:-1]

# СДНФ
def cdnf(variables_amount: Dict) -> str:
    list_of_variables()
    line = ''
    last_key = list(all_values.keys())[-1]  
    result_value = all_values[last_key]
    for i in range(2**variables_amount):
        if result_value[i] == '1':
            counter = 0
            line += '('
            for element in variable_values:
                if all_values[element][i] == '1':
                    line += element
                else:
                    line += ('!' + element)
                if len(variable_values) - 1 > counter:
                    line += '&'
                    counter += 1
            line += ')|'
    return line[:-1]