# main.py
from historico import HistoricoPilha
from downloads import FilaDownloads

def simular_navegador():
    # Criamos instâncias das duas classes
    historico = HistoricoPilha()
    fila_down = FilaDownloads()

    # Simulando navegação
    historico.visitar_pagina("https://www.pudim.com.br/")
    historico.visitar_pagina("https://www.palmeiras.com.br/")
    historico.visitar_pagina("https://www.deepseek.com/")

   

    # Verificando a página atual
    print("Página atual:", historico.pagina_atual())  # Deve ser site3

    # Voltando uma página
    url_voltada = historico.voltar()
    print("Voltou da página:", url_voltada)           # Deve ser site3
    print("Página atual agora:", historico.pagina_atual())  # Deve ser site2

    # Simulando downloads
    fila_down.novo_download("video.mp4")
    fila_down.novo_download("musica.mp3")

    print("Próximo download:", fila_down.proximo_download())  # 'video.mp4'
    concluido = fila_down.download_concluido()
    print("Download concluído:", concluido)                   # 'video.mp4'
    print("Restante na fila:", fila_down.proximo_download())  # 'musica.mp3'

if __name__ == "__main__":
    simular_navegador()
