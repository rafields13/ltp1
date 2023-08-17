n = int(input('Qual é o valor? '))
d = int(input('Qaul é o desconto? '))

print(f'Valor sem desconto : {n}')
print(f'Desconto: {d}%')
print(f'Valor com desconto: {n - (n * d / 100)}')
