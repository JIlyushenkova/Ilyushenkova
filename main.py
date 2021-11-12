# File "C:\Users\Ilyushenkova\PycharmProjects\pythonProject1\main.py", line 1
# уравнение имеет вид a*x**2+b*x+c=0
import math

print('введите коэффициенты для уравнения')
print('a*x**2+b*x+c=0')
a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

discr = b ** 2 - 4 * a * c
print('Дискриминант D = ' , discr)
if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print('x1 = ', x1, 'x2 = ', x2)
elif discr == 0:
    x = -b / (2 * a)
    print(x)
else:
    print('Корней нет')
if discr < 0:
    print('Дискриминант D =', discr)
else:
    print('Корней нет')
