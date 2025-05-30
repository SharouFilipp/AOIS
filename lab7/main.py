from matrix import *

vybor = input('''
1 - Найти слово;
2 - Логические операции;
3 - Арифметичесские операции над полями слов;
4 - Поисковые операции при помощи g и l;
5 - вывод матрицы;
6 - поиск адресного столбца;
0 - выход\n''')
matrix = create_table() 
while vybor != '0':
    
    match vybor:
        case '1':
            number = int(input('Номер слова:\n'))
            print(find_word(number, matrix))
        case '2':
            number = int(input('Номер слова:\n'))
            word = find_word(number, matrix)
            number2 = input('''Выберите номер операции:\n1 - f0;\n2 - f5;\n3 - f10;\n4 - f15\n''')
            print(word)
            print(logic_operation(number2, word, number, matrix))
        case '3':
            key = input('Введите ключ\n')
            summa(key, matrix)
        case '4':
            compare_word = input("Введите слово")
            words = []
            for i in range(16):
                words.append(find_word(i, matrix))

            result, max_matches = compare_bits(compare_word, words)
            # Вывод результатов
            print(f"Поисковый аргумент: {compare_word}")
            print(f"Максимальное количество совпадений: {max_matches}")
            print("Слова с максимальным совпадением и их состояния (g, l):")
            for word, g, l in result:
                if g == 0 and l == 0:
                    relation = "="
                elif g == 1 and l == 0:
                    relation = ">"
                elif g == 0 and l == 1:
                    relation = "<"
                else:
                    relation = "невозможно"
                print(f"Слово: {word}, g={g}, l={l}, отношение: {word} {relation} {compare_word}")
        case '5':
            for item in matrix:
                print(item)

            show_matrix(matrix)
        case '6':
            number = int(input('Номер слова:\n'))
            print(find_adres_word(number, matrix))
    vybor = input('''
1 - Найти слово;
2 - Логические операции;
3 - Арифметичесские операции над полями слов;
4 - Поисковые операции при помощи g и l;
5 - вывод матрицы;
6 - поиск адресного столбца;
0 - выход\n''')