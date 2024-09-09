'''
Crie um programa que cria dois objetos da mesma classe (Pessoa), e mostre uma conversa amigável entre os dois objetos.
'''

import random

class Pessoa:
    def __init__(self, nome, humor):
        self. humor = humor
    
    # método de ação
    def cumprimento(self):
        if self. humor:
            print(f'olá, meu é {self.nome}. Qual seu nome?')
        else:
            print(f'Tá olhando o quê? Se toca...')

    def responder(self, nome, humor):
        if humor:
            print(f'Olá, {nome}, meu nome {self.nome}. Prazer em te conhacer. ')
            self.humor = True

        else:
            print(f'Vai se lascar, infaliz.')
            self.humor = False
        return self.humor
    

if __name__ == '__main__':
    humores = (True, False)
    nome1 = input('Informe o nome do 1ª usuário:')
    nome2 = input('Informe o nome do 2º usuário:')

    # instância dos objetos
    usuario1 = Pessoa(nome1, humores[random.randint(0,1)])
    usuario2 = Pessoa(nome2, humores[random.randint(0,1)])

    usuario1.cumprimentar()
    usuario1.humor = usuario2.responder(usuario1.nome, usuario2.humor)

    if usuario1.humor:
        print(f'{usuario1.nome} ficou feliz.')
    else:
        print(f'{usuario1.nome} ficou triste.')

