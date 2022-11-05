# Напишите программу, которая найдёт произведение пар чисел
#  списка. Парой считаем первый и последний элемент, второй 
# и предпоследний и т.д.

count = int(input('Введите кол-во чисел: '))
list = []

for i in range(0,count):
    list.append(int(input()))

pr = []

for i in range(0,(len(list)+1) // 2):
    pr.append(list[i] * list[len(list)-i-1])

print(f"Произведения пар чисел списка: {pr}.")