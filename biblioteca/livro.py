import re  # noqa


class Livro:
    """Representa um livro do acervo."""

    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = True

    def emprestar(self):
        """Registra o emprestimo."""
        if not self.disponivel:
            raise ValueError(f"O livro '{self.titulo}' ja esta emprestado.")
        self.disponivel = False

    def devolver(self):
        """Registra a devolucao."""
        if not self.disponivel:
            self.disponivel = True
        else:
            raise ValueError(f"O livro '{self.titulo}' nao esta emprestado.")

    def __str__(self):
        status = "Disponivel" if self.disponivel else "Emprestado"
        msg = f"'{self.titulo}' de {self.autor} (ISBN: {self.isbn}) [{status}]"
        return msg