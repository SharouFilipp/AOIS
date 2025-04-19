from fromiration_table_true import *
from minimization import *

# !((a|b)->!c)

def main():

    logic_say = input("Введите логическое высказывание \n").lower()
    variables_amount = make_list_posible_values(logic_say)
    print(make_priority(logic_say))
    result(make_priority(logic_say))
    table_true(variables_amount)

    print(result(make_priority(logic_say)))

    cdnf_value = cdnf(variables_amount)
    cknf_value = cknf(variables_amount)
    
    
    result_value = get_result_of_table_true()
    print("Индексная форма: ", convert_from_2_to_10(("").join(result_value)))

    if cknf_value != '':
        print(cknf(variables_amount), 'ggg')
        number_2 = number_cknf(variables_amount)
        print(number_2)
        print('Минимизированная скнф')
        minimization_cknf(cknf(variables_amount))
    else:
        print("Отсутствует скнф")
    if cdnf_value != '':
        print(cdnf(variables_amount))
        number_1 = number_cdnf(variables_amount)
        print(number_1)
        print('Минимизированная сднф')
        minimization_cdnf(cdnf(variables_amount))
    else:
        print("Отсутствует сднф")

if __name__ == "__main__":
    main()