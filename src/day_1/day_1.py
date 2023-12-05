import string

number_list = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

def translate(line):
    for num, name in enumerate(number_list):
        line = line.replace(name, f'{name}{num}{name}')

    translation_table = str.maketrans("", "", string.ascii_letters)

    new_line = line.translate(translation_table)

    return new_line


# Example usage
sum_list = []

with open('input.txt', 'r') as file:
    for line in file:
        new_line = translate(line)
        right_ptr = len(new_line) - 1
        left_ptr = 0

        for ch in new_line:
            if new_line[left_ptr].isdigit():
                leftmost_num = new_line[left_ptr]
            else:
                left_ptr += 1

            if new_line[right_ptr].isdigit():
                rightmost_num = new_line[right_ptr]
            else:
                right_ptr -= 1

        alpha_num = int(leftmost_num + rightmost_num)
        sum_list.append(alpha_num)

print(sum(sum_list))