print("Введите координату X")
x = int(input())
print("Введите координату Y")
y = int(input())

if x > 0 and y > 0:
 print("Точка в 1й четверти.")
elif x < 0 and y > 0:
 print("Точка в 2й четверти.")
elif x < 0 and y < 0:
 print("Точка в 3й четверти.")
elif x > 0 and y < 0:
 print("Точка в 4й четверти.")
else:
 print("Точка в нуле.")