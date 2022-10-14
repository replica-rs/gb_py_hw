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

