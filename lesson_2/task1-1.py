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