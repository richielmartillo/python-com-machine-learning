class Animal:
    def __init__ (self, nome, cor, especie):
        self.nome = nome
        self.cor = cor
        self.especie = especie

    def apresentar(self):
        print(f'Eu sou o(a) {self.especie} chanado(a) {self.nome}')


class Gato(Animal):
    def emitir_som(self):
        print('Miau!')
    def arranhar(self):
        print('O gato está arranhando')    

class Cachorro(Animal):
    def emitir_som(self):
        print('Au Au Au...')

class Elefante(Animal):
    def emitir_som(self):
        print('Pruuuuuuu...')
    

gato1 = Gato('Felix', 'Branco', 'Siamese')
gato1.apresentar()
gato1.emitir_som()
gato1.arranhar()

cachorro1 = Cachorro('Russo', 'Preto', 'Pastor Alemão')
cachorro2 = Cachorro('Bella', 'Branca', 'Maltes')
cachorro1.apresentar()
cachorro1.emitir_som()
cachorro2.apresentar()

eletante1 = Elefante('Fred', 'Marrom', 'Elefante Asiatico')
eletante1.apresentar()
eletante1.emitir_som()