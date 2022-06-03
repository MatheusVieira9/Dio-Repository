'''
print('Qual a cor do alienigena ? \ngreen \nyellow \nred')
alien_color = input('Antes de confirmar, verifique se escreveu o nome da cor corretamente. ')
alien_color = alien_color.lower()

if alien_color == 'green':
    score = 5

elif alien_color == 'yellow':
    score = 10

elif alien_color == 'red':
    score = 15
 
print('Sua pontuação é {} pontos.'.format(str(score)))

# Cria a lista que irá receber os dicionários com cada caracteristica de cada alien
aliens = []

# Cria um alien e adiciona-o a lista (aliens), até chegar na quantidade total exigida que é 27
for alien in range(27):
    new_alien = {'speed' : 'slow', 'color' : 'red', 'point' : 5}

    aliens.append(new_alien)

# Apresenta os 5 primeiros aliens da lista
for alien in aliens[: 5]:
    print(alien)

print('.' *3)

print('\n\n O número de aliens criados é: {}'.format(len(aliens)))
'''
dicio = {}
num = 0
for num in range(10):
    num += 1
    chaves = 'chave' + str(num)
    valores = 'valor' + str(num)
    
    dicio[chaves] = valores

print(dicio)    