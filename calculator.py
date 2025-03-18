#Addition calculater
def num_add():
    add = num1 + num2
    return add

num1 =int(input ('Enter First Number: '))
num2 = int(input ('Enter Second Number: '))

print(f'{num1} + {num2} = ',num_add())
