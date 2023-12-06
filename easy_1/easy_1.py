def len_of_last_word(s):
    words = s.split()

    if not words:
        return 0

    return len(words[-1])

a = input("Enter a string: ")

result = len_of_last_word(a)
print(f"The length of the last word is: {result}")
