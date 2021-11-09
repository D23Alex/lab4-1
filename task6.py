from lab4classes import QueueWithStacks
from lab4classes import StackWithMin


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
    return data


def execute_the_command(current_command, queue, file_out):
    if current_command[0] == '-':
        queue.pop()
    elif current_command[0] == '?':
        file_out.write(str(queue.minim()) + '\n')
    else:
        queue.push(int(current_command[1]))


def main():
    data = inputs('input.txt')
    queue = QueueWithStacks(StackWithMin)
    file_out = open('output.txt', 'a')
    for current_command in data:
        execute_the_command(current_command, queue, file_out)
    file_out.close()


main()
