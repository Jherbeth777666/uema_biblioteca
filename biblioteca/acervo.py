class Acervo:
    """Gerencia o conjunto de livros de uma biblioteca."""

    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, livro):
        """Adiciona um livro ao acervo."""
        self.livros.append(livro)

    def total_livros(self):
        """Retorna a quantidade total de livros."""
        return len(self.livros)

    def buscar_por_titulo(self, titulo):
        """Busca livros pelo título."""
        return [
            livro
            for livro in self.livros
            if titulo.lower() in livro.titulo.lower()
        ]

    def buscar_por_autor(self, autor):
        """Busca livros pelo autor."""
        return [
            livro
            for livro in self.livros
            if autor.lower() in livro.autor.lower()
        ]

    def livros_disponiveis(self):
        """Retorna os livros disponíveis."""
        return [
            livro
            for livro in self.livros
            if livro.disponivel
        ]

    def livros_emprestados(self):
        """Retorna os livros emprestados."""
        return [
            livro
            for livro in self.livros
            if not livro.disponivel
        ]
