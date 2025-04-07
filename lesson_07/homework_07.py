# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 10:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_two_numbers(num1, num2):
    return num1 + num2

my_sum = sum_two_numbers(138, 90)
print(my_sum)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

numbers = [4, 6, 8]
average = calculate_average(numbers)
print(average)


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(original_string):
    return original_string[::-1]

my_string = " Some interesting text"
reversed_string = reverse_string(my_string)
print(reversed_string)

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def find_longest_word(word_list):
    return max(word_list, key=len)

words = ["yellow", "green", "cherry", "white-white", "light-brown"]
longest_word = find_longest_word(words)
print(longest_word)

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    if str2 in str1:
        return str1.find(str2)
    else:
        return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
#функція повертає список лише з рядковими (str) елементами з вхідного списку

def extract_string(some_list):
    return [item for item in lst1 if isinstance(item, str)]

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
print(extract_string(lst1))


# task 8

def sum_of_even_numbers(numbers):
    return sum(number for number in list_of_numbers if number % 2 == 0) #функція рахує суму усіх парних чисел в списку

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,100]
print(sum_of_even_numbers(list_of_numbers))

# task 9
#функція рахує кількість унікальних символів в строці (input)
def check_unique_chars(user_input):
    unique_chars = set(user_input)
    return len(unique_chars) > 10 #Якщо їх більше 10 - виведе True, інакше - False.

user_input = input("Custom string: ")

print(check_unique_chars(user_input))

# task 10

def count_letter_in_text(text, letter):
    return text.count(letter) # Виведе, скількі разів у тексті зустрічається певна літера

adwentures_of_tom_sawer = "Tom gave up the brush with reluctance in his .... face but alacrity in his heart."

number_of_letters = count_letter_in_text(adwentures_of_tom_sawer, "h")
print(number_of_letters)


"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""