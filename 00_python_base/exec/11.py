# -*-coding:utf8 -*-

def a(n):
    result = []
    num = []
    for i in range(n):
        line = []
        num_line = []
        for j in range(n):
            line.append([i, j])
            num_line.append(0)
        result.append(line)
        num.append(num_line)
    return result, num


def booboo(n, start):
    result, num = a(n)
    for line in result:
        for x, y in line:
            if x == n - 1 or y == 0:
                z = x + y + 1 + start - 1
                num[x][y] = z
            elif y == n - 1:
                z = 2 * n - 1 + (y - x) + start - 1
                num[x][y] = z
            elif x == 0 and y != 1:
                z = 3 * n - 2 + (n - 1 - y) + start - 1
                num[x][y] = z
            elif y == 1 and x == 0:
                z = 3 * n - 2 + (n - 1 - y) + start - 1
                num[x][y] = z

    c_list = []
    for c in num:
        for _num in c:
            c_list.append(_num)
    start = max(c_list) + 1
    return num, start


def merge_fun(a, b):
    len_int = len(a)
    # print(len_int)
    for x in range(len_int):
        for y in range(len_int):
            b[x + 1][y + 1] = a[x][y]
    return b


def startup(number):
    out_put = number
    num_list = [number]
    while True:
        number = number - 2
        if number > 0:
            num_list.append(number)
        else:
            break
    # print(num_list)

    total_list = []
    for n in num_list:
        if num_list.index(n) == 0:
            start = 1
            num, start = booboo(n, start)
            total_list.append(num)
        else:
            num, start = booboo(n, start)
            total_list.append(num)

    # print(total_list)

    for i in range(len(total_list) - 1, -1, -1):
        if i != 0:
            total_list[i - 1] = merge_fun(total_list[i], total_list[i - 1])

    # print(total_list[0])
    print("按照指定规律打印,num={}".format(out_put))
    for i in total_list[0]:
        for j in i:
            print(str(j).zfill(2), end=' ')
        print()

    return total_list[0]


startup(6)
startup(5)
startup(4)
startup(3)
startup(2)
startup(1)
