from math import *
A = input()
B = input()
C = input()
D = input()
buk = A+B+C+D
if buk.isalpha():
    print("Вычисление невозможно")

else:
    A = float(A)
    B = float(B)
    C = float(C)
    D = float(D)

    if C <= 0:
        print("Ошибка:нарушено условие существования логарифма")
    elif D == 0:
        print("Ошибка: деление на ноль")
    elif (pow(5.5, A) - ((2*sin((A+B))) / (1-cos((log(C, e))))) + pi/D) < 0:
        print("Ошибка: подкоренное выражение меньше 0")
    elif (1-cos(log(C, e))) == 0:
        print("Ошибка: деление на ноль")
    else:
        S = (7.7*pow(10, -5)) * sqrt(pow(5.5,A) - ((2*sin(A+B)) / (1- cos(log(C,e)))) + pi/D )
        print(S)
