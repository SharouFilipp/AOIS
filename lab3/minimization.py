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

def vybor_both(first: str, second: str) -> str:
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
                result.add(vybor_both(item,item1))
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


# def table(logic_s, logic_S : str) -> None:

#     table = PrettyTable()
#     table.field_names = [''] + logic_S
#     rows = [item for item in logic_s]
#     # print(logic_S, 'gggggggggggggggggggggg')
#     for row in rows:
#         spis = [row]
#         chars = list(row)
#         for stolb in logic_S:
#             if all(char in stolb for char in chars):
#                 spis.append('X')
#             else: 
#                 spis.append('')
#         table.add_row([item for item in spis])
#     print(table)

    
    


def table(logic_s, logic_S):
    
    coverage = {}
    
    for imp in logic_s:
        covered = []
        
        for m in logic_S:
           
            match = True
            for i in range(len(imp)):
                if imp not in m:
                    match = False
                    break
            if match:
                covered.append(m)
        coverage[imp] = covered
    
    remaining_minterms = set(logic_S)
    essential_implicants = []

    while remaining_minterms:
        best_imp = None
        max_covered = 0
        for imp in coverage:
            current_covered = set(coverage[imp]) & remaining_minterms
            if len(current_covered) > max_covered:
                max_covered = len(current_covered)
                best_imp = imp

        if not best_imp:
            break  

        essential_implicants.append(best_imp)
        remaining_minterms -= set(coverage[best_imp])

    table = PrettyTable()
    table.field_names = [''] + logic_S

    for imp in essential_implicants:
        row = [imp]
        for m in logic_S:
            row.append('X' if m in coverage[imp] else '')
        table.add_row(row)

    print(table)

def minimization_cknf(logic_s: str) -> None:
    logic_s =logic_S= redactor_str(logic_s).split(' ')
    for _ in range(len(logic_s[0]) - 1):
        logic_s = refractor(logic_s)
        print(logic_s)
    print(formiration_result_cknf(logic_s))
    table(logic_s, logic_S)

def minimization_cdnf(logic_s: str) -> None:
    logic_s =logic_S= redactor_str(logic_s).split(' ')
    for _ in range(len(logic_s[0]) - 1):
        logic_s = refractor(logic_s)
        print(logic_s)
    print(formiration_result_cdnf(logic_s))
    table(logic_s, logic_S)