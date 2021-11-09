from lab4classes import QueueWithStacks
from lab4classes import StackWithMax


def inputs(file_name):
    file_open = open(file_name, 'r')
    data = [int(i) for i in file_open.read().split()]
    m = data.pop()
    del data[0]
    file_open.close()
    return data, m


def outputs(filename, data):
    file_out = open(filename, 'w')
    for current_number in data:
        file_out.write(str(current_number) + ' ')


def main():
    data, m = inputs('input.txt')
    ans = []
    queue = QueueWithStacks(StackWithMax)
    queue.stack1.push(data[:m])
    data = data[m:]
    data_index = 0
    finish = False

    while True:
        queue.fake_pop()
        for i in range(m):
            ans.append(queue.maxim())
            queue.pop()
            if data_index >= len(data):
                finish = True
                break
            else:
                queue.push(data[data_index])
            data_index += 1
        if finish:
            break

    outputs('output.txt', ans)


main()
