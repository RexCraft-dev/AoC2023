data = []
nums = []
symbols = list('&*#/@$%+-=')
total_sum = 0


def find_symbols(lst):
    for i in lst:
        if i in symbols:
            return True
    return False


with open('input.txt', 'r') as file:
    for line in file:
        data.append(line.strip('\n'))

i = 0

while i < len(data):
    current_num = ''
    is_counted = False
    check_lst = []
    k = 0

    while k < len(data[i]):
        current_num = ''
        is_counted = False

        if i == 0:
            if data[i][k].isdigit():
                while k < len(data[i]) and data[i][k].isdigit():
                    current_num += data[i][k]
                    check_lst.append(data[i+1][k])
                    if k > 0 and k+1 < len(data[i]):
                        check_lst.append(data[i][k-1])
                        check_lst.append(data[i][k+1])
                        check_lst.append(data[i+1][k+1])
                        check_lst.append(data[i+1][k-1])
                    else:
                        check_lst.append(data[i+1][k])
                    k += 1

                is_counted = find_symbols(check_lst)

                if is_counted:
                    total_sum += int(current_num)

                current_num = ''
                check_lst = []

        elif i == len(data) - 1:
            if k < len(data[i]) and data[i][k].isdigit():
                if k == 0:
                    current_num += data[i][k]
                    check_lst.append(data[i - 1][k])
                else:
                    while k < len(data[i]) and data[i][k].isdigit():
                        if k == len(data[i])-1:
                            current_num += data[i][k]
                            check_lst.append(data[i-1][k])
                            k += 1
                        else:
                            current_num += data[i][k]
                            check_lst.append(data[i][k+1])
                            check_lst.append(data[i-1][k])
                            check_lst.append(data[i-1][k+1])
                            check_lst.append(data[i-1][k-1])
                            check_lst.append(data[i][k-1])
                            k += 1

                    is_counted = find_symbols(check_lst)

                    if is_counted and current_num != '':
                        total_sum += int(current_num)
                    current_num = ''
                    check_lst = []
        else:
            while k < len(data[i]) and data[i][k].isdigit():
                if k == 0 or k == len(data[i]):
                    current_num += data[i][k]
                    check_lst.append(data[i-1][k])
                    check_lst.append(data[i+1][k])
                else:
                    current_num += data[i][k]
                    check_lst.append(data[i-1][k-1])
                    check_lst.append(data[i-1][k])
                    check_lst.append(data[i][k-1])
                    check_lst.append(data[i+1][k-1])
                    check_lst.append(data[i+1][k])

                    if k + 1 < len(data[i]):
                        check_lst.append(data[i - 1][k + 1])
                        check_lst.append(data[i][k + 1])
                        check_lst.append(data[i + 1][k + 1])

                k += 1

            is_counted = find_symbols(check_lst)

            if is_counted and current_num != '':
                total_sum += int(current_num)
            current_num = ''
            check_lst = []
        k += 1
    i += 1

print(total_sum)
