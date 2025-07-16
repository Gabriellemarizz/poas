import requests

def main():
    id_pedido = input("Digite o ID do pedido: ")
    try:
        id_int = int(id_pedido)
        response = requests.get(f"http://127.0.0.1:8000/pedido/{id_int}")
        if response.status_code == 200:
            print(response.json())
        else:
            print("Erro:", response.status_code, "-", response.json().get("detail"))
    except ValueError:
        print("ID inválido. Digite um número inteiro.")

if __name__ == "__main__":
    main()
