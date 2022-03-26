num1 = int(input('enter an integer: '))
num2 = int(input('enter another integer: '))


def multiplicationtable(x,y):
    for i in range(x, y):
        for j in range(x, y):
            print(i, "*", j, '=', i * j)

multiplicationtable(num1, num2)