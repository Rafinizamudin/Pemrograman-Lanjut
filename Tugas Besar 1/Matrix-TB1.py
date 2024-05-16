import re

with open('Matrix-TB1.txt', 'r') as file:
    lines = file.readlines()

first_input = lines[0].rstrip().split()
n = int(first_input[0])
m = int(first_input[1])

matrix = lines[1:]
encoded_list = list(zip(*matrix))
encoded_string = "".join([''.join(item) for item in encoded_list])
pat = r'\b[^a-zA-Z0-9]+\b'
print(re.sub(pat,r' ',encoded_string))