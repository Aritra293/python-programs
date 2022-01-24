#Program to find palindromes in
#a list of strings.

my_list = ["arora", "pop", "toto", "practice", "aa"]

result = list(filter(lambda x: (x == "".join(reversed(x))), my_list))

print(result)
