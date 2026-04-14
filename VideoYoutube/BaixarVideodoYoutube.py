from pathlib import Path  # Importa biblioteca para lidar com caminhos de arquivos
from pytubefix import YouTube  # Importa a classe principal do YouTube
from pytubefix.cli import on_progress  # Importa a função que mostra a barra de progresso

# Solicita o link e remove espaços em branco nas extremidades
url = input("Digite a URL do vídeo do YouTube: ").strip()

if not url:
    print("Nenhuma URL foi informada.")
else:
    # Pergunta ao usuário sobre a preferência de local
    escolha_pasta = input("Deseja salvar em uma pasta específica? (s/n): ").strip().lower()

    if escolha_pasta == 's':
        destino_informado = input("Digite o caminho da pasta: ").strip()
        # Converte o texto em um caminho real (expanduser resolve o '~' do Linux/Mac)
        destino = Path(destino_informado).expanduser() if destino_informado else Path.home() / "Downloads"
    else:
        # Define o caminho padrão como a pasta Downloads do usuário atual
        destino = Path.home() / "Downloads"

    # Cria a pasta de destino caso ela ainda não exista no computador
    destino.mkdir(parents=True, exist_ok=True)

    try:
        # Cria o objeto do vídeo e define a função que será chamada enquanto o download ocorre
        yt = YouTube(url, on_progress_callback=on_progress)
        
        print(f"\nTítulo: {yt.title}")  # Exibe o título do vídeo
        print(f"Salvando em: {destino.resolve()}")  # Mostra o caminho completo da pasta
        
        # Filtra a stream com maior resolução e inicia o download na pasta destino
        yt.streams.get_highest_resolution().download(output_path=str(destino))
        print("\nDownload do YouTube concluído!")

    except Exception as e:
        print(f"Erro no YouTube: {e}")  # Captura e exibe qualquer erro que ocorra