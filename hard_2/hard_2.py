def short_pal(s):
    rev_s = s[::-1]
    for i in range(len(s) + 1):
        if s.startswith(rev_s[i:]):
            return rev_s[:i] + s

a = input("Enter a string: ")

result = short_pal(a)
print(f"The shortest palindrome is:",result)
