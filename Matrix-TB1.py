import re

def decode_matrix_script(file_name):
    with open(file_name, 'r') as file:
        data = file.readlines()

    first_line = data[0].strip().split()
    n = int(first_line[0])
    m = int(first_line[1])

    matrix = data[1:]
    decoded_matrix = [''.join(col) for col in zip(*matrix)]
    decoded_string = ''.join(decoded_matrix)

    decoded_result = re.sub(r'\b[^a-zA-Z0-9]+\b', r' ', decoded_string)

    return decoded_result

decoded_result = decode_matrix_script('Matrix-TB1.txt')
print(decoded_result)