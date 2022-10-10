import random

symbols = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
password = int(input('Введите колличество знаков: '))
gen_password = ''

for i in range(password):
    q = random.choice(symbols)
    gen_password += q

print(gen_password)