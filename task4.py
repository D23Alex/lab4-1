from lab4classes import Stack


def inputs(file):
    file_open = open(file, 'r')
    data = [i for i in file_open.read()]
    return data


def is_closing(el):
    return el in '}])'


def main():
    stack = Stack()
    data = inputs('input.txt')
    to_return = None
    file_out = open('output.txt', 'w')
    for i in range(len(data)):
        if data[i] in '([{}])':
            if is_closing(data[i]):
                if stack.top.key is None:
                    to_return = i + 1
                    break
                if stack.top.key[0] + data[i] not in ['()', '[]', '{}']:
                    to_return = i + 1
                    break
                else:
                    stack.pop()
            else:
                stack.push((data[i], i))

    if to_return is not None:
        file_out.write(str(to_return))
    elif stack.is_empty():
        file_out.write('success')
    else:
        current_element = stack.top
        while current_element.previous.key is not None:
            current_element = current_element.previous
        file_out.write(str(current_element.key[1] + 1))

    file_out.close()


main()
