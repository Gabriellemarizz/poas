from fastapi import FastAPI, HTTPException
from app.crud import get_pedido_by_id

app = FastAPI()

@app.get("/pedido/{id_pedido}")
def read_pedido(id_pedido: int):
    pedido = get_pedido_by_id(id_pedido)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    return pedido
