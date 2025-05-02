"""  Функція, яка розрахує середнє арифметичне списку чисел.
"""
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

"""  Функція, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(original_string):
    return original_string[::-1]

"""  Функція, яка приймає список слів та повертає найдовше слово у списку.
"""
def find_longest_word(word_list):
    return max(word_list, key=len)

"""функція рахує суму усіх парних чисел в списку"""
def sum_of_even_numbers(numbers):
    return sum(number for number in numbers if number % 2 == 0)

""" Функція повертає список лише з рядковими (str) елементами з вхідного списку"""

def extract_string(some_list):
    return [item for item in some_list if isinstance(item, str)]
