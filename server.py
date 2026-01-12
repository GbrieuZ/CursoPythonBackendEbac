# API de Livros

# GET, POST, PUT e DELETE

# GET - Buscar os dados dos livros (Create)
# POST - Adicionar novos livros (Read)
# PUT - Atualizar informações dos livros (Update)
# DELETE - Deletar informações dos livros (Delete)

# Vamos acessar nosso ENDPOINT
# E vamos acessar os PATH's desse endpoint
# Query Strings

#CRUD - Create, Read, Update, Delete

from fastapi import FastAPI, HTTPException

app = FastAPI()

dict = {}

@app.get("/livros")
def get_livros():
    if not dict:
        return {"message": "Nenhum livro cadastrado"}
    else:
        return {"Livros": dict}


# id do livro
# nome do livro
# autor do livro
# ano de publicação

@app.post("/adiciona")
def post_livros(id_livro: int, nome_livro: str, autor_livro: str, ano_livro: int):
    if id_livro in dict:
        raise HTTPException(status_code=400, detail="Livro já cadastrado")
    else:
        dict[id_livro] = {"nome": nome_livro, "autor": autor_livro, "ano": ano_livro}
        return {"message": "Livro adicionado com sucesso!"}
    

@app.put("/atualiza/{id_livro}")
def put_livros(id_livro: int, nome_livro: str, autor_livro: str, ano_livro: int):
    meu_livro = dict.get(id_livro)
    if not meu_livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    else:
        if nome_livro: # Validando se o campo exite
            meu_livro["nome"] = nome_livro # Atualizando o campo com a nova informação
        if autor_livro:
            meu_livro["autor"] = autor_livro
        if ano_livro:
            meu_livro["ano"] = ano_livro
        
        return {"message": "Livro atualizado com sucesso!"}
    
@app.delete("/deletar/{id_livro}")
def delet_livro(id_livro: int):
    if id_livro not in dict:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    else:
        del dict[id_livro]
        
        return {"message": "Livro deletado com sucesso!"}