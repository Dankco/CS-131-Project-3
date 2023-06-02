def take(n, gen):
    count = 0
    output = []
    while count < n:
        output.append(next(gen))
        count += 1
    return output


def skip(n):
    num = n
    while True:
        yield num
        num += n


print(take(5, skip(2)))
