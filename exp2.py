S = int(input("Введите сумму чисел: "))
P = int(input("Введите произведение чисел: "))

for X in range(1, 1001):
    if P % X != 0:  # X должно быть делителем P
        continue

    Y = P // X
    if X + Y == S:
        print("Ответ: X = {}, Y = {}".format(X, Y))
        break
else:
    print("Нет решения для заданных параметров.")