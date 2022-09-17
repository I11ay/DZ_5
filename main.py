print('Первое задание:')

a = int(input('Введите первое число которое будет больше 10 и кратно 3:'))
b = int(input('Введите второе число которое будет больше 10 и кратно 3:'))
c = int(input('Введите третье число которое будет больше 10:'))

if ((a > 10) and ((a % 3) == 0)) and ((b > 10) and ((b % 3) == 0)) and c > 10:
    print('Yes')
else:
    print('No')

print("Второе задание:")
A = int(input('Введите первое число:'))
B = int(input('Введите второе число:'))
C = int(input('Введите третье число:'))
if A > C and A > B:
    print(f'Max:{A}')
elif B > C and B > A:
    print(f'Max:{B}')
elif C > A and C > B:
    print(f'Max:{C}')
else:
    print('Вы ввели одинаковые числа, при корректной работе программы необходимо ввести разные числа.')

print("Третье задание:")
number = input('Введите любое трёхзначное число:')
ints = []
try:
    for line in number:
        ints.append(int(line))
except ValueError:
    print('Это не число. Начните заново.')
else:
    first_digit = int(int(number) / 100)
    second_digit = int((int(number) - (first_digit * 100)) / 10)
    third_digit = int(int(number) - (first_digit * 100) - (second_digit * 10))
    c = int(str(third_digit) + str(second_digit) + str(first_digit))
    print(f'reversed_number {c}')
    exit()
number = input('Введите любое трёхзначное число:')
ints = []
try:
    for line in number:
        ints.append(int(line))
except ValueError:
    print("Снова не верное значение, прочитайте условия внимательнее и начните заново.")
else:
    first_digit = int(int(number) / 100)
    second_digit = int((int(number) - (first_digit * 100)) / 10)
    third_digit = int(int(number) - (first_digit * 100) - (second_digit * 10))
    c = int(str(third_digit) + str(second_digit) + str(first_digit))
    print(f'reversed_number {c}')
