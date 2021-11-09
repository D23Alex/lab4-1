from lab4classes import StackWithCalc


def inputs(file_name):
    file_open = open(file_name, 'r')
    data = [i for i in file_open.read().split()]
    del data[0]
    return data


def main():
    data = inputs('input.txt')
    file_out = open('output.txt', 'w')
    stack = StackWithCalc()
    for currentElement in data:
        if currentElement in '+-*/':
            stack.push(currentElement)
        else:
            stack.push((int(currentElement)))
    file_out.write(str(stack.top.key))
    file_out.close()


main()
