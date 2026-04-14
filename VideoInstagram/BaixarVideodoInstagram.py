import instaloader  # Importa a biblioteca para interagir com o Instagram
from pathlib import Path  # Importa biblioteca para caminhos de arquivos

# Função simples para converter 's' em True e 'n' em False
def sim_ou_nao(pergunta):
    resposta = input(f"{pergunta} (s/n): ").strip().lower()
    return resposta == 's'

url = input("Digite a URL do Instagram: ").strip()

if not url:
    print("Nenhuma URL foi informada.")
else:
    # Pergunta apenas se o usuário quer a foto de capa (Thumbnail)
    quer_capa = sim_ou_nao("Deseja baixar a capa (foto) do vídeo?")
    
    # Configura o Instaloader para baixar apenas o necessário (evita arquivos extras)
    L = instaloader.Instaloader(
        download_pictures=quer_capa,  # Baixa foto apenas se o usuário quis
        download_videos=True,         # Sempre tenta baixar o vídeo
        download_video_thumbnails=quer_capa,
        download_geotags=False,       # Não baixa localização
        download_comments=False,      # Não baixa comentários
        save_metadata=False,          # Não cria arquivo .json de dados
        post_metadata_txt_pattern=""  # Não cria arquivo .txt de legenda
    )

    escolha_pasta = input("\nDeseja escolher a pasta? (s/n): ").strip().lower()

    if escolha_pasta == 's':
        destino_informado = input("Digite o caminho: ").strip()
        destino = Path(destino_informado).expanduser() if destino_informado else Path.home() / "Downloads"
    else:
        destino = Path.home() / "Downloads"
    
    destino.mkdir(parents=True, exist_ok=True)

    try:
        # Limpa a URL para extrair apenas o código identificador do post (shortcode)
        url_limpa = url.rstrip('/')
        shortcode = url_limpa.split("/")[-1]
        
        # Faz o download do post usando o identificador extraído
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        print(f"Baixando post de: {post.owner_username}")
        L.download_post(post, target=str(destino))
        
        print(f"Download do Instagram concluído!")

    except Exception as e:
        print(f"Erro no Instagram: {e}")