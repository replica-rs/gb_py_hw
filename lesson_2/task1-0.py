#Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.
value = float(input('Число = '))
summ = 0

if (0<value<1) or (value<0):
    for ch in str(value):
        if ch !='.' and ch !='-':
            summ += int(ch)
else:
    while value != 0:
        summ += value % 10
        value = value // 10

print(f"Сумма цифр: {int(summ)}.")