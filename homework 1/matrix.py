def matrixFunct(t):
    print("Matrix:")
    for i in range(1, t+ 1):
        for j in range(1, t+ 1):
            print((i - 1) * t + j, end=' ')
        print()
    print("Matrix transpose:")
    for i in range(1, t+ 1):
        for j in range(1, t+ 1):
            print(i + (j - 1) * 3, end=' ')
        print()

t = int(input('enter a number'))
matrixFunct(t)