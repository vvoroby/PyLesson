# задание 1
otvet1 = input('is it raining? ').lower()
if otvet1 == 'yes':
   otvet2 = input('is it windy?').lower()
   if otvet2 == 'yes':
       print('it is too windy for an umbrella')
   else:
       print('take an umbrella')
else:
   print('enjoy your day')

# задание 2
name = input('Введите фамилию: ').title()
name2 = input('Введите имя: ').title()
print(name+name2)

# задание 3
stroka = input('Введите первую строку какого-нибудь стихотворения: ')
start = int(input("Введите начальную позицию: "))
end = int(input("Введите конечную позицию: "))
print('Длинна строки: ' + str(len(stroka)) + ' Выбранная часть строки ' + stroka[start:end])

# задание 4
name = input('Ведите своё имя: ')
if len(name) < 5:
    fam = input('Введите фамилию: ')
    print(name.upper() + fam.upper())
else:
    print(name.lower())

# задание 5
import math
s = int(input('Введите целое число >500: '))
print(float('{:.2f}'.format(math.sqrt(s))))

# задание 6
import math

figura = input('Введите тип фигуры из предложенных (круг, треугольник, прямоугольник): ')
if figura == 'круг':
    r = float(input('Введите радиус круга: '))
    print('Результат' + str(3.14 * r * r))
elif figura == 'треугольник':
    a = float(input('Введите длину стороны A: '))
    b = float(input('Введите длину стороны В: '))
    c = float(input('Введите длину стороны С: '))
    p = (a+b+c)/2
    print('Результат: ' + str(math.sqrt(p*(p-a)*(p-b)*(p-c))))
elif figura == 'прямоугольник':
    a1 = float(input('Введите длину стороны A: '))
    b1 = float(input('Введите длину стороны B: '))
    print('Результат: ' + str((a1+b1)/2))
else:
    print('Фигура указана неверно')

