# Read an integer N and print out the values that lead upto N
# on a single line

if __name__ == '__main__':
    number = int(input())

    value = 0
    while value != number:
        value += 1
        print(f'{value}', end='')
