import pytest
from biblioteca.livro import Livro
from biblioteca.acervo import Acervo


def test_adicionar_e_total_livros():
    acervo = Acervo("Biblioteca Municipal")
    livro = Livro("Python Fluente", "Luciano Ramalho", "987654321")
    acervo.adicionar_livro(livro)
    assert acervo.total_livros() == 1


def test_buscar_por_titulo_case_insensitive():
    acervo = Acervo("Biblioteca Municipal")
    livro = Livro("Python Fluente", "Luciano Ramalho", "987654321")
    acervo.adicionar_livro(livro)
    
    resultados = acervo.buscar_por_titulo("python")
    assert len(resultados) == 1
    assert resultados[0].titulo == "Python Fluente"


def test_buscar_por_autor_case_insensitive():
    acervo = Acervo("Biblioteca Municipal")
    livro = Livro("Python Fluente", "Luciano Ramalho", "987654321")
    acervo.adicionar_livro(livro)
    
    resultados = acervo.buscar_por_autor("LUCIANO")
    assert len(resultados) == 1
    assert resultados[0].autor == "Luciano Ramalho"


def test_livros_disponiveis_e_emprestados():
    acervo = Acervo("Biblioteca Municipal")
    livro1 = Livro("Livro A", "Autor A", "111")
    livro2 = Livro("Livro B", "Autor B", "222")
    acervo.adicionar_livro(livro1)
    acervo.adicionar_livro(livro2)
    
    livro1.emprestar()
    
    assert livro1 in acervo.livros_emprestados()
    assert livro2 in acervo.livros_disponiveis()