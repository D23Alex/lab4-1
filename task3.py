from lab4classes import Stack


def is_valid(str_given, stack):
    for current_symbol in str_given:
        if current_symbol in '])':
            if stack.top.key is None:
                return 'NO'
            if stack.top.key + current_symbol not in ['()', '[]']:
                return 'NO'
            stack.pop()
        else:
            stack.push(current_symbol)
    if stack.is_empty():
        return 'YES'
    return 'NO'


def inputs(file_name):
    file_open = open(file_name, 'r')
    data = []
    line = file_open.readline()
    while True:
        # считываем строку

        # прерываем цикл, если строка пустая
        if not line:
            break
        line1 = line
        line = file_open.readline()
        data.append(line[:-1])
    data[len(data) - 2] += line1[len(line1) - 1]
    del data[len(data) - 1]
    return data


def main():
    data = inputs('input.txt')
    file_out = open('output.txt', 'w')
    answer = []

    for current_str in data:
        stack = Stack()
        file_out.write(is_valid(current_str, stack) + '\n')


main()
