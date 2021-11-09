from lab4classes import QueueArmy
from lab4classes import QueueElement


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


def execute_the_command(current_command, queue, file_out):
    if current_command[0] == 'left':
        queue.insert_left(QueueElement, current_command[1], current_command[2])
    elif current_command[0] == 'right':
        queue.insert_right(QueueElement, current_command[1], current_command[2])
    elif current_command[0] == 'leave':
        queue.delete_element(current_command[1])
    else:
        left, right = queue.neighbors(current_command[1])
        file_out.write(left + ' ' + right + ' ' + '\n')


def main():
    data = inputs('input.txt')
    file_out = open('output.txt', 'a')
    queue = QueueArmy('1')
    for current_command in data:
        execute_the_command(current_command, queue, file_out)
    file_out.close()


main()
