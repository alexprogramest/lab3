def for_line():
    my_sum = 0
    with open("text.txt") as f:
        for line in f:
            if line.strip().isdigit():
                my_sum += int(line.strip())


def generate():
    my_sum = sum((int(row.strip()) for row in open('text.txt') if row.strip().isdigit()))


if __name__ == '__main__':
    # with open('text.txt', 'a') as f:
    #     while os.path.getsize("text.txt") < 52428800:
    #         f.write(str(randint(0, 1000000)) + '\n')
    print(timeit.timeit(read_lines, number=1))
    print(timeit.timeit(for_line, number=1))
    print(timeit.timeit(generate, number=1))
