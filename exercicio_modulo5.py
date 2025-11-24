# Criei uma classe Animal com atributos de nome e idade.
class Animal():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
# Função para emitir um som genérico
    def emiti_som(self):
        return "O animal emitiu um som genérico"
    
# Nova classe Cachorro que herda da classe Animal 
# implementa a função emiti_som, nesse caso para o cachorro

class Cachorro(Animal):
    def emiti_som(self):
        return "O cachorro latiu!"

# Nova classe Gato que herda da classe Animal
# inplementa a função emiti_som, nesse caso para o gato
class Gato(Animal):
    def emiti_som(self):
        return "O gato miou!"

cachorro = Cachorro("Rex", 3)
print(cachorro.emiti_som())

gato = Gato("Garfield", 2)
print(gato.emiti_som())

teste = Animal("Teste", 1)
print(teste.emiti_som())