def process(i: int):
    printout = ''
    if i % 3 == 0:
        printout += 'Fizz'
    if i % 5 == 0:
        printout += 'Buzz'
    if printout == '':
        printout += str(i)
    return printout


if __name__ == '__main__':
    n = 100
    for i in range(1, n + 1):
        print(process(i))
