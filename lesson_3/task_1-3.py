# Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное.
def tobin_int(value):
    answer = ""
    value = int(value)

    while value >= 1:
        answer = answer + str(value % 2)
        value = value // 2

    answer = list(answer)

    for i in range(0,len(answer)//2):
        temp = answer[i]
        answer[i] = answer[len(answer)-i-1]
        answer[len(answer)-i-1] = temp

    answer = ''.join(answer)
    return answer



def tobin_dec(value,precision):
    answer = ""
    value = float('0' + value[value.find('.'):])

    for i in range(0,precision):
        value = value * 2
        answer = answer + str(int(value))
        value = float('0' + str(value)[str(value).find('.'):])

    return answer



value = str(input("Введите десятичное число: "))

if value.find(".") == -1:

    answer = tobin_int(value)
    
    print(f'В двоичном представлении: {answer}')


else:

    answer1 = tobin_int(value[:value.find('.')])
    answer2 = tobin_dec(value,11)
    answer = answer1 + "." + answer2

    print(f'В двоичном представлении: {answer}')