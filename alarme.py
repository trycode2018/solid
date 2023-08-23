class Alarme:
    
    def __init__(self,estado:bool) -> None:
        self.__estado = estado
        
    def get_estado(self) -> bool:
        return self.__estad
    o
    
    def set_estado(self,valor:bool) -> None:
        if isinstance(valor,bool):
            self.__estado = valor
        

al = Alarme(True)
al.set_estado('ola')
print(al.get_estado())


   