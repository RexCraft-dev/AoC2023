data = []
nums = []
symbols = list('!@#$%^&*()_+}{[]|\?/><,;:`~')


def find_symbols(lst):
    for i in lst:
        if i in symbols:
            return True
    return False


with open('input_test.txt', 'r') as file:
    for line in file:
        data.append(line.strip('\n'))

i = 0

while i < len(data):
    current_num = ''
    is_counted = False
    check_lst = []
    k = 0

    print(data[i])

    while k < len(data[i]):
        current_num = ''
        is_counted = False

        if i == 0:
            if data[i][k].isdigit():
                while k < len(data[i]) and data[i][k].isdigit():
                    current_num += data[i][k]
                    if k > 0:
                        check_lst.append(data[i][k-1])
                    if k < len(data[i]):
                        check_lst.append(data[i][k+1])
                    k += 1

                is_counted = find_symbols(check_lst)

                if is_counted:
                    nums.append(current_num)

                current_num = ''
                check_lst = []

        elif i == len(data) - 1:
            if k < len(data[i]) and data[i][k].isdigit():
                if k == 0:
                    check_lst.append(data[i - 1][k])
                    print(check_lst)
                else:
                    while k < len(data[i]) and data[i][k].isdigit():
                        current_num += data[i][k]
                        check_lst.append(data[i - 1][k])
                        check_lst.append(data[i][k-1])
                        k += 1
                    if k + 1 < len(data[i]):
                        check_lst.append(data[i - 1][k + 1])
                        check_lst.append(data[i][k + 1])

                    is_counted = find_symbols(check_lst)

                    if is_counted and current_num != '':
                        print(f'Current number appended: {current_num}')
                        nums.append(current_num)
                    current_num = ''
                    check_lst = []

        else:
            while data[i][k].isdigit():
                if k > 0 and k < len(data[i]) - 1:
                    check_lst.append(data[i][k-1])
                    check_lst.append(data[i-1][k-1])
                    check_lst.append(data[i+1][k-1])
                    check_lst.append(data[i-1][k+1])
                    check_lst.append(data[i+1][k+1])
                else:
                    check_lst.append(data[i-1][k])
                    check_lst.append(data[i+1][k])
                k += 1

                print(current_num)

            is_counted = find_symbols(check_lst)

            if is_counted and current_num != '':
                print(f'Current number appended: {current_num}')
                nums.append(current_num)
            current_num = ''
            check_lst = []
        k += 1
    i += 1

filtered_list = [int(item) for item in nums if item != '']

print(filtered_list)
print(sum(filtered_list))
