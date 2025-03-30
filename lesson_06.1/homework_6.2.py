
while True:
    user_input = input("Please enter a word that contains the letter 'h':").lower()

    if "h" in user_input:
        print("Yes, that's correct!")
        break
    else:
        print("Try one more time")