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
from pydantic import BaseModel
from typing import Optional
app = FastAPI()

meus_livrozinhos = {}

class Livro(BaseModel):
    nome_livro: str
    autor_livro: str
    ano_livro: int

@app.get("/livros")
def get_livros():
    if not meus_livrozinhos:
        return {"message": "Nenhum livro cadastrado"}
    else:
        return {"Livros": meus_livrozinhos}
# id do livro
# nome do livro
# autor do livro
# ano de publicação

@app.post("/adiciona")
def post_livros(id_livro: int, livro: Livro):
    if id_livro in meus_livrozinhos:
        raise HTTPException(status_code=400, detail="Livro já cadastrado")
    else:
        meus_livrozinhos[id_livro] = livro.dict()
        return {"message": "Livro adicionado com sucesso!"}
    

@app.put("/atualiza/{id_livro}")
def put_livros(id_livro: int, livro: Livro):
    meu_livro = meus_livrozinhos.get(id_livro)
    if not meu_livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    else:
        # Eu jogo essa informação dentro do meu antigo dicionário (que é o meus_livrozinhos)
        # E NÃOooooo dentro da REFERENCIA do antigo dicionário
        # Antigo dicionário != Referencia do antigo dicionário
        meus_livrozinhos[id_livro] = livro.dict() 
        
        
        return {"message": "Livro atualizado com sucesso!"}
    
@app.delete("/deletar/{id_livro}")
def delet_livro(id_livro: int):
    if id_livro not in meus_livrozinhos:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    else:
        del meus_livrozinhos[id_livro]
        return {"message": "Livro deletado com sucesso!"}