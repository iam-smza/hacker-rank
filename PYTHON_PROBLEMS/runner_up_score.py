# The first line contains n. The second line contains an array A[] of n
# integers each separated by a space.
# Example:
#       Given list is [2 3 6 6 5]. The maximum score is 6, second maximum is 5.
#       Hence, we print 5 as the runner-up score.

if __name__ == '__main__':

    number = int(input())
    array = sorted(map(int, input().split()), reverse=True)

    for item in array:
        if item < max(array):
            print(item, end='')
            break
