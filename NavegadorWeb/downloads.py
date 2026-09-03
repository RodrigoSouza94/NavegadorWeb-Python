# downloads.py
from collections import deque

class FilaDownloads:
    """
    Classe que implementa a fila de downloads (FIFO).
    """
    def __init__(self):
        # Usamos 'deque' para ter enqueue/dequeue eficientes
        self.queue = deque()

    def novo_download(self, arquivo):
        """
        Insere um novo arquivo de download no fim da fila.
        """
        self.queue.append(arquivo)

    def download_concluido(self):
        """
        Remove e retorna o arquivo que está no começo da fila.
        Retorna None se a fila estiver vazia.
        """
        if self.queue:
            return self.queue.popleft()
        return None

    def proximo_download(self):
        """
        Retorna o primeiro arquivo da fila, sem removê-lo.
        Retorna None se estiver vazia.
        """
        if self.queue:
            return self.queue[0]
        return None
