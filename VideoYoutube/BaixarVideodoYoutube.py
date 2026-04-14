from pathlib import Path
from pytubefix import YouTube
from pytubefix.cli import on_progress

# Solicita a URL do vídeo
url = input("Digite a URL do vídeo do YouTube que deseja baixar: ").strip()

if not url:
    print("Nenhuma URL foi informada.")
else:
    # Pergunta sobre a pasta de destino
    escolha_pasta = input("Quer que o vídeo seja salvo em uma pasta de sua escolha? (s/n): ").strip().lower()

    if escolha_pasta == 's':
        destino_informado = input("Digite a pasta onde o vídeo deve ser salvo: ").strip()
        if not destino_informado:
            print("Caminho não informado. Usando pasta padrão...")
            destino = Path.home() / "Downloads"
        else:
            destino = Path(destino_informado).expanduser()
    else:
        # Define automaticamente a pasta Downloads do usuário
        destino = Path.home() / "Downloads"
        print(f"O vídeo será salvo em: {destino}")

    # Cria a pasta caso ela não exista
    destino.mkdir(parents=True, exist_ok=True)

    try:
        # Instancia o objeto YouTube
        yt = YouTube(url, on_progress_callback=on_progress)
        
        print(f"Título: {yt.title}")
        print(f"Autor: {yt.author}")
        print(f"Salvando em: {destino.resolve()}")
        print("Baixando...")

        # Realiza o download
        yt.streams.get_highest_resolution().download(output_path=str(destino))

        print("Download concluído!")
        
    except Exception as e:
        print(f"Ocorreu um erro: {e}")