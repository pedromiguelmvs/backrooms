from subtitles import *
from questions import *
import random

print("""
 _______ _              ______              _                                  
(_______) |            (____  \            | |                                 
 _      | | _   ____    ____)  ) ____  ____| |  _  ____ ___   ___  ____   ___  
| |     | || \ / _  )  |  __  ( / _  |/ ___) | / )/ ___) _ \ / _ \|    \ /___) 
| |_____| | | ( (/ /   | |__)  | ( | ( (___| |< (| |  | |_| | |_| | | | |___ | 
 \______)_| |_|\____)  |______/ \_||_|\____)_| \_)_|   \___/ \___/|_|_|_(___/  
""")

input('Pressione Enter para iniciar.')
for a in range(10):
    print()

name = input('Como você se chama? ').capitalize()
age = input('Qual é a sua idade? ')

while not age.isnumeric():
    print('Por favor, insira sua idade')
    age = input('Qual é a sua idade? ')
else:
    def isAgeInt():
        if age.isnumeric():
            return int(age)
        else:
            return int(age.split('.')[0])
    # a função acima verifica se o que o usuário inseriu de fato é um número inteiro. Caso não seja um número inteiro
    # então a função irá transformá-lo numa lista e pegar o número de index 0, que será um inteiro. Contará como a idade.

    if type(isAgeInt()) == int and isAgeInt() >= 18:  # Essa condicional verifica se a idade inserida é maior ou igual a 18.
        print()
    else:  # Caso não seja, o programa encerra. Caso seja, ele continuará a rodar.
        print(OLDER_THAN_FOURTEEN_ONLY)
        exit()

    print(WHO_ARE_YOU(name))

    stayorleave = str(input('[A] Ir embora | [B] Ficar na sala: ')).upper()

    if stayorleave == 'A':
        parallels = [BE_A_HERO, GET_OUT_WITH_BROTHERS]
        alternative_final = random.choice(parallels)
        alternative_final()
    elif stayorleave == 'B':
        parallels = [LEFT_NIGHT]
        alternative_final = random.choice(parallels)
        alternative_final()
    else:
        print(GOD_PUNISHMENT_FINAL)
        exit()

    stayorleave2 = str(input('[A] Permanecer na sala | [B] Passear pelos corredores: ')).upper()

    if stayorleave2 == 'A':
        print(GET_OUT_ALONE)
        print(PRISIONED_FINAL)
    elif stayorleave2 == 'B':
        print(
            5 * '\n' + 'Você abre a porta da sala e começa a andar pelos corredores escuros de seu colégio. Passando\n'
                       'pela sala de computação, você decide navegar um pouco pela internet. Lá você descobre que há um\n'
                       f'anúncio recompensando quem encontrasse alguém chamado {name}. É você, e a noticia é datada de\n'
                       f'10 anos atrás. Você nunca mais foi visto.')
        print('|Preso no tempo: Você acessou um buraco de minhoca e está preso numa dimensão onde o tempo é confuso|')
    else:
        print(5 * '\n' + 'Devido a não conseguir tomar decisões acertivas em sua vida, você foi punido por Deus a \n'
                         'cessar sua existência medíocre. Você nunca mais foi visto.')
        exit()
