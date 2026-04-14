import instaloader
from pathlib import Path

def sim_ou_nao(pergunta):
    """Auxiliar para converter entrada do usuário em Booleano"""
    resposta = input(f"{pergunta} (s/n): ").strip().lower()
    return resposta == 's'

url = input("Digite a URL do post do Instagram: ").strip()

if not url:
    print("Nenhuma URL foi informada.")
else:
    # --- Menu de Escolhas ---
    print("--- Configurações de Download ---")
    quer_fotos = sim_ou_nao("Deseja baixar as fotos/capa?")
    
    # Inicializa o objeto com as escolhas do usuário
    L = instaloader.Instaloader(
        download_pictures=quer_fotos,
        download_videos=True, # Mantemos True pois o foco é o vídeo
        download_geotags=False
    )

    destino_informado = input("Digite a pasta onde deseja salvar: ").strip()

    if not destino_informado:
        print("Nenhum caminho foi informado.")
    else:
        destino = Path(destino_informado).expanduser()
        destino.mkdir(parents=True, exist_ok=True)

        try:
            # Extrai o shortcode da URL
            shortcode = url.split("/")[-2] if url.endswith("/") else url.split("/")[-1]
            
            print("Buscando post...")
            post = instaloader.Post.from_shortcode(L.context, shortcode)

            # Executa o download com as preferências definidas
            L.download_post(post, target=str(destino))
            
            print(f"Processo concluído! Verifique a pasta: {destino.resolve()}")

        except Exception as e:
            print(f"Erro ao processar: {e}")