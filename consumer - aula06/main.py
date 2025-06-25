#pip install requests
import requests
import json

def listar_livros(url):
    r = requests.get(f"{url}/livros")
    print(f"Status: {r.status_code}")
    print(r.text)

def pesquisar_livro(url, titulo):
    r = requests.get(f"{url}/livros/{titulo}")
    print(f"Status: {r.status_code}")
    print(r.text)

def cadastrar_livro(url, livro):
    r = requests.post(f"{url}/livros", json=livro)
    print(f"Status: {r.status_code}")
    print(r.text)

def deletar_livro(url, titulo):
    r = requests.delete(f"{url}/livros/{titulo}")
    print(f"Status: {r.status_code}")
    print(r.text)

def editar_livro(url, titulo):
    # vai checar se existe o livro aqui
    r = requests.get(f"{url}/livros/{titulo}")
    if r.status_code == 404:
        print("Livro não encontrado!")
        return
    
    print("Digite os novos dados do livro (deixe em branco para manter o valor atual):")
    novo_titulo = input(f"Novo título ({titulo}): ") or titulo
    ano_atual = json.loads(r.text).get('ano', '')
    novo_ano = input(f"Novo ano ({ano_atual}): ") or ano_atual
    edicao_atual = json.loads(r.text).get('edicao', '')
    nova_edicao = input(f"Nova edição ({edicao_atual}): ") or edicao_atual
    
    livro = {
        "titulo": novo_titulo,
        "ano": int(novo_ano) if novo_ano else ano_atual,
        "edicao": int(nova_edicao) if nova_edicao else edicao_atual
    }
    
    r = requests.put(f"{url}/livros/{titulo}", json=livro)
    print(f"Status: {r.status_code}")
    print(r.text)

def main():
    url = "http://127.0.0.1:8000/livros"
    
    while True:
        print("\nMenu:")
        print("1 - Listar todos os livros")
        print("2 - Pesquisar livro por título")
        print("3 - Cadastrar um livro")
        print("4 - Deletar um livro")
        print("5 - Editar um livro")
        print("6 - Sair")
        
        opcao = input("Escolha uma opção (1-6): ")
        
        if opcao == "1":
            listar_livros(url)
        
        elif opcao == "2":
            titulo = input("Digite o título do livro para pesquisar: ")
            pesquisar_livro(url, titulo)
        
        elif opcao == "3":
            titulo = input("Digite o título do livro: ")
            ano = input("Digite o ano do livro: ")
            edicao = input("Digite a edição do livro: ")
            livro = {
                "titulo": titulo,
                "ano": int(ano) if ano else 0,
                "edicao": int(edicao) if edicao else 0
            }
            cadastrar_livro(url, livro)
        
        elif opcao == "4":
            titulo = input("Digite o título do livro para deletar: ")
            deletar_livro(url, titulo)
        
        elif opcao == "5":
            titulo = input("Digite o título do livro para editar: ")
            editar_livro(url, titulo)
        
        elif opcao == "6":
            print("Saindo...")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()