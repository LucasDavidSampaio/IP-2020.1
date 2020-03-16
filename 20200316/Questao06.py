num = int(input())

for i in range(num):
    if (num % (i + 1) == 0):
        print(i + 1, end=' ')
