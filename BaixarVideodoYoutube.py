from pathlib import Path

from pytubefix import YouTube
from pytubefix.cli import on_progress

url = input("Digite a URL do vídeo do YouTube que deseja baixar: ").strip()

if not url:
    print("Nenhuma URL foi informada.")
else:
    destino_informado = input("Digite a pasta onde o vídeo deve ser salvo: ").strip()

    if not destino_informado:
        print("Nenhum caminho foi informado.")
    else:
        destino = Path(destino_informado).expanduser()
        destino.mkdir(parents=True, exist_ok=True)

        yt = YouTube(url, on_progress_callback=on_progress)
        print(f"Título: {yt.title}")
        print(f"Autor: {yt.author}")
        print(f"Data de publicação: {yt.publish_date}")
        print(f"Salvando em: {destino.resolve()}")
        print("Baixando...")

        yt.streams.get_highest_resolution().download(output_path=str(destino))

        print("Download concluído!")
