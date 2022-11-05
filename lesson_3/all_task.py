#                1-0

# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной 
# позиции.

count = int(input('Введите кол-во чисел: '))
list = []

for i in range(0,count):
    list.append(int(input()))

sum = 0

for i in range(1,len(list)+1):
    if i %2 == 0:
        sum += list[i-1]

print(f"Сумма элементов списка, стоящих на нечётной позиции: {sum}.")



#                1-1

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



#                1-2

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


       




#                1-3

# Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное.
def tobin_int(value):
    answer = ""
    value = int(value)

    while value >= 1:
        answer = answer + str(value % 2)
        value = value // 2

    answer = list(answer)

    for i in range(0,len(answer)//2):
        temp = answer[i]
        answer[i] = answer[len(answer)-i-1]
        answer[len(answer)-i-1] = temp

    answer = ''.join(answer)
    return answer



def tobin_dec(value,precision):
    answer = ""
    value = float('0' + value[value.find('.'):])

    for i in range(0,precision):
        value = value * 2
        answer = answer + str(int(value))
        value = float('0' + str(value)[str(value).find('.'):])

    return answer



value = str(input("Введите десятичное число: "))

if value.find(".") == -1:

    answer = tobin_int(value)
    
    print(f'В двоичном представлении: {answer}')


else:

    answer1 = tobin_int(value[:value.find('.')])
    answer2 = tobin_dec(value,11)
    answer = answer1 + "." + answer2

    print(f'В двоичном представлении: {answer}')



#                1-4

# Задайте число. Составьте список чисел Фибоначчи, в том 
# числе для отрицательных индексов.

value = int(input("Введите индекс:"))
list1 = [0,1]
list2 = []

for i in range(2,value+1):
    list1.append(list1[i-1]+list1[i-2])
    list2.append((-1)**(i+1)*list1[i])

list2.reverse()
print(f'Список чисел Фибоначи для этого индекса: {list2 + list1}')
