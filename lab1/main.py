# from arithmetic_operation_binary_code import *

# def main():
    
#     print("Сложение:")
#     number_1 = int(input("Ввод числа №1: "))
#     print(f"Число введено: {number_1}")
#     print(f"Прямой код: {convert_to_direct_code(number_1)}")
#     print(f"Обратный код: {convert_to_reverse_code(number_1)}")
#     print(f"Дополнительный код: {convert_to_extra_code(number_1)}")

#     number_2 = int(input("Ввод числа №2: "))
#     print(f"Число введено: {number_2}")
#     print(f"Прямой код: {convert_to_direct_code(number_2)}")
#     print(f"Обратный код: {convert_to_reverse_code(number_2)}")
#     print(f"Дополнительный код: {convert_to_extra_code(number_2)}")
    
#     result = summa_extra_code(convert_to_extra_code(number_1), convert_to_extra_code(number_2))
#     print(f"Результат в дополнительном коде: {result}")
#     print(f"Результат: {number_1 + number_2}")
#     print(f"Дополнительный код в число: {convert_from_2_to_10(result)}")

#     print("Вычитание:")
#     result_vyczitanie = substraction_2_numbers(convert_to_extra_code(number_1), convert_to_extra_code(number_2))
#     print(f"Результат в дополнительном коде: {result_vyczitanie}")
#     print(f"Результат: {number_1 - number_2}")
#     print(f"Дополнительный код в число: {convert_from_2_to_10(result_vyczitanie)}")

#     # При умножении потеря знака если в прямом коде

#     print("Умножение:")
#     result_umnozenie = multiplication_extra_code(convert_to_extra_code(number_1), convert_to_extra_code(number_2))
#     print(f"Результат в прямом коде: {result_umnozenie}")
#     print(f"Результат: {number_1 * number_2}")
#     print(f"Пряой код в число: {convert_from_2_to_10(result_umnozenie)}")

#     print("Числа с плавающей точкой")
    
#     number_1p = float(input("Ввод числа №1:"))
#     print(f"Число введено: {number_1p}")
#     print(f"Стандарт с плавающей точкой код: {convert_to_floating_point(number_1p)}")

#     number_2p = float(input("Ввод числа №1:"))
#     print(f"Число введено: {number_2p}")
#     print(f"Стандарт с плавающей точкой код: {convert_to_floating_point(number_2p)}")

#     print("Cумма чисел с плавающей точкой:")
#     result_sum_swim_point = summa_floating_point(convert_to_floating_point(number_1p), convert_to_floating_point(number_2p))
#     print(f"Результат в коде c плавающей точке: {result_sum_swim_point}")
#     print(f"Результат: {number_1p + number_2p}")
#     print(f"Стандарт в число: {(result_sum_swim_point)}")

# if __name__ == "__main__":
#     main()