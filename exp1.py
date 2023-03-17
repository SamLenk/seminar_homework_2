def min_flips(coins):
    heads = coins.count('H')
    tails = coins.count('T')
    if heads == 0 or tails == 0:
        return 0
    if heads < tails:
        return heads
    else:
        return tails

n = int(input('Введите количесво монет: '))
coins = input('Введите какой стороной повернуты монеты (H H H T T(Пример)): ').split()
print(f'-> В данном случае достаточно перевернуть {min_flips(coins)} монет.')