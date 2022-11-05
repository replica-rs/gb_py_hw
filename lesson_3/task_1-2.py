# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным 
# значением дробной части элементов.

count = int(input('Введите кол-во чисел: '))
list = []

for i in range(0,count):
    list.append(input())

min = 1
max = 0

for i in range(0,count):
 list[i] = float('0' + list[i][list[i].find('.'):])

for i in range(0,count):
    if min > list[i]:
        min = list[i]

    if max < list[i]:
        max = list[i]

print(f"Максимальное значение дробной части элементов: {max}.  Минимальное значение дробной части элементов: {min}. Их разница {max-min}")


       
