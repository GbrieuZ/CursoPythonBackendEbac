def meu_decorator(func): #Esse func pode ser qualquer nome
    def wrapper():
        print("Antes da execução da função.")
        func() # Chama a função despedida
        print("Depois da execução da função.")

    return wrapper

@meu_decorator
def despedida():
    print("tchau!")
    

@meu_decorator
def cheguei():
    print("Oii")


cheguei()
despedida()