# 📊 PROJETO DE ENGENHARIA DE DADOS

## 👨‍💻 Integrantes

* Rafael Pacífico
* Walter Neto
* Fabio Pereira
* Nicolas Rocha

---

## 🎯 Objetivo

Desenvolver um pipeline de ETL (Extract, Transform, Load), integrando dados de diferentes fontes e criando um dashboard analítico no Power BI.

---

## ⚙️ Tecnologias Utilizadas

* Python (Pandas)
* Power BI
* GitHub

---

## 🔄 Processo ETL

### 📥 Extração

* Arquivo CSV: pedidos
* Arquivo CSV: clientes
* Arquivo JSON: produtos

### 🔧 Transformação

* Limpeza de dados
* Padronização de datas
* Criação da coluna `valor_total` (quantidade × valor_unitário)

### 🔗 Integração

* Junção das tabelas de pedidos, clientes e produtos

### 📤 Carga

* Geração de uma base consolidada (`base_consolidada.csv`)

---

## 📊 Dashboard (Power BI)

Foi desenvolvido um dashboard interativo utilizando Power BI, contendo:

* Receita por região
* Top produtos mais vendidos
* Evolução mensal da receita

📁 O arquivo do Power BI está incluído no repositório (`.pbix`).

---

## 📁 Estrutura do Projeto

* dados/ → arquivos de entrada
* scripts/ → códigos Python do ETL
* output/ → base consolidada gerada
* arquivo `.pbix` → dashboard Power BI

---

## 🚀 Resultado

O projeto integra múltiplas fontes de dados, aplica transformações e disponibiliza análises visuais para apoio à tomada de decisão.

