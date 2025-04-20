array_with_strings = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

# Функція для обчислення суми чисел
def sum_of_numbers(line_with_numbers):
    try:
        numbers = line_with_numbers.split(",")
        # Перетворити кожен символ на число і порахувати суму
        total = sum(int(num) for num in numbers)
        return total
    except ValueError:
        return "Не можу це зробити"

# Обробка кожного елементу в списку
for item in array_with_strings:
    result = sum_of_numbers(item)
    print(result)