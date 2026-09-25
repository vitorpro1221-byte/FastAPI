from fastapi import FastAPI
from pydantic import BaseModel



app = FastAPI()

class Livro(BaseModel):
    id: int
    titulo: str
    autor: str

livros = [
    {"id": 1, "titulo": "Duna", "autor": "Frank Herbert"},
    {"id": 2, "titulo": "1984", "autor": "George Orwell"},
    {"id": 3, "titulo": "O Hobbit", "autor": "J.R.R. Tolkien"},
]


@app.post("/livros")
def criar_livro(livro: Livro):
    livros.append(livro.model_dump())
    return livro

@app.get("/livros")
def listar_todos_livros():
    return livros

@app.get("/livros/{id_livro}")
def listar_livros(id_livro: int):
    for livro in livros:
        if livro["id"] == id_livro:
            return livro
    return {"mensagem": "Livro não encontrado"}

@app.get("/livros/titulo/{titulo_livro}")
def listar_livros_por_titulo(titulo_livro: str):  
    for livro in livros:
        if livro["titulo"] == titulo_livro:
            return livro
    return {"mensagem": "Livro não encontrado"}

@app.get("/livros/autor/buscar")
def listar_livros_por_autor(autor_livro: str):
    livros_do_autor = []
    for livro in livros:
        if livro["autor"] == autor_livro:
            livros_do_autor.append(livro)
            
    if livros_do_autor:
        return livros_do_autor
    else:
        return {"mensagem": "Nenhum livro encontrado para o autor especificado"}