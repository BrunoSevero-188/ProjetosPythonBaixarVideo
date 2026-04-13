from pathlib import Path
from pytubefix import YouTube
from pytubefix.cli import on_progress

# Solicita a URL do vídeo ao usuário e remove espaços extras
url = input("Digite a URL do vídeo do YouTube que deseja baixar: ").strip()

# Verifica se o usuário digitou algo
if not url:
    print("Nenhuma URL foi informada.")
else:
    # Solicita o diretório de destino
    destino_informado = input("Digite a pasta onde o vídeo deve ser salvo: ").strip()

    if not destino_informado:
        print("Nenhum caminho foi informado.")
    else:
        # Gerencia o caminho da pasta:
        # expanduser() resolve o símbolo '~' (pasta do usuário) se for utilizado
        destino = Path(destino_informado).expanduser()
        
        # Cria a pasta caso ela não exista (parents=True cria pastas pai se necessário)
        destino.mkdir(parents=True, exist_ok=True)

        # Instancia o objeto YouTube com o callback de progresso para exibir a barra no terminal
        yt = YouTube(url, on_progress_callback=on_progress)
        
        # Exibe informações básicas do vídeo antes de iniciar
        print(f"Título: {yt.title}")
        print(f"Autor: {yt.author}")
        print(f"Data de publicação: {yt.publish_date}")
        print(f"Salvando em: {destino.resolve()}")
        print("Baixando...")

        # Seleciona a stream de vídeo com a maior resolução disponível (progressiva)
        # e inicia o download para o caminho especificado
        yt.streams.get_highest_resolution().download(output_path=str(destino))

        print("Download concluído!")