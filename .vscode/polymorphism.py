# Polymorphism

class Cachorro:
    def emitir_som(self):
        print('au au au!')


class Gato:
    def emitir_som(self):
        print('miau!')


animais = [Cachorro(), Gato()]

for animal in animais:
    animal.emitir_som()


