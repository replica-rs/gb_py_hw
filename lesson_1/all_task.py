#Task 1

#Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот
#  день выходным.

print("Введите день недели в цифровом формате:")
value = int(input())
if value > 6 and value < 7:
 print("Да")
else: 
 print("Нет")




#Task 2,1

#Напишите программу для. проверки истинности 
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для 
# всех значений предикат.

print("Введите X:")
x = bool(input())
print("Введите Y:")
y = bool(input())
print("Введите Z:")
z = bool(input())


out1 = not(x and y and z)
out2 = not(x) and not(y) and not(z)

print(f"{out1}={out2} - {out1 == out2}")



#Task 2,2

#Напишите программу, которая принимает на вход 
# координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и 
# выдаёт номер четверти плоскости, в которой находится
#  эта точка (или на какой оси она находится).

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



#Task 3,1

#Напишите программу, которая по заданному номеру четверти,
#  показывает диапазон возможных координат точек в этой 
# четверти (x и y).

print("Введите номер четверти.")
value = int(input())

answer = [
["0","+∞","0","+∞"],
["-∞","0","0","+∞"],
["-∞","0","-∞","0"],
["0","+∞","-∞","0",]
]
if value > 0 and value < 5:
 print(f"X может принимать значения от {answer[value-1][0]} до {answer[value-1][1]}.")
 print(f"Y может принимать значения от {answer[value-1][2]} до {answer[value-1][3]}.")
else:
 print("Неверный ввод.")





#Task 3,2

#Напишите программу, которая принимает на вход 
# координаты двух точек и находит расстояние между ними 
# в 2D пространстве.

import math

print("Введите координаты точек A,B")
print(" ")
print("Координата X точки A:")
ax = int(input())
print("Координата Y точки A:")
ay = int(input())

print("Координата X точки B:")
bx = int(input())
print("Координата Y точки B:")
by = int(input())


result = math.sqrt(math.pow(bx - ax, 2) + math.pow(by - ay, 2))

print(f"Расстояние между точками A,B равно {result}.")

