def print_line(char, times):
    print(char * times)


def print_lines(row, char, times):
    """打印多行分割线

    :param row: 打印几次
    :param char: 打印那种分割线
    :param times: 每个分割线打印几次
    """
    n = 0
    while n < row:
        print_line(char, times)
        n += 1


print_lines()
