from abc import ABC, abstractmethod

class Bank(ABC): #Creamos la interfaz de banco con 1 atributo vacío y 1 método que luego heredan otras clases
    @abstractmethod
    def bank_name(self): #Atributo del nombre del banco
        pass

    @abstractmethod
    def transfer(self,amount):
        pass
