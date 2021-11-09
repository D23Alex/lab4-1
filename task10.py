from lab4classes import QueueWithLength


def inputs(file_name):
    to_return = []
    file_open = open(file_name, 'r')
    data = [int(i) for i in file_open.read().split()]
    del data[0]
    for i in range(0, len(data) - 2, 3):
        to_return.append((data[i] * 60 + data[i + 1], data[i + 2]))
    file_open.close()
    return to_return


def outputs(value_mins, file_name):
    file_out = open(file_name, 'a')
    file_out.write(str(value_mins // 60) + ' ' + str(value_mins % 60) + '\n')
    file_out.close()


# процедура прихода нового клиента
def new_customer(queue, arrival_time, tolerance):
    # выпустим людей
    queue.let_people_out(arrival_time)
    a = queue.length
    # если сечас перед клиентом больше чем он может выдержать - выпускаем сразу
    if queue.length > tolerance:
        outputs(arrival_time, 'output.txt')
    else:
        # посмотрим, сколько ещё стоять первому в очереди челу и добавим количество людей в очереди -1 * 10
        if queue.first.next is None:
            leave_time = arrival_time + 10
        else:
            leave_time = (queue.first.next.key - arrival_time) + (queue.length - 1) * 10 + arrival_time + 10
        outputs(leave_time, 'output.txt')
        # всё просчитано и выведено в файл, теперь чел отправляется в очередь
        queue.push(leave_time)


def main():
    # идея - к моменту прихода нового посетителя будем сначала выпускать тех, то уже должны были быть обслужены
    # затем, зная, сколько человек на самом деле перед ним и сколько минут ещё стоять первому челу -
    # новый чел либо уходит, либо для него сразу рассчитывается время выхода и он добавляется в очередь
    # будем хранить в значении key кортеж время выхода
    data = inputs('input.txt')
    queue = QueueWithLength()
    # если учередь пустая, то есть queue.first.next is None - то чел становится первым и время его выхода
    for i in range(len(data)):
        new_customer(queue, data[i][0], data[i][1])
    # в ответ на задачу готов, но чтобы подготовить очередь к след. использованию можно выпустить всех людей(необяз.)


main()
