class Circo:
    
    def apresentar(self,apresentador:any):
        apresentador.apresentar_show()
        
class Palhaco:

    def apresentar_show(self):
        print('Palhaco apresentando seu show...')
        
class Malabarista:
    
    def apresentar_show(self):
        print('Malabarista apresentando seu show ...')
        

circo = Circo()
mal = Malabarista()
pal = Palhaco()


circo.apresentar(mal)

