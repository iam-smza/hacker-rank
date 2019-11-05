# Read an integer N. For all non-negative integers i < N. Print sqr(i)

if __name__ == '__main__':
    number = int(input())

    for n in range(0, number):
        print(f'{n * n}')
