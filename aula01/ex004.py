x = 0
c = 0 

while x != -1:
    x = int(input('Digite um número, por favor. (-1 caso deseje sair)'))
    c += 1

    if x == -1:
        break

print('O número total de loops foi {}.'.format(c-1)) # c-1 pois tiramos o loop de saída "-1".