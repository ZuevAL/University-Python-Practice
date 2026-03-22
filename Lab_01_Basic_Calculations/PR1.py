import math as m

#функция для нахождения ctg
def ctg(x):
    return 1 / m.tan(x)
#вычисление арифметического выражения
ans = (m.cos(0.3 * m.pi) + m.sqrt(1 - m.cos(0.35 * m.pi))) \
      / pow(m.tan(1.6 * m.pi) - ctg(0.8), 2) \
      - m.exp(-0.5) * m.log10(20.3)

print('Oтвет:', ans)