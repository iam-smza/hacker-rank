# Read two STDIN and print out integer division and float division

if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(f'{a // b}')
    print(f'{a / b:.11f}')
