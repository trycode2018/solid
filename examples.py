from typing import Type

class Pessoa:
    
    def __init__(self,nome,idade,altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        
    def apresentar_info(self) -> None:
        print('{} tem {} anos de idade, e mede {} de altura...'.format(self.nome,self.idade,self.altura))
        
wilson = Pessoa('Henrique Ventura',24,1.73)

wilson.apresentar_info()