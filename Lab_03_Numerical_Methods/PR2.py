import math as m

# функция для нахождения ctg
def ctg(x):
    return 1 / m.tan(x)

def f(x):
    try:
        return (m.cos(0.3 * m.pi) + m.sqrt(1 - m.cos(0.35 * m.pi))) \
            / pow(m.tan(1.6 * m.pi) - ctg(x), 2) \
            - m.exp(-0.5) * m.log10(20.3)
    except:
        return None

# ввод значения x с проверкой
while True:
    try:
        x = float(input('Введите х: '))
        break
    except ValueError:
        print('Ошибка! Введено не число')
        continue


print("+---------+-------------+")
print("|    x    |     f(x)    |")
print("+---------+-------------+")

for i in [0.5 * x, 0.75 * x, x, 1.25 * x, 1.5 * x]:
    y = f(i)
    if y is None:
        print("| %7.2f | %11s |" % (i, 'NaN'))
    else:
        print("| %7.2f | %11.3f |" % (i, y))

print("+---------+-------------+")