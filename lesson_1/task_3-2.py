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