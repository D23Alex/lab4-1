from lab4classes import QueueWithLength


def serve_one(queue):
    # выдаём справку 1 клиенту и его же отправляем в конец, если ему ещё что-то надо
    new_key = queue.pop() - 1
    if new_key > 0:
        queue.push(new_key)


def inputs(file_name):
    file_open = open(file_name, 'r')
    data = [int(i) for i in file_open.read().split()]
    m = data[1]
    del data[0]
    del data[0]
    file_open.close()
    return data, m


def outputs(queue, file_name):
    file_out = open(file_name, 'w')

    length = queue.length
    if length == 0:
        length = -1

    current_element = queue.first.next
    file_out.write(str(length) + '\n')
    while current_element is not None:
        file_out.write(str(current_element.key) + ' ')
        current_element = current_element.next
    file_out.close()


def main():
    data, m = inputs('input.txt')
    queue = QueueWithLength(data)

    # m раз выдаём справку
    for i in range(m):
        if queue.length <= 0:
            break
        serve_one(queue)

    outputs(queue, 'output.txt')


main()
