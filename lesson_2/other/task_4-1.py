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