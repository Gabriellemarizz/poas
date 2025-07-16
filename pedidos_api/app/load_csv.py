import pandas as pd
from app.models import Pedido, SQLModel
from app.database import engine, get_session

def load_data(csv_path: str):
    df = pd.read_csv(csv_path, sep=";", encoding="utf-16", parse_dates=[
    "DataRegistro", "PrazoAtendimento", "DataResposta"
], dayfirst=True)


    SQLModel.metadata.create_all(engine)

    with get_session() as session:
        for _, row in df.iterrows():
            pedido = Pedido(**row.to_dict())
            session.add(pedido)
        session.commit()

if __name__ == "__main__":
    load_data("20250702_Pedidos_csv_2025.csv")
