import requests

def buscar_usuarios(username, tipo):
    url = f"https://api.github.com/users/{username}/{tipo}"

    usuarios = []
    pagina = 1

    while True:
        response = requests.get(url, params={
            "per_page": 100,
            "page": pagina
        })

        if response.status_code != 200:
            print(f"Erro ao consultar GitHub: {response.status_code}")
            return []

        dados = response.json()

        if not dados:
            break

        usuarios.extend(dados)
        pagina += 1

    return usuarios


username = input("Digite seu usuário do GitHub: ")

following = buscar_usuarios(username, "following")
followers = buscar_usuarios(username, "followers")

following_names = {user["login"] for user in following}
followers_names = {user["login"] for user in followers}

nao_seguem_de_volta = following_names - followers_names

print("\n===== NÃO SEGUEM DE VOLTA =====")

if nao_seguem_de_volta:
    for numero, usuario in enumerate(sorted(nao_seguem_de_volta), start=1):
        print(f"{numero}. @{usuario} - https://github.com/{usuario}")
else:
    print("Todos os usuários que você segue seguem você de volta!")

print(f"\nTotal: {len(nao_seguem_de_volta)} usuários")

print(f"\nVocê segue: {len(following)} usuários")
print(f"Seus seguidores: {len(followers)} usuários")