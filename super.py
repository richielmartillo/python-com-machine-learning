#Sistema de Escola
class Escola():
    def __init__(self, nome, idade, status):
        self.nome = nome
        self.idade = idade
        self.status = status

    def Apresentar(self):
        print(f'Meu nome é {self.nome}') 
   
    def verificar_status(self):
        print(f'Status: {"ATIVO" if self.status else "INATIVO"}')

class Aluno(Escola):
    def __init__(self, nome, idade, status, ano):
       super().__init__(nome, idade, status)
       self.ano = ano

    def Apresentar(self):
        super().Apresentar()
        print(f'Eu sou um aluno da escola')


class Professor(Escola):
    def __init__(self, nome, idade, status, materia):
       super().__init__(nome, idade, status)
       self.materia = materia
    def Apresentar(self):
        super().Apresentar()
        print(f'Eu sou um professor da escola')

       
class Asistente(Escola):
    def __init__(self, nome, idade, status, bloco):
       super().__init__(nome, idade, status)
       self.bloco = bloco       

    def Apresentar(self):
        super().Apresentar()
        print(f'Eu sou um(a) assistente da escola')       

#Instanciando os objetos
a1 = Aluno(nome='Terminator', idade=45, status=True, ano=2)
p1 = Professor(nome='Leonardo Da Vinci',  idade=55, status=True, materia='Estatistica')
as1 = Asistente(nome='Luciana Salazar',  idade=22, status=False, bloco='Bloco C')

p1.Apresentar()
p1.verificar_status()
