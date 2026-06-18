import pandas as pd
import os
import json

print("🚀 Iniciando ETL...")

base = os.path.dirname(__file__)

# =========================
# FUNÇÃO CSV SEGURA
# =========================
def carregar_csv(caminho, nome):
    if not os.path.exists(caminho):
        raise FileNotFoundError(f"❌ Arquivo não encontrado: {nome}")

    if os.path.getsize(caminho) == 0:
        raise ValueError(f"❌ Arquivo vazio: {nome}")

    return pd.read_csv(caminho)

# =========================
# FUNÇÃO JSON SEGURA
# =========================
def carregar_json_seguro(caminho):
    if not os.path.exists(caminho):
        raise FileNotFoundError(f"❌ produtos.json não encontrado")

    with open(caminho, 'r', encoding='utf-8') as f:
        conteudo = f.read().strip()

        if conteudo == "":
            raise ValueError("❌ produtos.json está vazio")

        try:
            data = json.loads(conteudo)
        except json.JSONDecodeError as e:
            raise ValueError(f"❌ JSON inválido: {e}")

    return pd.DataFrame(data)

# =========================
# CAMINHOS
# =========================
pedidos_path = os.path.join(base, '..', 'dados', 'pedidos.csv')
clientes_path = os.path.join(base, '..', 'dados', 'clientes.csv')
produtos_path = os.path.join(base, '..', 'dados', 'produtos.json')

# =========================
# EXTRAÇÃO
# =========================
pedidos = carregar_csv(pedidos_path, "pedidos.csv")
clientes = carregar_csv(clientes_path, "clientes.csv")
produtos = carregar_json_seguro(produtos_path)

print("✅ Dados carregados!")

# =========================
# TRANSFORMAÇÃO
# =========================
pedidos['valor_total'] = pedidos['quantidade'] * pedidos['valor_unitario']
pedidos['data_pedido'] = pd.to_datetime(pedidos['data_pedido'], errors='coerce')

# remove dados inválidos
pedidos = pedidos.dropna()

# =========================
# INTEGRAÇÃO
# =========================
df = pedidos.merge(clientes, on='id_cliente', how='inner')
df = df.merge(produtos, on='id_produto', how='inner')

# renomear colunas
df.rename(columns={
    'nome_x': 'nome_cliente',
    'nome_y': 'nome_produto'
}, inplace=True)

# =========================
# LOAD
# =========================
saida = os.path.join(base, '..', 'output')
os.makedirs(saida, exist_ok=True)

arquivo_saida = os.path.join(saida, 'base_consolidada.csv')
df.to_csv(arquivo_saida, index=False)

print("✅ ETL FINALIZADO COM SUCESSO!")
print("📁 Arquivo gerado em:", arquivo_saida)