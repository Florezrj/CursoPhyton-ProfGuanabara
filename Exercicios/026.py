frase = input('Digite uma frase: ').strip()
frase = frase.lower()
print('A letra A aparece {} vezes na frase? '.format(frase.count('a')))
print('A letra A aparece a primeira vez na posição {}.'.format(frase.find('a') + 1))
print('A letra a aparece pela ultima vez na posição {}'.format(frase.rfind('a') + 1))