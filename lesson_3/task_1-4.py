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
