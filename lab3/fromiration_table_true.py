from logic_operation import *
import itertools

def make_list_posible_values(logic_say: str) -> int:
    variables_amount = 0
    logic_say = logic_say.replace('->', '>')
    list_of_variables = []
    for element in logic_say:
        if element in VARIABLES:
            list_of_variables.append(element)
            variables_amount += 1
    
    combinations_znaczenii = list()
    combinations = list(itertools.product('01', repeat=variables_amount))
    for combination in combinations:
        combinations_znaczenii.append(''.join(combination))

    for i in range(len(list_of_variables)):
        values = list()
        for element in combinations_znaczenii:
            values.append(element[i])
        all_values[list_of_variables[i]] = values
    return variables_amount

def priority(op: str) -> int:
    if op in ('~'):
        return 2
    elif op in ('>'):
        return 3
    elif op in ('|'):
        return 4
    elif op in ('&'):
        return 5
    elif op in ('!'):
        return 6
    elif op == '(':
        return 1
    return 0

def make_priority(logic_say: str) -> str:    
    output = []
    operators = []

    for char in logic_say:
        if char.isalpha():
            output.append(char)
        elif char == '(':
            operators.append(char)
        elif char == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            operators.pop() 
        elif char in ('!', '&', '|', '~', '>'):
            while (operators and
                   priority(operators[-1]) >= priority(char)):
                output.append(operators.pop())
            operators.append(char)

    while operators:
        output.append(operators.pop())
    out_logic_say = ''.join(output)
    return out_logic_say

def result(logic_say: str)-> Dict:
    stack = []
    for ss in logic_say:
        if ss.isalpha():
            stack.append(ss)
        else:
            if ss == '&':
                op1 = all_values[stack.pop()]
                op2 = all_values[stack.pop()]
                res = konukcia(op1,op2)
            elif ss == '!':
                op1 = all_values[stack.pop()]
                op2 = None
                res = substact(op1)
            elif ss == '|':
                op1 = all_values[stack.pop()]
                op2 = all_values[stack.pop()]
                res = nekonukcia(op1,op2)
            elif ss == '~':
                op1 = all_values[stack.pop()]
                op2 = all_values[stack.pop()]
                res = ekvivalent(op1,op2)
            elif ss == '>':
                op1 = all_values[stack.pop()]
                op2 = all_values[stack.pop()]
                res = implication(op1,op2)
            if op2 == None:
                all_values[get_name_to_base(ss, op1)] = res
                stack.append(get_name_to_base(ss, op1))
            else:
                all_values[get_name_to_base(ss, op1, op2)] = res
                stack.append(get_name_to_base(ss, op1, op2))
    return res