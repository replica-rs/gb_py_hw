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