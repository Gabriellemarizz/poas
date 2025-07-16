from sqlmodel import select
from app.models import Pedido
from app.database import get_session

def get_pedido_by_id(id_pedido: int):
    with get_session() as session:
        statement = select(Pedido).where(Pedido.IdPedido == id_pedido)
        result = session.exec(statement).first()
        return result
