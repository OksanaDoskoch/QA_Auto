import unittest

from lesson_09.homeworks import calculate_average, reverse_string, find_longest_word, sum_of_even_numbers, extract_string

class MyTest(unittest.TestCase):
     #середнє значення чисел
    def test_average_positive(self):
        result = calculate_average([4, 6, 8])
        self.assertEqual(result, 6)

    def test_average_negative(self):
        result = calculate_average([4, 6, 8])
        self.assertNotEqual(result, 2)

    #рядок в зворотньому порядку
    def test_reverse(self):
        my_string = "Some interesting text "
        result = reverse_string(my_string)
        self.assertEqual(result, " txet gnitseretni emoS")

    def test_reverse_negative(self):
        my_string = "Some interesting text "
        result = reverse_string(my_string)
        self.assertNotEqual(result, "txet gnitseretni emoS") #пропущено пробіл

    #найдовше слово у списку
    def test_find_longest_word(self):
        words = ["yellow", "green", "cherry", "white-white", "light-brown"]
        result = find_longest_word(words)
        self.assertEqual(result, "white-white")

    #негативний кейс: ValueError коли список порожній
    def test_longest_word_empty_list(self):
        with self.assertRaises(ValueError):
            find_longest_word([])

    # сума парних чисел у списку
    def test_sum(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]
        result = sum_of_even_numbers(numbers)
        self.assertEqual(result, 130)

    def test_sum_negative(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]
        result = sum_of_even_numbers(numbers)
        self.assertNotEqual(result, 30)

    #список лише з рядковими (str) елементами з вхідного списку
    def test_extract_string(self):
        lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8]
        result = extract_string(lst1)
        self.assertEqual(result, ['1', '2', 'False', '6'])

    def test_extract_string_negative(self):
        lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8,]
        result = extract_string(lst1)
        self.assertNotEqual(result, ['1', '2', True, 'False', '6'])

if __name__ == "__main__":
    unittest.main()