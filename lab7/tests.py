import unittest
from typing import List
from unittest.mock import patch
from io import StringIO
from matrix import *

class TestMatrixFunctions(unittest.TestCase):
    def setUp(self):
        """Инициализация тестовой матрицы и данных."""
        self.size = 16
        self.matrix = create_table(self.size)
        self.valid_word = "0101010101010101"
        self.valid_key = "101"

    # Тесты для create_table
    def test_create_table_correct_size(self):
        """Проверка создания матрицы 16x16 с шахматным узором."""
        matrix = create_table()
        self.assertEqual(len(matrix), 16)
        self.assertEqual(len(matrix[0]), 16)
        self.assertEqual(matrix[0][0], 0)
        self.assertEqual(matrix[0][1], 1)
        self.assertEqual(matrix[1][0], 1)
        self.assertEqual(matrix[1][1], 0)


    # Тесты для logic_operation
    def test_logic_operation_case_1(self):
        """Проверка case '1' возвращает '0'."""
        result = logic_operation('1', self.valid_word, 0, self.matrix)
        self.assertEqual(result, '0')

    def test_logic_operation_case_2(self):
        """Проверка case '2' возвращает исходное слово."""
        result = logic_operation('2', self.valid_word, 0, self.matrix)
        self.assertEqual(result, self.valid_word)

    def test_logic_operation_case_3(self):
        """Проверка case '3' инвертирует столбец и слово."""
        matrix = [[0 for _ in range(16)] for _ in range(16)]
        word = find_word(0, matrix)
        result = logic_operation('3', word, 0, matrix)
        
        self.assertEqual(result, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        for i in range(16):
            self.assertEqual(matrix[i][0], 1)

    def test_logic_operation_case_4(self):
        """Проверка case '4' возвращает '1'."""
        result = logic_operation('4', self.valid_word, 0, self.matrix)
        self.assertEqual(result, '1')


    def test_logic_operation_invalid_number(self):
        """Проверка обработки некорректного number."""
        with self.assertRaises(IndexError):
            logic_operation('3', self.valid_word, 16, self.matrix)


    # Тесты для find_word
    def test_find_word_valid_number(self):
        """Проверка find_word с корректным number."""
        result = find_word(2, self.matrix)
        self.assertEqual(len(result), 16)
        self.assertEqual(result[0], self.matrix[2][2])

    def test_find_word_edge_cases(self):
        """Проверка find_word на граничных значениях number."""
        result_0 = find_word(0, self.matrix)
        self.assertEqual(len(result_0), 16)
        result_15 = find_word(15, self.matrix)
        self.assertEqual(len(result_15), 16)

    def test_find_word_invalid_number(self):
        """Проверка find_word с некорректным number."""
        with self.assertRaises(IndexError):
            find_word(16, self.matrix)



    # Тесты для compare_bits
    def test_compare_bits_single_word(self):
        """Проверка compare_bits с одним словом."""
        result, max_matches = compare_bits("101", ["101"])
        self.assertEqual(max_matches, 3)
        self.assertEqual(result, [("101", 0, 1)])

    def test_compare_bits_multiple_words(self):
        """Проверка compare_bits с несколькими словами."""
        words = ["101", "111", "000"]
        result, max_matches = compare_bits("101", words)
        self.assertEqual(max_matches, 3)
        self.assertEqual(result, [("101", 0, 1)])

    def test_compare_bits_no_matches(self):
        """Проверка compare_bits с несовпадающими словами."""
        result, max_matches = compare_bits("111", ["000"])
        self.assertEqual(max_matches, 0)
        self.assertEqual(result, [("000", 0, 0)])

    def test_compare_bits_empty_words(self):
        """Проверка compare_bits с пустым списком слов."""
        with self.assertRaises(ValueError):
            compare_bits("101", [])

    def test_compare_bits_invalid_input(self):
        """Проверка compare_bits с некорректными данными."""
        with self.assertRaises(ValueError):
            compare_bits("abc", ["101"])
        with self.assertRaises(ValueError):
            compare_bits("101", ["abc"])

    # Тесты для find_adres_word
    def test_find_adres_word_valid_number(self):
        """Проверка find_adres_word с корректным number."""
        result = find_adres_word(2, self.matrix)
        self.assertEqual(result[0], self.matrix[2][0])
        self.assertEqual(result[14], self.matrix[0][14])

    # Тесты для print_table
    @patch('sys.stdout', new_callable=StringIO)
    def test_print_table(self, mock_stdout):
        """Проверка вывода print_table."""
        small_matrix = [[0, 1], [1, 0]]
        print_table(small_matrix)
        output = mock_stdout.getvalue().strip()
        self.assertIn("[0, 1]", output)
        self.assertIn("[1, 0]", output)

    def test_print_table_empty_matrix(self):
        """Проверка print_table с пустой матрицей."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            print_table([])
            self.assertEqual(mock_stdout.getvalue(), "")

    # Тесты для summa
    @patch('sys.stdout', new_callable=StringIO)
    def test_summa_valid_key(self, mock_stdout):
        """Проверка summa с ключом, который есть в матрице."""
        matrix = create_table()
        summa("101", matrix)

    @patch('sys.stdout', new_callable=StringIO)
    def test_summa_invalid_key(self, mock_stdout):
        """Проверка summa с ключом, которого нет."""
        matrix = create_table()
        matrix_copy = [row[:] for row in matrix]
        summa("999", matrix)
        self.assertEqual(mock_stdout.getvalue(), "")
        self.assertEqual(matrix, matrix_copy)

    def test_show_matrix_invalid_row_length(self):
        """Проверка show_matrix с некорректной длиной строки."""
        matrix = [[0, 1], [1]]
        with self.assertRaises(ValueError):
            show_matrix(matrix)

    # Тесты для summa_extra_code
    def test_summa_extra_code_valid(self):
        """Проверка summa_extra_code с корректными входными данными."""
        self.assertEqual(summa_extra_code("1010", "0101"), "01111")
        self.assertEqual(summa_extra_code("0000", "0000"), "00000")
        self.assertEqual(summa_extra_code("1111", "1111"), "11110")

    def test_summa_extra_code_different_lengths(self):
        """Проверка summa_extra_code с разной длиной строк."""
        self.assertEqual(summa_extra_code("10", "1010"), "01100")


if __name__ == '__main__':
    unittest.main()