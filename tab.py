num = int(input('Digite um numero:'))

print(f'A tabuada de {num} é...')

for resultado in range(1, 101):
    print(f'{num} x {resultado:2} = {num * resultado}')