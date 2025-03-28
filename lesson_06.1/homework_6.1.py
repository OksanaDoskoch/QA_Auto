user_input = input("Custom string: ")

char_count = {}
for char in list(user_input):
    char_count[char] = char_count.get(char, 0) + 1

print(len(char_count) > 10)