import os
import pandas as pd

from src.analise import *

# Cria pasta de gráficos automaticamente
os.makedirs("outputs", exist_ok=True)

# Ler dataset
df = pd.read_csv(
    "datasets/dadosProcessados/final_data.csv"
)

# Chamar funções
renda_evasao(df)
renda_mortalidade(df)
renda_acesso_superior(df)
renda_conclusao_superior(df)
escolarizacao_acesso_superior(df)
heatmap_geral(df)

print("FOOOOOI xDDDD")