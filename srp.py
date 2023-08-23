class Sistema:
    
    def __init__(self):
        self.nome 
        self.idade 
    
    def cadastrar(self,nome:str,idade:int)->None:
        if self.__verificar_dados(nome,idade):
            self.__armazenar_usuario(nome,idade)
        else:
            self.__indicar_erro()
        
    
    def __verificar_dados(self,nome:str,idade:int):
        if isinstance(nome,str) and isinstance(idade,int):
            return True
        else:
            return False
        
    def __armazenar_usuario(self,nome:str,idade:int):
        print('Acessando o banco de dados...')
        print('Cadastrar o usuario {}, idade {}'.format(nome,idade))
    
    def __indicar_erro():
        print('dados invalidos') 
        

user = Sistema('Wilson',23)
user.cadastrar('Henrique Ventura',23)
