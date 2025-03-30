
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,100]

sum_of_even_numbers = sum(number for number in list_of_numbers if number % 2 == 0)
print(sum_of_even_numbers)