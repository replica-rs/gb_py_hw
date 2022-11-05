#Задайте список из n чисел последовательности (1+(1/n))^n 
# и выведите на экран их сумму.
value = int(input('Число = '))
list = [] 
for i in range(1,value+1):
    list.append((1+1/i)**i)

print(f'Cписок последовательности (1+(1/n))^n : {list}') 
print(f'Сумма его чисел: {sum(list)}')