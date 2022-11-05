#           1-0

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


#           1-1

#Напишите программу, которая принимает на вход число N и выдает набор 
# произведений чисел от 1 до N.
value = int(input('Число(N) = '))
list = [] 
for i in range(1,value+1):
    temp = 1
    for j in range(1,i+1):
        temp = temp * j
    list.append(temp)
    
print(f'Произведений чисел от 1 до N: {list}')



#           1-2

#Задайте список из n чисел последовательности (1+(1/n))^n 
# и выведите на экран их сумму.
value = int(input('Число = '))
list = [] 
for i in range(1,value+1):
    list.append((1+1/i)**i)

print(f'Cписок последовательности (1+(1/n))^n : {list}') 
print(f'Сумма его чисел: {sum(list)}')




#           OTHER


#           4-1

# Задайте список из N элементов, заполненных числами из
#  промежутка [-N, N]. Найдите произведение элементов на
#  указанных позициях. Позиции хранятся в файле file.txt 
# в одной строке одно число.

# Реализуйте алгоритм перемешивания списка.

count = int(input('Введите кол-во чисел: '))
list = []
pos = []
answer = 1

for i in range(count):
    list.append(input())


path = 'D:/GitHud/Phyton_GB/git_homew/lesson_2/other/file.txt'
with open(path, 'r') as data:
 for line in data:
   pos.append(int(line.replace("\n", "")))

if int(count-1) not in pos:
    print("В файле нет позиций заданного списка.")
    exit()


for i in range(len(list)):
    if i in pos:
        answer = answer * list[i]

print(f"Произведение элементов на указанных позициях: {answer}.")




#           4-2

# Даны два массива:
# [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
# Надо вернуть их пересечение
# [1, 2, 2, 3]

list1 = [1,2,3,2,0]
list2 = [5,1,2,7,3,2]
ltemp = []

for i in list1:
    for j in list2:
        if i == j:
            ltemp.append(i)
            break

print(f'Пересечение [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]: {ltemp}')