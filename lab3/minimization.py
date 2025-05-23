from typing import List, Set
from prettytable import PrettyTable
from global_perem import *

def redactor_str(logic_say: str) -> str:
    final_str = ''
    for i in range(len(logic_say)):
        if logic_say[i - 1] == '!' and logic_say[i] in VARIABLES:
            final_str += logic_say[i].upper()
            
        elif logic_say[i] == '(':
            final_str += ' '
        elif logic_say[i] in VARIABLES:
            final_str += logic_say[i]
    return final_str.strip()

def choose_both(first: str, second: str) -> str:
    for i in range(len(first)):
        if first[i] != second[i]:
            return first[:i] + first[i + 1:]

def reverse_letter(letter: str) -> str:
    return letter.upper() if letter.islower() else letter.lower()

def refractor(logic_s: List) -> Set:
    result = set()
    for item in logic_s:
        variantes = []
        x = False
        for i in range(len(item)):
            letter_new = reverse_letter(item[i])
            new_item = item
            new_item = new_item.replace(item[i], letter_new)
            variantes.append(new_item)
        for item1 in variantes:
            if item1 in logic_s:
                result.add(choose_both(item,item1))
                x =True
        if x == False:
            result.add(item)
    return result

def formiration_result_cdnf(logic_s: str) -> str:
    final_result = ''
    for item in logic_s:
        result = ''
        result += '('
        for item1 in item:
            if item1.isupper():
                result += '!'
                result += item1.lower()
            elif item1 in VARIABLES:
                result += item1
            if len(item) - 1  > result.count('&'):
                result += '&'
        result += ')'
        if len(logic_s) - 1 > final_result.count('|'):
            result += '|'
        final_result += result
    return final_result


def formiration_result_cknf(logic_s: str) -> str:
    final_result = ''
    for item in logic_s:
        result = ''
        result += '('
        for item1 in item:
            if item1.isupper():
                result += '!'
                result += item1.lower()
            elif item1 in VARIABLES:
                result += item1
            if len(item) - 1  > result.count('|'):
                result += '|'
        result += ')'
        if len(logic_s) - 1 > final_result.count('&'):
            result += '&'
        final_result += result
    return final_result


def table(logic_s, logic_S : str) -> None:
    coverage = set()
    table = PrettyTable()
    table.field_names = [''] + logic_S
    rows = [item for item in logic_s]
    for row in rows:
        if len(coverage) != len(logic_S):
            spis = [row]
            chars = list(row)
            for stolb in logic_S:

                if all(char in stolb for char in chars):
                    spis.append('X')
                    coverage.add(stolb)
                else: 
                    spis.append('')
            table.add_row([item for item in spis])
    print(table)

def minimization_cknf(logic_s: str) -> str:
    logic_s = logic_S = redactor_str(logic_s).split(' ')
    for _ in range(len(logic_s[0]) - 1):
        logic_s = refractor(logic_s)
        print(logic_s)
    result = formiration_result_cknf(logic_s)
    print(result)
    table(logic_s, logic_S)
    return result

def minimization_cdnf(logic_s: str) -> str:
    logic_s =logic_S = redactor_str(logic_s).split(' ')
    for _ in range(len(logic_s[0]) - 1):
        logic_s = refractor(logic_s)
        print(logic_s)
    result = formiration_result_cdnf(logic_s)
    print(result)
    table(logic_s, logic_S)
    return result