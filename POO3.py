# Molde do Pokemon

# Vamos ter vários atributos

# A classe é um molde que vamos criar para poder construir coisas

class MoldePokemon:
    def __init__(self, nome, altura, peso, hp, ataque, tipo):
        self.nome = nome
        self.altura = altura
        self.peso = peso
        self.hp = hp
        self.ataque = ataque
        self.tipo = tipo
    
    def mostrar_nome_pokemon(self):
        print(f"O nome do pokemon é: {self.nome}")
    
    def mostrar_altura_pokemon(self):
        print(f"A altura do pokemon é: {self.altura}")
    
    def mostrar_peso_pokemon(self):
        print(f"O peso do pokemon é: {self.peso}")
        
    def mostrar_hp_pokemon(self):
        print(f"O hp do pokemon é: {self.hp}")
    
    def mostrar_ataque_pokemon(self):
        print(f"O ataque do pokemon é: {self.ataque}")

    def mostrar_tipo_pokemon(self):
        print(f"O tipo do pokemon é: {self.tipo}")
    
    def mostrar_dados_pokemon(self):
        print(f"HP: {self.hp}")
        print(f"Tipo: {self.tipo}")
        print(f"Ataque: {self.ataque}")
        print(f"Altura: {self.altura}")
        print(f"Peso: {self.peso}")
# Chegou a hora de pegar a classe e de fato construir essas coisas
# Por enquanto, a gente ainda tem apenas o molde
# Construir dentro da Orientação a Objetos significa criar um Objeto

pikachu = MoldePokemon("Pikachu", 50, 3, 300, "Choque do trovão", "Eletrico")
chatizard = MoldePokemon("Charizard", 200, 1500, 450, "Lanca chamas", "Fogo")
miau = MoldePokemon("Miau", 45, 2.5, 100, "Unhada", "Normal")

pikachu.mostrar_nome_pokemon()
pikachu.mostrar_dados_pokemon()
chatizard.mostrar_nome_pokemon()
chatizard.mostrar_dados_pokemon()
miau.mostrar_nome_pokemon()
miau.mostrar_dados_pokemon()