# Uma classe é um Molde.
# Vamos usar esses Molde para construir coisas que queremos, que tem um mesmo padrão 


# HP
# Tipo do meu Pokemon (Terra, Elétrico, Fogo, etc...)
# Quais seus ataques (Choque do trovão)
# Altura
# Peso
# Nome

# Hp - 300
# Tipo -  Eletrico
# Ataque - Choque do trovão
# Altura - 50cm
# Peso - 15kg
# Nome - Pikachu

# Hp - 450
# Tipo -  Fogo
# Ataque - Lança chamas
# Altura - 2m
# Peso - 1500kg
# Nome - Charizard

class MoldePokemon:
    # Método construtor
    # Self tem a responsabilidade de armazenar e manipular essas informações dos atributos 
    def __init__(self, nome, hp, tipo, ataque, altura, peso):
        self.nome = nome
        self.hp = hp
        self.tipo = tipo
        self.ataque = ataque
        self.altura = altura
        self.peso = peso
    
    def mostrar_nome_pokemon(self):
        print(f"O nome do pokemon é: {self.nome}")
        
    def mostrar_dados_pokemon(self):
        print(f"HP: {self.hp}")
        print(f"Tipo: {self.tipo}")
        print(f"Ataque: {self.ataque}")
        print(f"Altura: {self.altura}")
        print(f"Peso: {self.peso}")
