# просто стек
from lab4classes import Stack


def inputs(file_name):
    file_open = open(file_name, 'r')
    data = []
    while True:
        # считываем строку
        line = file_open.readline()
        # прерываем цикл, если строка пустая
        if not line:
            break
        data.append([i for i in line.split()])
    del data[0]
    file_open.close()
    return data


def main():
    data = inputs('input.txt')
    file_out = open('output.txt', 'a')
    stack = Stack()
    for currentCommand in data:
        if currentCommand[0] == '-':
            file_out.write(str(stack.pop()) + '\n')
        else:
            stack.push(int(currentCommand[1]))
    file_out.close()


main()
