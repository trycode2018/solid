class Loja:
    
    tarifa = 1.03
    
    def __init__(self,endereco:str):
        self.__endereco = endereco
        
    @classmethod
    def vender(cls)->int:
        return 40 * cls.tarifa
    
    
    def apresentar_endereco(self) ->None:
        return self.__endereco
    
    @classmethod
    def alterar_tarifa(cls,nova_tarifa:int) -> None:
        if isinstance(nova_tarifa,int):
            cls.tarifa = nova_tarifa
        else:
            print('Valor da tarifa invalida')
            
l = Loja
#l.alterar_tarifa(2)
print(l.vender())