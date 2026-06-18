import pandas as pd
import random
from datetime import datetime, timedelta
import os

print("🚀 Gerando pedidos...")

clientes = list(range(101,136))
produtos = list(range(501,521))

dados = []
data_inicio = datetime(2025,1,1)

cliente_top = 101
id_pedido = 1

for _ in range(40):
    dados.append([
        id_pedido, cliente_top,
        random.choice(produtos),
        random.randint(1,5),
        (data_inicio + timedelta(days=random.randint(0,364))).strftime('%Y-%m-%d'),
        random.choice([150,300,500,800,1200,2200,3500])
    ])
    id_pedido +=1

for cliente in clientes:
    if cliente == cliente_top:
        continue
    for _ in range(5):
        dados.append([
            id_pedido, cliente,
            random.choice(produtos),
            random.randint(1,5),
            (data_inicio + timedelta(days=random.randint(0,364))).strftime('%Y-%m-%d'),
            random.choice([150,300,500,800,1200,2200,3500])
        ])
        id_pedido +=1

while len(dados) < 400:
    dados.append([
        id_pedido,
        random.choice(clientes),
        random.choice(produtos),
        random.randint(1,5),
        (data_inicio + timedelta(days=random.randint(0,364))).strftime('%Y-%m-%d'),
        random.choice([150,300,500,800,1200,2200,3500])
    ])
    id_pedido +=1

df = pd.DataFrame(dados, columns=[
    'id_pedido','id_cliente','id_produto',
    'quantidade','data_pedido','valor_unitario'
])

base = os.path.dirname(__file__)
caminho = os.path.join(base,'..','dados')
os.makedirs(caminho, exist_ok=True)

df.to_csv(os.path.join(caminho,'pedidos.csv'), index=False)

print("✅ 400 pedidos gerados!")