Claro! Aqui está o conteúdo de um `README.md` com explicações simples e diretas para te ajudar (ou qualquer outra pessoa) a entender como o projeto funciona e como rodar ele:

---

## 📦 PEDIDOS\_API — Consulta de Pedidos via FastAPI + SQLite

Este projeto carrega um arquivo `.csv` com pedidos públicos e cria uma **API** para consultar os dados pelo terminal, via **FastAPI**.
Ele usa **Python**, **SQLModel**, **SQLite**, e uma aplicação simples de terminal para buscar um pedido pelo seu ID.

---

### Sobre a atividade

* Lê um arquivo CSV com os dados dos pedidos.
* Salva tudo em um banco de dados SQLite (`pedidos.db`).
* Cria uma API com FastAPI para buscar pedidos pelo ID.
* Tem uma interface de terminal onde você digita o ID e recebe o resultado (ou erro se não existir).


### Estrutura dos arquivos

```
pedidos_api/
│
├── app/
│   ├── models.py          # Modelo do Pedido
│   ├── database.py        # Conexão com banco SQLite
│   ├── crud.py            # Consulta por ID
│   ├── main.py            # API FastAPI
│   └── load_csv.py        # Carrega o CSV no banco
│
├── terminal_app.py        # App que pergunta o ID e consulta a API
├── pedidos.db             # Banco SQLite (gerado após rodar)
├── requirements.txt       # Dependências do projeto
├── 20250702_Pedidos_csv_2025.csv  # Arquivo com os pedidos
└── README.md              # Este arquivo
```

---

### Para rodar o projeto

#### 1. Clone a pasta `pedidos_api`

#### 2. Crie e ative um ambiente virtual (opcional, mas recomendado)

Windows:

```bash
python -m venv venv
venv\\Scripts\\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

#### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

#### 4. Carregue os dados do CSV para o banco

```bash
python -m app.load_csv
```

aqui o comando lê o arquivo `20250702_Pedidos_csv_2025.csv` e salva os dados em `pedidos.db`.

---

#### 5. Rode a API FastAPI

```bash
uvicorn app.main:app --reload
```

A API vai rodar em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

Lembrar de colocar o /docs no final
---

#### 6. Consulte pedidos no terminal

Com a API rodando, abra outro terminal e digite:

```bash
python terminal_app.py
```

Ele vai te perguntar o ID do pedido. Digite um número e veja os dados!

---

### Se der erro com `utf-8` ao ler o CSV...

Edite o arquivo `app/load_csv.py` e troque:

```python
encoding="utf-8"
```

Por:

```python
encoding="utf-16"
```