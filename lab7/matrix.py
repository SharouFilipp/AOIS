from random import randint
from typing import List
from prettytable import PrettyTable

SIZE = 16


def create_table(size: int = 16) -> List[List[int]]:
    return [[(i + j) % 2 for j in range(size)] for i in range(size)]


# def create_table() -> List[List[int]]:
#     return [[randint(0,1) for _ in range(SIZE)] for _ in range(SIZE)]

def logic_operation(choose: str, word: str, number: int, matrix: List[List[int]] ) -> str:
    match choose:
        case '1':
            return '0'
        case '2':
            return word            
        case '3':
            for i in range(len(matrix)):
                matrix[i][number] = 0 if matrix[i][number] == 1 else 1
            return [0 if item == 1 else 1 for item in word]
        case '4':
            return '1'
        
def find_word(number :int, matrix : List[List[int]]) -> str:
    result = []
    for item in range(number, SIZE): 
        result.append(matrix[item][number])
    for item in range(number):
        result.append(matrix[item][number])
    return result

def compare_bits(search_arg: str, words: str) -> str:
    n = len(search_arg) 
    matches = []  
    for j, word in enumerate(words):
        g_j_i_plus_1 = 0
        l_j_i_plus_1 = 0
        match_count = 0 

        for i in range(n - 1, -1, -1):
            a_i = int(search_arg[i]) 
            s_j_i = int(word[i])   

            g_j_i = g_j_i_plus_1 or ((not a_i) and s_j_i and (not l_j_i_plus_1))
            l_j_i = l_j_i_plus_1 or (a_i and s_j_i and (not g_j_i_plus_1))

            g_j_i_plus_1 = g_j_i
            l_j_i_plus_1 = l_j_i

            if a_i == s_j_i:
                match_count += 1

        matches.append((word, match_count, g_j_i, l_j_i))

    max_matches = max(match_count for _, match_count, _, _ in matches)
    result = [(word, g, l) for word, match_count, g, l in matches if match_count == max_matches]

    return result, max_matches

def find_adres_word(number :int, matrix : List[List[int]]) -> str:
    result = []
    position = 0
    for item in range(number, SIZE): 
            result.append(matrix[item][position])
            position +=1
    position = 0
    for item in range(SIZE - number, SIZE): 
            result.append(matrix[position][item])
            position +=1
    return result
                    
def print_table(matrix: List):
    for item in matrix:
        print(item)

def summa(key: str, matrix: List[List[int]]):
    all_words = []
    for i in range(SIZE):
        all_words.append(''.join(str(num) for num in find_word(i, matrix)))

    for i in range(len(all_words)):
        if all_words[i][0:3] == key:
            part_A = all_words[i][3:7]
            part_B = all_words[i][7:11]
            part_S = summa_extra_code(part_A,part_B)
            all_words[i] = all_words[i][0:11] + part_S
            new_word = all_words[i][SIZE-i:] + all_words[i][0:SIZE-i]
            new_word = [int(item) for item in new_word]
            for y in range(len(matrix)):
                matrix[y][i] = new_word[y]
            print(all_words[i])

def show_matrix(table: List[List[int]]):
    pt = PrettyTable()

    pt.field_names = [""] + [str(i) for i in range(SIZE)]

    for i, row in enumerate(table):
        pt.add_row([str(i)] + row)

    pt.header = True
    pt.border = True
    pt.hrules = True  
    pt.vrules = True 
    pt.align = 'c'    
    pt.padding_width = 1  
    
    print(pt)

def summa_extra_code(binary_code_1: str, binary_code_2: str) -> str:
    digit = '0'
    sum_binary_code = ''
    max_len = 5
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
    