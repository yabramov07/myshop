def from_decimal(number, base):
    data = []
    while number > 0:
        data.append(str(number % base))
        number //= base
    data = data[::-1]
    print(''.join(data))


def to_decimal(number, base):
    summ = 0
    number = str(number)[::-1]
    for i in range(len(number)):
        summ += int(number[i]) * (base ** i)
    print(summ)


while True:
    question = input('из десятичной (1) / в десятичную (2): ')
    if question == 'stop':
        break
    if question == 'из десятичной' or question == '1':
        number, base = int(input('Изначальное число: ')), int(input('Основание нового числа: '))
        from_decimal(number, base)
        print('-' * 52)
    elif question == 'в десятичную' or question == '2':
        number, base = int(input('Изначальное число: ')), int(input('Основание изначального числа: '))
        to_decimal(number, base)
        print('-' * 52)
