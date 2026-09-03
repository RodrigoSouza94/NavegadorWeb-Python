# historico.py
class HistoricoPilha:
    """
    Classe que implementa o histórico de páginas
    como uma 'pilha' (LIFO).
    """
    def __init__(self):
        # Usamos uma lista nativa do Python como pilha
        self.stack = []

    def visitar_pagina(self, url):
        """
        Empilha a nova URL no topo.
        """
        self.stack.append(url)

    def voltar(self):
        """
        Retira (pop) a última URL visitada, se houver.
        Retorna essa URL, ou None se estiver vazia.
        """
        if self.stack:
            return self.stack.pop()
        return None

    def pagina_atual(self):
        """
        Retorna a página atual (topo da pilha) sem remover.
        Retorna None se estiver vazia.
        """
        if self.stack:
            return self.stack[-1]
        return None
